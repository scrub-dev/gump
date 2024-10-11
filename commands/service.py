import argparse
import json
import itertools
import logging
import utils.getFile
import utils.service.enable
import utils.service.disable
import utils.service.process
import utils.printer as printer
import utils.wsl
import utils.wsl.online

REQUIRE_ADMIN = True

#TODO: Add checks to see if a service exists. Maybe just wrap in trys.

def main(parameters) -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("service", type=str, nargs='?')
    parser.add_argument("verb", type=str, nargs='?', choices=["start", "stop", "restart"])
    args = parser.parse_args(parameters)

    if args.service is None:
        print("No Service provided... stopping")
        return
    
    with open(utils.getFile.config("conf.json","service")) as conf:
        conf = json.load(conf)
        DEFAULT_VERB = conf['DEFAULT_VERB'] or "start"
        DEFAULT_ENV = conf['DEFAULT_ENV'] or "win"

    if "," in args.service:
        args.service = args.service.split(",")
    else: args.service = [args.service]

    def getenv(s):
        if ":" in s: 
            _ = s.split(":", 1)
            if _[0] not in ["wsl", "win"]: _[0] = DEFAULT_ENV
            return {"name":_[1], "env":_[0]}
        else: return {"name":s, "env": DEFAULT_ENV}

    def getalias(s, list):
        if s in list:
            return [getenv(e) for e in list[s]]
        else: return [getenv(s)]

    def getconflicts(s, list):
        confLookup = f"{s['env']}:{s['name']}"
        if confLookup in list:
            return [getenv(x) for x in list[confLookup]]
        else: return None

    printer.console(f"Changing services for {','.join(args.service)}")

    with open(utils.getFile.config("aliases.json","service")) as aliases:
        aliases = json.load(aliases)
        args.service = list(itertools.chain.from_iterable(e for e in [getalias(s, aliases) for s in args.service] if e is not None))

    with open(utils.getFile.config("conflicts.json","service")) as conflicts:
        conflicts = json.load(conflicts)
        args.conflicts = list(itertools.chain.from_iterable(e for e in [getconflicts(s, conflicts) for s in args.service] if e is not None))

    def processConflicts(conflicts) -> None:
        res = [utils.service.process.execute(conflict, 'stop') for conflict in conflicts]
        return res

    def processServices(services, verb):
        res = [utils.service.process.execute(service, verb or DEFAULT_VERB) for service in services]
        return res
        
    def process():
        if args.conflicts and (args.verb != 'stop' or args.verb != 'restart'):
             processConflicts(args.conflicts)
        processServices(args.service, args.verb)
        return

    process()

def help() -> None:
    return