import json
import subprocess
import re
import utils
def getWSLInstances():
    x = str(subprocess.check_output(["wsl", "-l", "-v"], text=True, shell=True)).split("\n")
    y = [_ for _ in [re.sub('[^0-9a-zA-Z -]+', '', y) for y in x] if _][1::]
    z = [re.sub(' +', ' ', _).strip().split(" ")[:-1] for _ in y]
    return [{"name": wslInstance[0], "status": True if wslInstance[1] == "Running" else False } for wslInstance in z]

def check() -> bool:
    with open(utils.getFile.config("conf.json","wsl")) as conf:
        conf = json.load(conf)
        MAIN_INSTANCE = conf['MAIN_INSTANCE']
    return next((x for x in getWSLInstances() if x['name'] == MAIN_INSTANCE), None)['status']