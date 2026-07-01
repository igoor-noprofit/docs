#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Paths resolved relative to this script (repo root) so the watcher works
# regardless of where the repo is checked out on disk.
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
OBSIDIAN_PATH = os.path.abspath(os.path.join(REPO_ROOT, "..", "IGOOR_VAULT", "DOCS"))
DOCS_PATH = os.path.abspath(os.path.join(REPO_ROOT, "docs"))

class ObsidianFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.rebuild_in_progress = False
        self.debounce_time = 2  # seconds
        self.last_trigger_time = 0
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Only process markdown files
        if not event.src_path.endswith(('.md', '.MD')):
            return
        
        current_time = time.time()
        if current_time - self.last_trigger_time < self.debounce_time:
            return
        
        self.last_trigger_time = current_time
        print(f"File changed: {event.src_path}")
        self.rebuild_docs()
    
    def rebuild_docs(self):
        if self.rebuild_in_progress:
            print("Rebuild already in progress, skipping...")
            return
        
        self.rebuild_in_progress = True
        try:
            print("Rebuilding documentation...")
            
            # Remove existing docs folder
            if os.path.exists(DOCS_PATH):
                subprocess.run(['rmdir', '/s', '/q', DOCS_PATH], shell=True)

            # Create fresh docs folder
            os.makedirs(DOCS_PATH, exist_ok=True)

            # Copy files from Obsidian
            subprocess.run(['xcopy', OBSIDIAN_PATH, DOCS_PATH, '/E', '/I', '/Y'], shell=True)

            # Touch a file in the docs folder to trigger mkdocs live reload
            index_file = os.path.join(DOCS_PATH, "index.md")
            if os.path.exists(index_file):
                current_time = time.time()
                os.utime(index_file, (current_time, current_time))
            else:
                # If index.md doesn't exist, create a temporary file and delete it
                temp_file = os.path.join(DOCS_PATH, ".mkdocs_reload")
                with open(temp_file, 'w') as f:
                    f.write("reload trigger")
                os.remove(temp_file)
            
            # Wait a moment to ensure mkdocs detects the change
            time.sleep(0.5)
            
            print("Documentation rebuilt successfully!")
        except Exception as e:
            print(f"Error rebuilding documentation: {e}")
        finally:
            self.rebuild_in_progress = False

if __name__ == "__main__":
    # Set up the observer to watch the Obsidian folder
    event_handler = ObsidianFileHandler()
    observer = Observer()
    observer.schedule(event_handler, OBSIDIAN_PATH, recursive=True)
    
    print(f"Watching {OBSIDIAN_PATH} for changes...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
