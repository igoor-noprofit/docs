#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
            
            # Copy files from Obsidian to docs folder
            obsidian_path = r"C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS"
            docs_path = r"C:\TMP\IGOOR\docs\docs"
            
            # Remove existing docs folder
            if os.path.exists(docs_path):
                subprocess.run(['rmdir', '/s', '/q', docs_path], shell=True)
            
            # Create fresh docs folder
            os.makedirs(docs_path, exist_ok=True)
            
            # Copy files from Obsidian
            subprocess.run(['xcopy', obsidian_path, docs_path, '/E', '/I', '/Y'], shell=True)
            
            # Touch a file in the docs folder to trigger mkdocs live reload
            index_file = os.path.join(docs_path, "index.md")
            if os.path.exists(index_file):
                current_time = time.time()
                os.utime(index_file, (current_time, current_time))
            else:
                # If index.md doesn't exist, create a temporary file and delete it
                temp_file = os.path.join(docs_path, ".mkdocs_reload")
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
    obsidian_path = r"C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS"
    event_handler = ObsidianFileHandler()
    observer = Observer()
    observer.schedule(event_handler, obsidian_path, recursive=True)
    
    print(f"Watching {obsidian_path} for changes...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
