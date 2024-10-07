```
#IMPORTS GO HERE

REQUIRE_ADMIN=TRUE || FALSE
logger: logging.Logger

def main(parameters: list) -> None:

def help() -> None:
    print("Command Help Doc")

```


## Logging
A logger object is injected into the command using a setattr in the module loader.
To utilise it in the command, at the top of the file add:
```
logger: logging.Logger
```
The boilerplate example above includes this addition.
The Logger will still be available if this is not included but will warn you about not the logger not being referenced!

