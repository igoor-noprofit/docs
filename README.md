# IGOOR Documentation

Multi-language documentation site built with MkDocs Material theme, supporting English and French content with a separate builds architecture.

## Quick Start

### Development Mode
```batch
launch.bat
```
- Syncs documentation from Obsidian vault
- Builds both English and French sites
- Starts development server at http://127.0.0.1:8000/
- Enables auto-rebuild when Obsidian files change
- Opens browser automatically

### Production Build
```batch
rebuild.bat
```
- Performs clean build (removes existing site/)
- Builds both English and French sites
- No server started (static files only)
- Ready for deployment

## Project Structure

```
docs/
├─ config/
│  ├─ en/mkdocs.yml          # English site configuration
│  └─ fr/mkdocs.yml          # French site configuration
├─ docs/
│  ├─ en/                    # English content (auto-synced from Obsidian)
│  └─ fr/                    # French content (auto-synced from Obsidian)
├─ overrides/
│  ├─ assets/                # Shared assets (logo, favicon, CSS, JS)
│  └─ partials/
│     └─ header.html         # Language-specific announcements
├─ site/                     # Build output
│  ├─ en/                    # English built site
│  └─ fr/                    # French built site
├─ venv/                     # Python virtual environment
├─ launch.bat                # Development server (with Obsidian sync)
├─ rebuild.bat               # Production build (clean build)
├─ watch_docs.py             # Auto-rebuild script for Obsidian sync
└─ requirements.txt           # Python dependencies
```

## Key Differences: launch.bat vs rebuild.bat

| Aspect | launch.bat | rebuild.bat |
|--------|-----------|-------------|
| **Purpose** | Development workflow | Production build |
| **Obsidian Sync** | ✅ Copies docs from Obsidian vault | ❌ No sync |
| **Virtual Environment** | ✅ Activates venv | ❌ Assumes activated |
| **Clean Build** | ❌ Incremental builds | ✅ Removes entire `site/` directory |
| **Development Server** | ✅ Starts `mkdocs serve` | ❌ No server |
| **Browser** | ✅ Opens Chrome automatically | ❌ No browser |
| **Watch Mode** | ✅ Runs `watch_docs.py` in background | ❌ No watch mode |
| **Auto-rebuild** | ✅ Rebuilds on file changes | ❌ Manual rebuild required |
| **Output** | Live preview at http://127.0.0.1:8000/ | Static files in `site/` directory |
| **Deployment Ready** | ❌ No | ✅ Yes |
| **Typical Use Case** | Writing and testing documentation | Preparing for deployment to GitHub Pages |

## When to Use Each Script

### Use launch.bat when:
- You're actively writing or editing documentation in Obsidian
- You need to preview changes in real-time
- You want the development server to auto-reload
- You're testing navigation, styling, or content changes
- You need to see both English and French sites during development

### Use rebuild.bat when:
- You're preparing for deployment to production
- You want a fresh build without any cached files
- You're done editing and need final static files
- You're running CI/CD pipelines
- You need to verify the complete build works

## Development Workflow

1. **Edit documentation** in Obsidian Vault: `C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS\`
2. **Run** `launch.bat` to sync and start development server
3. **Make changes** in Obsidian - they auto-sync and rebuild
4. **Preview** at http://127.0.0.1:8000/ (English) or run `mkdocs serve -f config/fr/mkdocs.yml` for French
5. **Test** navigation, language switching, and content

## Production Deployment

1. Run `rebuild.bat` to generate clean build
2. Verify `site/en/` and `site/fr/` exist and contain complete sites
3. Commit and push to GitHub - GitHub Actions automatically deploys to GitHub Pages
4. Access at:
   - English: https://igoor-noprofit.github.io/docs/
   - French: https://igoor-noprofit.github.io/docs/fr/

## Manual Build Commands

### English Site
```batch
call venv\Scripts\activate
mkdocs build -f config/en/mkdocs.yml
mkdocs serve -f config/en/mkdocs.yml
```

### French Site
```batch
call venv\Scripts\activate
mkdocs build -f config/fr/mkdocs.yml
mkdocs serve -f config/fr/mkdocs.yml
```

## Architecture Notes

### Separate Builds
- Each language builds independently with its own MkDocs configuration
- No `mkdocs-static-i18n` plugin dependency
- Eliminates navigation duplication issues
- French folders can use French names (e.g., "3 - UTILISER IGOOR")

### Shared Assets
- `overrides/` folder contains theme overrides shared by both languages
- Both configs reference same assets via `custom_dir: ../../overrides/`
- Changes to CSS, JavaScript, or images apply to both languages automatically

### Language Switching
- Each config has `extra.alternate` links for language switching
- English site links to `/fr/` for French version
- French site links to `/` for English version

## Troubleshooting

### Server Won't Start
- Check if another mkdocs server is running: `taskkill /F /IM python.exe`
- Try removing `site/` directory and rebuild

### Changes Not Appearing
- Stop the server (Ctrl+C)
- Run `launch.bat` again to force full rebuild
- Check that Obsidian vault path is correct

### French Site Not Loading
- Ensure French site is built: `mkdocs build -f config/fr/mkdocs.yml`
- Serve French site: `mkdocs serve -f config/fr/mkdocs.yml`
- Access at http://127.0.0.1:8000/

### Navigation Shows Duplicates
- This architecture eliminates duplicate navigation issues
- If duplicates appear, verify no files exist in both `docs/en/` and `docs/fr/`

## Resources

- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Icons Search](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search)

## Additional Scripts

### watch_docs.py
Runs in background during development to detect changes from Obsidian and trigger automatic rebuilds. Started automatically by `launch.bat`.

### generate_nav.py & generate_nav_translations.py
Helper scripts for generating navigation structures (if needed for your workflow).
