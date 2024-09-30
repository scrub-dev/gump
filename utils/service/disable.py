import asyncio
import win32serviceutil

def execute(service) -> bool :
    if service['env'] == 'win':
        win32serviceutil.StopService(service['name'])
    elif service['env'] == 'wsl':
        return
    return True