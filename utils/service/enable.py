import win32serviceutil
import utils
import utils.service
import utils.wsl
import utils.wsl.instance
import utils.wsl.online

def execute(service) -> bool :
    if service['env'] == 'win':
        win32serviceutil.StartService(service['name'])
    elif service['env'] == 'wsl':
        if utils.wsl.online.check(): utils.wsl.instance.runWithInput(f"sudo systemctl start {service['name']}", "")
        else: utils.printer.console(f"WSL Instance not running... ignoring {service['name']}")
        return
    return True