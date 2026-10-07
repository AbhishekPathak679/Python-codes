# Multiply numbers sequentially up to 4 using a basic loop
target = 4
factorial = 1

for i in range(1, target + 1):
    factorial = factorial * i

print("The factorial sequence value for 4 is:", factorial)
