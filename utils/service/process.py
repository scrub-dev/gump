import utils.printer as printer
import utils.service.disable
import utils.service.enable


async def execute(service, verb) -> bool :
    if verb == 'start':
        printer.console(f"Starting {service['name']} on {service['env']}", 2)
        await utils.service.enable.execute(service)
    elif verb == 'stop':
        printer.console(f"Stopping {service['name']} on {service['env']}", 2)
        await utils.service.disable.execute(service)
    elif verb == 'restart':
        printer.console(f"Restarting {service['name']} on {service['env']}", 2)
        await utils.service.disable.execute(service)
        await utils.service.enable.execute(service)
    else:
        printer.console("Unrecognised Verb.. How did we get here?")