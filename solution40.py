# Run a structural eligibility milestone check
joining_age = 19

print("Candidate age logged:", joining_age)
if joining_age >= 18 and joining_age <= 25:
    print("Registration Status: Criteria met. Eligible.")
else:
    print("Registration Status: Criteria out of bounds.")
