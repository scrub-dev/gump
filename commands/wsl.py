import argparse
import json
import subprocess
import utils
import utils.getFile
import utils.printer
import utils.wsl
import utils.wsl.instance
import utils.wsl.utils

def main (parameters: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str)
    parser.add_argument("command_str", type=str, nargs=argparse.REMAINDER)
    args = parser.parse_args(parameters)

    match args.command.lower():
        case "proc":
            view_processes(args.command_str)
        case _:
            invalid_command()
    return

def help() -> None:
    print("Basic call and response command")

def invalid_command():
    utils.printer.console("No WSL Subcommand found! Exiting...")

def view_processes(params):
    parser = argparse.ArgumentParser()
    parser.add_argument("chosenProcViewer", nargs='?')
    parser.add_argument("-s","--sudo", action=argparse.BooleanOptionalAction ,default=False, type=bool)
    args = parser.parse_args(params)

    with open(utils.getFile.config("conf.json", "wsl")) as conf:
        conf = json.load(conf)

    chosenProcViewer = None if args.chosenProcViewer == None else args.chosenProcViewer

    if(chosenProcViewer == None):
        for process_viewer in conf['PROCESS_VIEWER_LIST']:
            if(utils.wsl.utils.doesBinExist(process_viewer)):
                args.chosenProcViewer = process_viewer
                break
    if(args.sudo):
        utils.wsl.instance.runPrivCommand(args.chosenProcViewer)
    else:    
        utils.wsl.instance.runCommand(args.chosenProcViewer)
