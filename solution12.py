# Count how many students scored passing marks (33 or above)
student_marks = [25, 45, 89, 12, 56, 78, 30, 92]
passing_count = 0

for mark in student_marks:
    if mark >= 33:
        passing_count = passing_count + 1

print("Total student marks list:", student_marks)
print("Number of students who passed:", passing_count)

