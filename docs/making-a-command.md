```
REQUIRE_ADMIN=True // Does The command require elevated permissions to run?


// main() will be what runs the command, if it does not require parametes
// from the arguments

// the main command should not return anything, any input or handling should be done
// in the command

def main(parameters: list) -> None:
COMMAND CODE GOES HERE
COMMAND CODE GOES HERE
COMMAND CODE GOES HERE
COMMAND CODE GOES HERE



// the help method is what is returned PER COMMAND when the help command is run.
//This will be printed to output to show how to use the command

def help() -> None:
    print("Command Help Doc")

```