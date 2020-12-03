import sys

phrase = ' '.join(sys.argv[1:])
phrase = phrase[::-1]
phrase = phrase.swapcase()

print(phrase)
