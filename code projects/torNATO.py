# takes a word provided by the user and spells phonetically using the NATO alphabet

word = input("Type a word and I'll spell it with the NATO Phonetic Alphabet. ")

def newNATOfunc(x):
    # initial dictionary where index is a letter and its value is the phonetic equivalent 
    natoBET = {
        'a': 'ALPHA',
        'b': 'BRAVO',
        'c': 'CHARLIE',
        'd': 'DELTA',
        'e': 'ECHO',
        'f': 'FOXTROT',
        'g': 'GOLF',
        'h': 'HOTEL',
        'i': 'INDIA',
        'j': 'JULIETT',
        'k': 'KILO',
        'l': 'LIMA',
        'm': 'MIKE',
        'n': 'NOVEMBER',
        'o': 'OSCAR',
        'p': 'PAPA',
        'q': 'QUEBEC',
        'r': 'ROMEO',
        's': 'SIERRA',
        't': 'TANGO',
        'u': 'UNIFORM',
        'v': 'VICTOR',
        'w': 'WHISKEY',
        'x': 'X-RAY',
        'y': 'YANKEE',
        'z': 'ZULU',
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE',
        '.': 'POINT',
        '00': 'HUNDRED',
        '000': 'THOUSAND',
        '-': 'HYPHEN',
        ' ': 'STOP',
        '?': 'STOP',
        '!': 'STOP',
        ',': 'STOP',
        ':': 'STOP',
        ';': 'STOP' 
        }
    NATOequiv = [] # empty list to add string characters of input word
    newNATO = [] # appended list for output

    stringWord = str(word) # convert input to a string
    lcaseWord = stringWord.lower() # convert string to lowercase
    # print(lcaseWord) # 1st test point

    for letter in lcaseWord:
        NATOequiv.append(letter)

    # print(NATOequiv) # 2nd test point

    for i in NATOequiv:
        for k, v in natoBET.items():
            if i == k:
                newNATO.append(v)

    print(newNATO)
    # print("Your word is " + stringWord + " and the NATO equivalent is " + newNATO + ".")

newNATOfunc(word)