# Check if a word reads the same backwards and forwards
word = "racecar"
reversed_word = word[::-1]

print("Original word:", word)
print("Reversed word:", reversed_word)

if word == reversed_word:
    print("Result: Yes, it is a palindrome!")
else:
    print("Result: No, it is not a palindrome.")
