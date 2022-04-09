# https://edabit.com/challenge/XPnTdP9eDkwqAQeWq
'''
You have two lists. One shows the names of the people names,
while the other shows their occupation jobs.
Your task is to create a dictionary
displaying each person to their respective occupation.

Person	Job
Annie	Teacher
Steven	Engineer
Lisa	Doctor
Osman	Cashier

'''


def assign_person_to_job(names, jobs):
    mapping = {}
    for name, job in zip(names, jobs):
        mapping[name] = job
    return mapping

    # Short version
    # return dict(zip(names, jobs))


# Without using zip
def assign_person_to_job(names, jobs):
    mapping = {}
    i, j = 0, 0
    while i < len(names) or j < len(jobs):
        mapping[names[i]] = jobs[j]
        i += 1
        j += 1
    return mapping


# Soultion 3:
def assign_person_to_job(names, jobs):
    mapping = {}
    for i, name in enumerate(names):
        mapping[name] = jobs[i]
    return mapping


names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

# names = ["Annie", "Steven", "Lisa", "Osman"]
# jobs = ["Teacher", "Engineer", "Doctor", "Cashier"]

print(assign_person_to_job(names, jobs))

'''
Output: {
  "Dennis": "Butcher",
  "Vera": "Programmer",
  "Mabel": "Doctor",
  "Annette": "Teacher",
  "Sussan": "Lecturer"
}
'''
