@echo off
SETLOCAL
set VAR1=Core!
%~dp0venv\Scripts\Python.exe %~dp0\gump.py %*
ENDLOCAL