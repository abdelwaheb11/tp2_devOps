def bubble_sort(table):
    n = len(table)
    for i in range(n):
        for j in range(0, n-i-1):
            if table[j] > table[j+1]:
                # Swap the elements
                table[j], table[j+1] = table[j+1], table[j]