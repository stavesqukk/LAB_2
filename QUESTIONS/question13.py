#13. Write a program that reads a text and counts the frequency of each character (excluding
#spaces and special characters) using a dictionary.

sent = input("Enter a sentence: ")
sent = sent.strip().lower()
char_count = {}

for ch in sent:
    if ch.isalpha():  # Only count alphabetic characters
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

print("Character frequencies (excluding spaces and special characters):")
print(char_count)
