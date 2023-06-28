word = input("Please enter a word:  ")
vowel_count = 0

for i in range(len(word)):
    if word[i] in 'aeiouAEIOU':
        vowel_count += 1
        
print(f"Number of vowels in the word {word}: ", vowel_count)