from enum import Enum
import win32serviceutil
import utils
import utils.wsl
import utils.wsl.instance

class STATUS(Enum):
    SERVICE_STOPPED = 1
    SERVICE_STOP_PENDING = 3
    SERVICE_START_PENDING = 2
    SERVICE_RUNNING = 4
    INVALID = 0
    SERVICE_PAUSED = 7

    def text(input) -> str:
        if input == 1: return "Stopped"
        elif input == 2: return "Pending Start"
        elif input == 3: return "Pending Stop"
        elif input == 4: return "Stopped"
        elif input == 0: return "Invalid"
        elif input == 7: return "Paused"

def execute(service) -> bool :
    if service['env'] == 'win':
        (serviceType, currentState, controlsAccepted, exitCode, serviceSpecificExitCode, checkPoint, waitHint) = win32serviceutil.QueryServiceStatus(service['name'])
    elif service['env'] == 'wsl':
        currentState = 4 if utils.wsl.instance.getServiceStatus(service['name']) else 1
    return currentState