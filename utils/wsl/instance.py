import subprocess
import re
import os
import pexpect.popen_spawn
import utils
import utils.printer
import utils.wsl
import utils.wsl.online

def run(command):
    if utils.wsl.online.check():
        return subprocess.check_output(f"wsl exec /bin/bash -c \"{command}\"", text=True, shell=True)
    else: utils.printer.console(f"WSL Instance offline, not running wsl command",2)
def runWithSudoPasswdWrapperNoOutput(command):
    val = os.getenv('VAR1', "")
    if utils.wsl.online.check():
        subprocess.run(f"wsl exec /bin/bash -c \"echo {val} | sudo -S {command}\"", stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        return
    else: utils.printer.console(f"WSL Instance offline, not running wsl command",2)
def getServiceStatus(serviceName):
    x = run(f"sudo service --status-all | grep -i {serviceName}").strip()
    return re.search("\[(.*?)\]", x).group(1).strip() == "+"

def getAllServiceStatus():
    run(f"service --status-all")