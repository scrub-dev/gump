import logging
import os

logger: logging.Logger
REQUIRES_ADMIN = False

def main (parameters: list) -> None:
    print("Hello from helloworld.py")

def help() -> None:
    print("Basic call and response command")