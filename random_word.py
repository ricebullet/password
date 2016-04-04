# Random word generator from list

import random

word_file = "1000.txt"
wordlist = open(word_file).read().splitlines()
words = []
for word in wordlist:
    if len(word) > 3:
        words.append(word)

words_copy = list(words)
print ("Press Enter for the next word. 'q' quits.")

while True:
    word = random.choice(words_copy)
    next = raw_input('Word: ' + word + ' ').lower()
    if next == 'q':
        exit(1)
    else:
        words_copy.remove(word)
