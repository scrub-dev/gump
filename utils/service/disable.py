import win32serviceutil
import utils
import utils.printer
import utils.wsl
import utils.wsl.instance
import utils.wsl.online

def execute(service) -> bool :
    if service['env'] == 'win':
        win32serviceutil.StopService(service['name'])
    elif service['env'] == 'wsl':
        if utils.wsl.online.check(): utils.wsl.instance.runWithSudoPasswdWrapperNoOutput(f"systemctl stop {service['name']}")
        else: utils.printer.console(f"WSL Instance not running... ignoring {service['name']}")
    return True