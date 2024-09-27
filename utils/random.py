import random

def generate(lower = 0, upper = 1) -> int:
    return random.randint(lower, upper)


def array (array) -> str:
    arrlen = len(array)
    return array[generate(0, arrlen - 1)]