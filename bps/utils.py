import random

def read(file):
    with open(file) as f:
        return f.read()

HUMAN_FRIENDLY_CHARS = '234679ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
def random_string(length):
    return ''.join(random.choice(HUMAN_FRIENDLY_CHARS) for x in range(length))
