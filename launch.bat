@echo off
if exist C:\TMP\IGOOR\docs\docs rmdir /s /q C:\TMP\IGOOR\docs\docs
mkdir C:\TMP\IGOOR\docs\docs
xcopy C:\TMP\IGOOR\OBSIDIAN\IGOOR_VAULT\DOCS C:\TMP\IGOOR\docs\docs /E /I /Y
cd C:\TMP\IGOOR\docs
call venv\Scripts\activate
start "" chrome http://127.0.0.1:8000/
start /B python watch_docs.py
mkdocs serve
