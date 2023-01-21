universities = [("Union College", 761, "New York"),
                ("Oregon State University", 17, "Oregon"),
                ("University of North Dakota", 23, "North Dakota"),
                ("University of Minnesota", 109, "Minnesota"),
                ("University of Florida", 9, "Florida"),
                ("Oregon State University", 90, "Oregon"),
                ("Union College", 87, "Nebraska"),
                ("Union College", 567, "Kentucky"),
                ]
# Solution 1:
dic = {}
duplicates = set()
for name, id, state in universities:
    if name in dic:
        duplicates.add(name)
    dic[name] = state

# for uni, state in dic.items():
#     print(f'{uni}: {state}')

mapping = {}
for name, id, state in universities:
    if name in duplicates:
        key = f'{name} - {state}'
        mapping[key] = id
    else:
        mapping[name] = id

# for k in mapping:
#     print(k, mapping[k])


# Solution 2 - hashmap inside hashmap:
dic = {}
for uni, id, state in universities:
    if uni not in dic:
        dic[uni] = {}
    dic[uni][state] = id


# for uni, state in mapping.items():
#     print(f'{uni}: {state}')

res = {}
for uni, states in dic.items():
    if len(states) > 1:
        for state, id in states.items():
            key = f'{uni} - {state}'
            res[key] = id
    else:
        for id in states.values():
            res[uni] = id

for uni, state in res.items():
    print(f'{uni}: {state}')

# Hashmap inside hashmap - MS version:
MULTI_STATES = 'multiple states'

mapping = {}
for university, id, state in universities:
    # Let us assign a unique value here saying that this
    # university is in multiple states
    if university in mapping and mapping.get(university) != state:
        mapping[university] = MULTI_STATES
    else:
        mapping[university] = state

institutions = {}
for university, id, state in universities:
    # while looping to the list of universities
    # if the university in multiple states,
    # let's map the university name and the state
    if mapping.get(university) == MULTI_STATES:
        institutions[f'{university} - {state}'] = id
    else:
        institutions[university] = id

for key in institutions:
    print(key, institutions.get(key))
