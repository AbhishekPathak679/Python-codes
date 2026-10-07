# Count how many standard vowels appear inside a target word
word = "university"
vowels = "aeiou"
vowel_count = 0

for letter in word:
    if letter in vowels:
        vowel_count = vowel_count + 1

print("Target word:", word)
print("Total number of vowels found:", vowel_count)
