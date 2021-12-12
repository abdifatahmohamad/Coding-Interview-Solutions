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

# --------------------------------------------------------------
# JavaScript:

# function customSort(tables, criteria){
#   let sorted_table = [];
#   for(let table of tables){
#     sorted_table.push(table[criteria]);
#   }

#   const s_tables = sorted_table.sort((a, b) => b - a);

#   // let res = [];
#   // for(let i of s_tables){
#   //   res.push(i);
#   // }
#   // console.log(res.join(", "))

#   // Same as above code:
#   for(let i of s_tables){
#     process.stdout.write(i + ", ");
#   }

# }

# let t = [{key: 9}, {key: 26}, {key: 13}, {key: 63}, {key: 19}, {key: 70}];
# let c = 'key';

# customSort(t, c)
