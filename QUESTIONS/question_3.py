#create a program that reads a sentence from the user and stores each word as an element in a list.
#then count the frequency of each word in the list and print the words along with their frequencies.
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1  
    else:
        word_count[word] = 1

print(word_count)