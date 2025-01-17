import json
import logging
import argparse
import subprocess
import utils
import utils.printer

logger: logging.Logger

def main (parameters: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("jira_ticket", help="Provide a jira ticket number")
    parser.parse_args(parameters)
    args = parser.parse_args(parameters)

    with open(utils.getFile.config("conf.json", "jira")) as conf:
        conf = json.load(conf)

    subprocess.run(formatOpenCommand(conf['base'], args.jira_ticket), shell=True)

def formatOpenCommand(base:str, jira_ticket:str):
    return f"start {base}{jira_ticket.upper()}"
    

def help () -> None:
    print("Opens websites")