student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades ={}

# Changing student's grade list to string values
for name in student_scores:
    if student_scores[name] in range (91,101):
        student_grades[name] = 'Outstanding'
    if student_scores[name] in range (81,91):
        student_grades[name] = 'Exceeds Expectations'
    if student_scores[name] in range(71, 81):
        student_grades[name] = 'Acceptable'
    if student_scores[name] in range(0, 71):
        student_grades[name] = 'Fail'

print(student_grades)






#print(student_scores)