import utils.printer as printer
import utils.service.disable
import utils.service.enable
import utils.service.status as SERVICE


def execute(service, verb) -> bool :

    # return await utils.service.status.execute(service)
    state = SERVICE.STATUS(SERVICE.execute(service))

    if state == SERVICE.STATUS.INVALID:
        return
    
    if verb == 'start':
        if state != SERVICE.STATUS.SERVICE_RUNNING:
            printer.console(f"Starting {service['name']} on {service['env']}", 2)
            utils.service.enable.execute(service)
        else: printer.console(f"{service['name']} already running on {service['env']}", 2)

    elif verb == 'stop':
        if state != SERVICE.STATUS.SERVICE_STOPPED:
            printer.console(f"Stopping {service['name']} on {service['env']}", 2)
            utils.service.disable.execute(service)
        else: printer.console(f"{service['name']} already stopped on {service['env']}", 2)
    elif verb == 'restart':
        if state != SERVICE.STATUS.SERVICE_STOPPED:
            printer.console(f"Restarting {service['name']} on {service['env']}", 2)
            utils.service.disable.execute(service)
            utils.service.enable.execute(service)
        else: printer.console(f"Restarting {service['name']} on {service['env']}", 2)

    else:
        printer.console(f"Unrecognised Verb.. How did we get here? {verb}")