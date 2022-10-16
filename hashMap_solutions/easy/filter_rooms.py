from collections import defaultdict


def treasure_rooms(treasure_rooms, instructions):
    mapping = defaultdict(list)
    actual_treasure_rooms = set()
    for src, des in instructions:
        if src != des:
            mapping[src].append(des)
            mapping[des].append(src)
        if src == des:
            actual_treasure_rooms.add(src)

    # {'tulip': ['jasmin', 'lily'], 'rose': ['violet'], 'violet': ['sunflower', 'daisy', 'iris']}
    # rooms = ['tulip', 'violet]
    # treasure_rooms = ["lily", "tulip", "violet", "rose"]
    # actual_treasure_rooms = ["tulip", "rose"]
    rooms = []
    for des in mapping:
        if len(mapping[des]) >= 2:
            rooms.append(des)

    result = []
    for room in rooms:
        if room in actual_treasure_rooms and room in treasure_rooms:
            result.append(room)
        else:
            for r in mapping[room]:
                if r in actual_treasure_rooms and room in mapping[r] and r in treasure_rooms:
                    result.append(room)
    return result


instructions_1 = [
    ["jasmin", "tulip"],
    ["lily", "tulip"],
    ["tulip", "tulip"],
    ["rose", "rose"],
    ["violet", "rose"],
    ["sunflower", "violet"],
    ["daisy", "violet"],
    ["iris", "violet"]
]

treasure_rooms_1 = ["lily", "tulip", "violet", "rose"]
treasure_rooms_2 = ["lily", "jasmin", "violet"]
treasure_rooms_3 = ["violet"]


instructions_2 = [
    ["jasmin", "tulip"],
    ["lily", "tulip"],
    ["tulip", "violet"],
    ["violet", "violet"]
]

print(treasure_rooms(treasure_rooms_1, instructions_1))
print(treasure_rooms(treasure_rooms_2, instructions_1))
print(treasure_rooms(treasure_rooms_3, instructions_2))

'''
filter_rooms(treasure_rooms_1, instructions_1) => ["tulip", "violet"]
* tulip can be accessed from rooms lily and jasmin. Tulip's instruction leads to a treasure room (tulip itself)
* violet can be accessed from daisy, iris. Violet's instruction leads to a treasure room (rose)

filter_rooms(treasure_rooms_2, instructions_1) => []
* none of the rooms reachable from tulip or violet are treasure rooms

filter_rooms(treasure_rooms_3, instructions_2) => [tulip]
* tulip can be accessed from rooms lily and jasmin. Tulip's instruction leads to a treasure room (violet)
'''
