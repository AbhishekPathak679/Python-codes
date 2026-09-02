# Manually search through a list to see if an item exists
enrolled_courses = ["Data Structures", "Web Dev", "Python Basics", "Cyber Security"]
search_target = "Python Basics"
item_found = False

for course in enrolled_courses:
    if course == search_target:
        item_found = True

print("Course Search Target:", search_target)
if item_found == True:
    print("Status: Student is verified and enrolled in this class.")
else:
    print("Status: Course registration not found.")

