from PyDictionary import PyDictionary
words = PyDictionary()

def meanings():
    while True:
        word = raw_input('\nWord: ').lower()
        if word == 'q':
            exit(1)
        lookup = words.meaning(word)
        for part_of_speech in lookup:
            if word in lookup[part_of_speech]:
                continue
            else:
                print part_of_speech,'\n', lookup[part_of_speech]

def synonyms():
    while True:
        word = raw_input('\nWord: ').lower()
        if word == 'q':
            exit(1)
        lookup = words.synonym(word)
        print "\nSynonyms:"
        for synonym in lookup:
            print synonym

def antonyms():
    while True:
        word = raw_input('\nWord: ').lower()
        if word == 'q':
            exit(1)
        lookup = words.antonym(word)
        print "\nAntonyms:"
        for antonym in lookup:
            print antonym

def select():
    choice = raw_input('Would you like meanings, synonyms, or antonyms? ').lower()
    if choice[0] == 'm':
        meanings()
    elif choice[0] == 's':
        synonyms()
    elif choice[0] == 'a':
        antonyms()
    else:
        print "I don't know what %s means." (choice)
        select()
