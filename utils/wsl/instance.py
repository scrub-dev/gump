import subprocess
import re
import utils
import utils.printer
import utils.wsl
import utils.wsl.online

def run(command):
    if utils.wsl.online.check():
        return subprocess.check_output(f"wsl exec /bin/bash -c \"{command}\"", text=True, shell=True)
    else: utils.printer.console(f"WSL Instance offline, not running wsl command",2)

def getServiceStatus(serviceName):
    x = run(f"service --status-all | grep -i {serviceName}").strip()
    return re.search("\[(.*?)\]", x).group(1).strip() == "+"

def getAllServiceStatus():
    run(f"service --status-all")