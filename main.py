import random

def create_table(size):
    return [random.randint(0, 100) for _ in range(size)]