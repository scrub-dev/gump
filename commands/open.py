import logging
import argparse

logger: logging.Logger

def main (parameters: list) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("main", help="Provide a preset, url or site name")
    parser.add_argument("-t", "--type", help="Type of site (core/magento/etc) Not needed if providing a preset or url", required=False)
    parser.add_argument("-b", "--browser", help="Open a specific browser or enter 'all' to open all browsers", required=False)
    parser.add_argument("-n", "--name", help="Require a specific basename for site name, use", required=False)

    parser.parse_args(parameters)

    # create a toOpen array

    # Look for preset
        # do the preset stuff
        # similar to check if sitename ngl

    # Check if url
        # add url to toOpen array

    # Check if sitename
        # check if type set, if not use default
        # check if name set, if not use default
        # get type structure and populate with values
        # get type endpoints
        # add type_structure + type_endpoints, per endpoint to toOpen array

    # Check if browser set
        #if all, run open with all browsers
        #if set, open with set browser
        #if not set, open with default browser

def help() -> None:
    print("Open Command!")