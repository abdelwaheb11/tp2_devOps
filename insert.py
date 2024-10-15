def insert_into_sorted_table(table, value):
    # Find the correct position to insert
    for i in range(len(table)):
        if value < table[i]:
            table.insert(i, value)
            break
    else:
        table.append(value)  # If value is greater than all elements