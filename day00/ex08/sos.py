import sys

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
    }


def translate_morse(args):
    """This function translates english to morse"""
    sentence = ' '.join(args)
    sentence = ' '.join(sentence.split())
    sentence = sentence.upper()
    for c in sentence:
        if c not in list(morse.keys()):
            print('ERROR')
            exit()
    j = 0
    for j in range(0, len(sentence)):
        print(morse[sentence[j]], end='')
        if j == len(sentence) - 1:
            print()
        else:
            print(' ', end='')


translate_morse(sys.argv[1::])
