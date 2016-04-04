from PyDictionary import PyDictionary
import time
import random
import os

# To download the PyDictionary module go to
# https://pypi.python.org/pypi/PyDictionary/1.5.2

lookup = PyDictionary()
word_file = "1000.txt"
wordlist = open(word_file).read().splitlines()
words = []
for word in wordlist:
    if len(word) > 3:
        words.append(word)

words_copy = words[:]

wins, attempts = 0, 0

def restart():
    choice = raw_input('Play again: Y or N? ').lower()
    if choice[0] == 'y':
        game()
    elif choice[0] == 'n':
        os._exit(1)
    else:
        print "I don't know what that means."
        restart()

def game():
    global attempts, wins
    idx = 0
    answer = random.choice(words_copy)
    while idx < 3:
        clue = lookup.synonym(answer)[idx]
        now = time.time()
        future = now + 10
        print '\nClue: ' + clue
        guess = raw_input('Guess: ').lower()
        if guess == answer or guess + 's' == answer or guess == answer[:-3]:
            print "\nCorrect!"
            wins += 1
            break
        elif now > future:
            print "You ran out of time! The answer was %s." % answer
            break
        else:
            print "\nWrong."
            idx += 1
            if idx == 3:
                print "\nThe answer was %s." % answer

    attempts += 1
    print "Game over. Your score was %d / %d." % (wins, attempts)
    print '-' * 10
    words_copy.remove(answer)
    restart()

print """\nWelcome to Password. Given 3 clues, try to guess
the word. You have 10 seconds to respond to each clue. Good luck!"""
time.sleep(5)
print "3 "
time.sleep(1)
print "2 "
time.sleep(1)
print "1"
time.sleep(1)
print '-' * 10

game()
