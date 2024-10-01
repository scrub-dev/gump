import win32serviceutil
import utils

def execute(service) -> bool :
    if service['env'] == 'win':
        win32serviceutil.StartService(service['name'])
    elif service['env'] == 'wsl':
        if utils.wsl.online.check(): utils.wsl.instance.run(f"sudo systemctl start {service['name']}")
        else: utils.printer.console(f"WSL Instance not running... ignoring {service['name']}")
        return
    return True