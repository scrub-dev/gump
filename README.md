# Gump | Python Based Modular Command Runner

GUMP is a module python-based command runner where commands in the /commands directory can be ran via command-line on windows. Made to automate repetitive tasks, this command runner is incredibly versitile in what it can offer. Including elevated-permission commands (be careful).
## Usage
Never install and run a command you don't trust, check first to see if it does what is advertised.

Add the gump folder to your path to use anywhere:

```
gump [command] [variables]
```
or
```
[path/to/gump.cmd] [command] [variables]
```

## Installation

Run `install.bat` in the root directory, this will create a virtual environment.\
If your python path variable is different to `py`, change it to `python` in the `install.bat` file. This is only needed to initially get the venv setup.

## Structure
### /commands
Create custom commands here!\
Create commands in this directory under the naming scheme of [commandname].py
this [commandname] will be what you run when running the gump command runner to run this file.

### /utils
Utils contains a list of general modules with commands that assist with creating your own commands. Subdirectories in this folder house more command or system specific modules. Such as managing services or interacting with WSL

### /configs
General config json files are stored in the root directory. Configs specific to commands or utility modules are stored in a clearly name subdirectory.


## Creating your own commands
[Default commandfile structure](docs/making-a-command.md)

## Issues
Pywin32 might need its postinstall script ran, this is found in `venv/Scripts/pywin32_postinstall.py`



## Todo

- [ ] Error Checking
- [ ] Handling when opened without command
