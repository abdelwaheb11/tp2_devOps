def insert_into_sorted_table(table, value):
    for i in range(len(table)):
        if value < table[i]:
            table.insert(i, value)
            break
    else:
        table.append(value)