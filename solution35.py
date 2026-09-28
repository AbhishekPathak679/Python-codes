# Check if a custom username fits within standard character limits
input_username = "AbhishekPathak679"

print("Checking username:", input_username)
if len(input_username) <= 20:
    print("Validation Result: Username length is acceptable.")
else:
    print("Validation Result: Username exceeds character limit.")
