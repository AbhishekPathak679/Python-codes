# Verify that a user input field is not completely empty
user_input = "   "
clean_input = user_input.strip()

if len(clean_input) == 0:
    print("Validation Result: Warning, field cannot be blank!")
else:
    print("Validation Result: Data accepted successfully.")
