import argparse
import json
import pyuac.admin
import pyuac
import itertools

DEFAULT_SERVICE_ENV = "win"
DEFAULT_SERVUCE_VERB = "start"

def main(parameters) -> None:

    # Needs to be admin
    if not pyuac.admin.isUserAdmin():
        pyuac.admin.runAsAdmin()

    parser = argparse.ArgumentParser()
    parser.add_argument("service", type=str, nargs='?')
    parser.add_argument("verb", type=str, nargs='?', choices=["start", "stop", "restart"])
    args = parser.parse_args(parameters)

    if args.service is None:
        print("No Service provided... stopping")
        return

    if "," in args.service:
        args.service = args.service.split(",")
    else: args.service = [args.service]

    def getenv(s):
        if ":" in s: 
            _ = s.split(":", 1)
            if _[0] not in ["wsl", "win"]: _[0] = DEFAULT_SERVICE_ENV
            return {"name":_[1], "env":_[0]}
        else: return {"name":s, "env":DEFAULT_SERVICE_ENV}

    def getalias(s, list):
        if s['name'] in list:
            return [getenv(e) for e in list[s['name']]]
        else: return [s]

    def getconflicts(s, list):
        confLookup = f"{s['env']}:{s['name']}"
        if confLookup in list:
            return [getenv(x) for x in list[confLookup]]
        else: return None


    args.service = [getenv(s) for s in args.service]

    with open("./configs/service/aliases.json") as aliases:
        aliases = json.load(aliases)
        args.service = list(itertools.chain.from_iterable(e for e in [getalias(s, aliases) for s in args.service] if e is not None))

    with open("./configs/service/conflicts.json") as conflicts:
        conflicts = json.load(conflicts)
        args.conflicts = list(itertools.chain.from_iterable(e for e in [getconflicts(s, conflicts) for s in args.service] if e is not None))

    print(f"TO ENABLE: {args.service}")
    print(f"TO DISABLE: {args.conflicts}")

    #disabled all conflicting service(s)
    #enabled all required service(s)
def help() -> None:
    return