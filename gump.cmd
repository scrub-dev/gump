@echo off
SETLOCAL
set VAR1=Core!
%~dp0venv\Scripts\Python.exe gump.py %*
ENDLOCAL