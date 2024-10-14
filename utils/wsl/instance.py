import subprocess
import re
import os
import utils
import utils.printer
import utils.wsl
import utils.wsl.online

def run(command):
    if utils.wsl.online.check():
        return subprocess.check_output(f"wsl exec /bin/bash -c \"{command}\"", text=True, shell=True)
    else: utils.printer.console(f"WSL Instance offline, not running wsl command",2)
def runWithSudoPasswdWrapperNoOutput(command):
    val = os.getenv('VAR1', "Core!")
    if utils.wsl.online.check():
        return subprocess.check_output(f"wsl exec /bin/bash -c \"echo {val} | sudo -S {command}\"", stderr = subprocess.DEVNULL)
    else: utils.printer.console(f"WSL Instance offline, not running wsl command",2)
def getServiceStatus(serviceName):
    x = run(f"sudo service --status-all | grep -i {serviceName}").strip()
    return re.search("\[(.*?)\]", x).group(1).strip() == "+"

def getAllServiceStatus():
    run(f"service --status-all")


# TODO CHECK AND VERIFY THIS WORKS
def getCommandRoute(binName):
    x = run(f"whereis {binName}")
    print(x)
    return x

def isCommandAvailable(binName):
    return