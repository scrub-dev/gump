import pyuac.admin
import win32serviceutil
import pyuac
def main(parameters) -> None:

    # Needs to be admin
    if not pyuac.admin.isUserAdmin():
        pyuac.admin.runAsAdmin()
        return

def help() -> None:
    return