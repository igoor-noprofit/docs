# IGOOR DOCUMENTATION - AGENTS GUIDE

## OVERVIEW

This documentation site uses a **separate builds architecture** for multi-language support (English and French). Each language has its own MkDocs configuration and build process.

## ARCHITECTURE

```
docs/
├─ config/
│  ├─ en/
│  │  └─ mkdocs.yml          # English site config
│  └─ fr/
│     └─ mkdocs.yml          # French site config
├─ docs/
│  ├─ en/                   # English content (folders kept in English)
│  └─ fr/                   # French content (folders in French)
├─ overrides/
│  ├─ assets/               # Shared assets (logo, favicon, CSS)
│  └─ partials/
│     └─ header.html         # Language-specific announcements
├─ site/                     # Build output
│  ├─ en/                   # English site
│  └─ fr/                   # French site
└─ mkdocs.yml                # Legacy config (not used for builds)
```

## KEY CONCEPTS

### Separate Builds
- Each language builds independently with its own config
- No `mkdocs-static-i18n` plugin dependency
- Eliminates navigation duplication issues
- French folder names can stay in French (e.g., "3 - UTILISER IGOOR")

### Shared Assets
- `overrides/` folder contains shared theme overrides
- `overrides/assets/` contains logo, favicon, and CSS
- Both languages reference the same shared assets via `custom_dir: ../../overrides/`

### Language Switching
- Each config has `extra.alternate` links
- English site links to `/fr/` for French
- French site links to `/` for English

## BUILD PROCEDURES

### 1. Copy Documentation from Obsidian

Documentation is stored in Obsidian vault and copied before building:

```batch
# This is done automatically in launch.bat/rebuild.bat
xcopy C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS C:\TMP\IGOOR\docs\docs /E /I /Y
```

**Folder Structure After Copy:**
- `docs/en/` - English content (folders: "1 - INSTALLATION", etc.)
- `docs/fr/` - French content (folders: "3 - UTILISER IGOOR", etc.)

### 2. Build English Documentation

```batch
cd C:\TMP\IGOOR\docs
call venv\Scripts\activate
mkdocs build -f config/en/mkdocs.yml
```

**Output:** `site/en/`

**Configuration:** `config/en/mkdocs.yml`
- `docs_dir: ../../docs/en`
- `site_dir: ../../site/en`
- `language: en`

### 3. Build French Documentation

```batch
cd C:\TMP\IGOOR\docs
call venv\Scripts\activate
mkdocs build -f config/fr/mkdocs.yml
```

**Output:** `site/fr/`

**Configuration:** `config/fr/mkdocs.yml`
- `docs_dir: ../../docs/fr`
- `site_dir: ../../site/fr`
- `language: fr`

## DEVELOPMENT WORKFLOW

### Launch Full Development Server (Both Languages)

```batch
launch.bat
```

**What it does:**
1. Copies docs from Obsidian vault
2. Builds English documentation
3. Builds French documentation
4. Starts `mkdocs serve` for English on http://127.0.0.1:8000/

**Testing French locally:**
```batch
mkdocs serve -f config/fr/mkdocs.yml
# Serves on http://127.0.0.1:8000/
```

### Watch Mode (Auto-rebuild)

The `watch_docs.py` script runs in background to detect changes from Obsidian and trigger rebuilds.

## PRODUCTION BUILD

### Build All Languages

```batch
rebuild.bat
```

**What it does:**
1. Removes existing `site/` directory
2. Builds English documentation to `site/en/`
3. Builds French documentation to `site/fr/`
4. Shows completion status

**Output Structure:**
```
site/
├─ en/
│  ├─ index.html
│  ├─ 1 - INSTALLATION/
│  ├─ 2 - CONFIGURATION/
│  └─ ...
└─ fr/
   ├─ index.html
   ├─ 1 - INSTALLATION/
   ├─ 2 - CONFIGURATION/
   └─ ...
```

## TESTING PROCEDURES

### 1. Local Testing

**English Site:**
```batch
# Option 1: Use launch.bat
launch.bat

# Option 2: Direct build
mkdocs build -f config/en/mkdocs.yml
mkdocs serve -f config/en/mkdocs.yml
```
- Navigate to: http://127.0.0.1:8000/
- Test navigation (should show English folders)
- Test language switcher (should link to `/fr/`)

**French Site:**
```batch
mkdocs build -f config/fr/mkdocs.yml
mkdocs serve -f config/fr/mkdocs.yml
```
- Navigate to: http://127.0.0.1:8000/
- Test navigation (should show French folders like "3 - UTILISER IGOOR")
- Test language switcher (should link to `/`)
- Verify **NO duplicate navigation entries**

### 2. Navigation Verification

**Expected English Navigation:**
```
- Home (index)
- 1 - INSTALLATION
- 2 - CONFIGURATION
- 3 - USING IGOOR
- 4 - VOICE SYNTHESIS
- 5 - VOICE RECOGNITION
- 6 - MEMORY
- 7 - INTEGRATION WITH DEVICES
- 9 - FAQ AND RESOLUTION OF COMMON PROBLEMS
```

**Expected French Navigation:**
```
- Accueil (index)
- 1 - INSTALLATION
- 2 - CONFIGURATION
- 3 - UTILISER IGOOR
- 4 - VOIX DE SYNTHESE
- 5 - RECONNAISSANCE VOCALE
- 6 - MEMOIRE
- 7 - INTEGRATION AVEC DISPOSITIFS
- 9 - FAQ ET RESOLUTION DES PROBLEMES COMMUNS
```

**Verify:**
- ✅ Each section appears only ONCE
- ✅ No duplicate folder names
- ✅ Links work correctly
- ✅ Language switcher works

### 3. Playwright Testing (For AI Agents)

