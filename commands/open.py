import json
import logging
import argparse
import subprocess
import utils

logger: logging.Logger

def main (parameters: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("main", help="Provide a preset, url or site name")
    parser.add_argument("-b", "--browser", help="Open a specific browser or enter 'all' to open all browsers", required=False)
    parser.parse_args(parameters)
    args = parser.parse_args(parameters)

    with open(utils.getFile.config("conf.json", "open")) as conf:
        conf = json.load(conf)
    
    browser_exe = \
            next((x for x in conf["browsers"] if x['name'] == args.browser), None) \
            if args.browser and args.browser in [x['name'] for x in conf['browsers']] \
            else next(x for x in conf["browsers"] if x['name'] == conf['default_browser'])
    
    with open(utils.getFile.config("presets.json", "open")) as presets:
        presets = json.load(presets)
    websites_to_open = ([f for f in presets['presets'] if f['name'] == args.main])[0]['urls'] if args.main in [x['name'] for x in presets['presets']] else [args.main]

    subprocess.run(formatOpenCommand(browser=browser_exe['exe_location'], websites=websites_to_open), shell=True)

def formatOpenCommand(browser, websites):
    return f"start {browser} {' '.join(websites)}"
    

def help () -> None:
    print("Opens websites")