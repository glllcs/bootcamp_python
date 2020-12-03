import sys
import string


def text_analyzer(text='', *args):
    """This function counts the number of upper characters, lower characters, \
punctuation and spaces in a given text."""
    if len(args) > 0:
        print("ERROR")
        return
    if text == '':
        text = input("What is the text to analyse?\n")
    upper = 0
    lower = 0
    space = 0
    punct = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isspace():
            space += 1
        elif c in string.punctuation:
            punct += 1
    print("The text contains %d characters:" % len(text))
    print("- %d upper letters" % upper)
    print("- %d lower letters" % lower)
    print("- %d punctuation marks" % punct)
    print("- %d spaces" % space)
    return
