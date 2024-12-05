import subprocess
import utils.wsl
import utils.wsl.instance


def listDirectories(a) -> list:
    return [x for x in utils.wsl.instance.run(f"ls {a['location']}").split("\n") if x != '']

def listDirectoryContents(a) -> list:
    return [x for x in utils.wsl.instance.run(f"cd {a} && ls").split("\n") if x != '']

def doesBinExist(a) -> str:
    try:
        return utils.wsl.instance.run(f"which {a}") != ""
    except:
        return False
    
def runShellCommand(a):
    subprocess.call(a, shell=True)

def runPrivShellCommand(a, b):
    runShellCommand(f"wsl -- /bin/bash -c \"echo {b} | sudo -S true; bashtop\"")
def runPrivShellCommand(a):
    runPrivShellCommand(a, )
