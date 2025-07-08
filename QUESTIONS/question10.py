#10. Write a Python function that accepts a sentence and returns a set of all unique vowels
#used.
sentence = input("Enter a sentence with space: ")
vowels = "aeiouAEIOU"
used_vowels = set()
for char in sentence:
    if char in vowels:
        used_vowels.add(char.lower())  
print("Unique vowels used:", used_vowels)


    
    