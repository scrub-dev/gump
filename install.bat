@echo off
echo GUMP INSTALLER...

start /B /wait py.exe -m venv %~dp0venv
@REM start %~dp0venv\Scripts\activate
start %~dp0venv\Scripts\pip.exe install -r ./requirements.txt
cmd /k
