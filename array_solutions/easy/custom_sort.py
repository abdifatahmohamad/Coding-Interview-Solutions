def custom_sort(tables, criteria):
    sorted_table = []

    for table in tables:
        sorted_table.append(table[criteria])

    sorted_table.sort(reverse=True)

    for i in sorted_table:
        print(i, end=", ")

    # tables = sorted(tables, key=lambda table: table[criteria], reverse=True)
    # print(tables)


t = [{'key': 9}, {'key': 26}, {'key': 13},
     {'key': 63}, {'key': 19}, {'key': 70}]
c = 'key'

custom_sort(t, c)
