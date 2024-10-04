@echo off
echo.   
echo    ________  ____  _______ 
echo   / ____/ / / /  ^|/  / __ \
echo  / / __/ / / / /^|_/ / /_/ /
echo / /_/ / /_/ / /  / / ____/
echo \____/\____/_/  /_/_/
echo.
echo ~ GUMP Installer
echo ~ Creating Python Virtual Environment
start /B /wait py.exe -m venv %~dp0venv
echo.
@REM start %~dp0venv\Scripts\activate
echo ~ Installing Python Packages
start /B /wait %~dp0venv\Scripts\pip.exe install -r ./requirements.txt
echo.
echo Done... GUMP Command Runner Installed
cmd /k
