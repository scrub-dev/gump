import random
generate = lambda l=0, u=1: random.randint(l, u)
array = lambda a : a[generate(0, len(a) - 1)]