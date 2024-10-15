import random

def insert_into_sorted_table(table, value):
    for i in range(len(table)):
        if value < table[i]:
            table.insert(i, value)
            break
    else:
        table.append(value)
        
def bubble_sort(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j] > table[j+1]:
                # Swap the elements
                table[j], table[j+1] = table[j+1], table[j]


def create_table(size):
    return [random.randint(0, 100) for _ in range(size)]