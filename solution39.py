# Manually swap the position of two elements inside a simple list
items = ["First", "Second"]
print("Before swap operation:", items)

# Use a temporary variable to switch elements safely
temp = items[0]
items[0] = items[1]
items[1] = temp

print("After swap operation:", items)