```python
# Navigate to English site
await page.goto('http://127.0.0.1:8000/')
# Check navigation elements
navigation = await page.query_selector_all('nav .md-nav__list')
# Verify single entries per section

# Navigate to French site
await page.goto('http://127.0.0.1:8000/fr/')
# Check navigation elements
navigation = await page.query_selector_all('nav .md-nav__list')
# Verify single entries per section (should use French folder names)
```

## DEPLOYMENT

### GitHub Actions Workflow

**File:** `.github/workflows/deploy.yml`

**Trigger:** Push to `main` branch or manual workflow dispatch

**Process:**
1. Checks out code
2. Sets up Python 3.13
3. Installs dependencies from `requirements.txt`
4. Builds English: `mkdocs build -f config/en/mkdocs.yml`
5. Builds French: `mkdocs build -f config/fr/mkdocs.yml`
6. Creates `.nojekyll` file
7. Uploads `site/` directory as artifact
8. Deploys to GitHub Pages

**Deployment URL:**
- English: https://igoor-noprofit.github.io/docs/
- French: https://igoor-noprofit.github.io/docs/fr/

## COMMON TASKS

### Update Documentation Content

1. Edit files in Obsidian Vault: `OBSIDIAN/IGOOR_VAULT/DOCS/`
2. Run `launch.bat` to copy and rebuild
3. Changes auto-reflect on http://127.0.0.1:8000/

### Modify Site Configuration

**English Site:** Edit `config/en/mkdocs.yml`
**French Site:** Edit `config/fr/mkdocs.yml`
**Shared Theme:** Edit files in `overrides/` directory

### Change Theme Styles

Edit: `overrides/assets/stylesheets/extra.css`

Changes apply to both languages automatically.

### Update Navigation Labels

Edit the `nav` section in:
- `config/en/mkdocs.yml` (English labels)
- `config/fr/mkdocs.yml` (French labels)

### Add Shared JavaScript/CSS

Place files in `overrides/` and reference them in both configs:
```yaml
# In both config/en/mkdocs.yml and config/fr/mkdocs.yml
extra_javascript:
  - overrides/js/custom.js

extra_css:
  - overrides/css/custom.css
```

## RESOURCES

### Icons Search
https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search

### MkDocs Material Documentation
https://squidfunk.github.io/mkdocs-material/

### MkDocs Documentation
https://www.mkdocs.org/

## TROUBLESHOOTING

### Build Fails

**Error:** "cannot find docs directory"
- **Solution:** Ensure `docs/en/` and `docs/fr/` exist after running `launch.bat`

**Error:** "missing nav configuration"
- **Solution:** Both configs must have valid `nav:` section

### Navigation Shows Duplicates

**Symptom:** Same folder appears twice in navigation
- **Root Cause:** Using old `mkdocs-static-i18n` plugin with folder structure mismatch
- **Solution:** This architecture eliminates the issue. If duplicates persist, verify:
  1. No files in both `docs/en/` and `docs/fr/` with same name
  2. Each language builds independently

### Language Switcher Not Working

**Symptom:** Clicking language button shows 404
- **Solution:** Verify `site_url` in configs matches deployment structure:
  - English: `site_url: https://igoor-noprofit.github.io/docs/`
  - French: `site_url: https://igoor-noprofit.github.io/docs/fr/`

### Assets Not Loading

**Symptom:** Logo, favicon, or CSS missing
- **Solution:** Ensure assets are in `overrides/assets/` and referenced correctly in both configs:
  ```yaml
  logo: assets/images/logo.svg
  favicon: assets/images/favicon.ico
  extra_css:
    - assets/stylesheets/extra.css
  ```

### TOC (Table of Contents) Not Visible

**Symptom:** "Table des matières" section is empty or missing
- **Root Cause:** `site_url` configuration causes incorrect base paths in generated HTML
- **Solution:** Remove `site_url` from config files
  - For local development: Don't set `site_url` (let MkDocs auto-detect)
  - For production: Use same `site_url` for both languages or set per environment

**Incorrect Configuration:**
```yaml
# ❌ This causes TOC issues and incorrect asset paths
site_url: https://igoor-noprofit.github.io/docs/fr/
```

**Correct Configuration:**
```yaml
# ✅ Correct for both local and production
docs_dir: ../../docs/fr
site_dir: ../../site/fr
# site_url: auto-determined by MkDocs
```

**Note:** The `site_url` should only be set if you know what you're doing. For separate builds architecture, it's better to let MkDocs auto-detect URLs.

## FILES REFERENCE

### Configuration Files
- `config/en/mkdocs.yml` - English site configuration (ACTIVE)
- `config/fr/mkdocs.yml` - French site configuration (ACTIVE)
- `mkdocs.yml` - Legacy configuration (DEPRECATED, kept for reference)

### Build Scripts
- `launch.bat` - Development server (copies docs + builds both + serves English)
- `rebuild.bat` - Production build (builds both languages)
- `watch_docs.py` - Auto-rebuild script for Obsidian sync

### Deployment
- `.github/workflows/deploy.yml` - GitHub Actions CI/CD

### Content
- `docs/en/` - English documentation content
- `docs/fr/` - French documentation content
- `overrides/` - Shared theme overrides and assets

## AGENT TESTING QUICK START

For AI agents or automated testing:

```batch
# 1. Clean build
rmdir /s /q site

# 2. Build English
mkdocs build -f config/en/mkdocs.yml

# 3. Build French
mkdocs build -f config/fr/mkdocs.yml

# 4. Serve English
mkdocs serve -f config/en/mkdocs.yml

# Now test at http://127.0.0.1:8000/
```

For French testing, use `mkdocs serve -f config/fr/mkdocs.yml` instead.