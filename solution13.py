# Track down the highest number in a collection without using max()
numbers = [14, 52, 87, 36, 99, 41, 63]
largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print("Numbers list:", numbers)
print("The largest number found is:", largest_number)

