students = [
    {"name":"osama","animal":"horse","grade":"18"},
    {"name":"hamza","animal":"red panda","grade":"60"},
    {"name":"ahmed","animal":None,"grade":"100"}
]

for student in students:
    print(student["name"], student["animal"], student["grade"], sep=",")

