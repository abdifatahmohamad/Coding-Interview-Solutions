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

'''
Output: {
'Annie': 'Teacher', 
'Steven': 'Engineer', 
'Lisa': 'Doctor', 
'Osman': 'Cashier'}
'''
