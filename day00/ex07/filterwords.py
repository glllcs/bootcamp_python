import sys
import string

if (len(sys.argv) != 3):
    print('ERROR')
    exit()
try:
    lim = int(sys.argv[2])
except ValueError:
    print('ERROR')
    exit()
word = ''
filt = []
for c in sys.argv[1]:
    if c != ' ' and c not in string.punctuation:
        word += c
    else:
        if len(word) > lim:
            filt.append(word)
        word = ''
if len(word) > lim:
    filt.append(word)
if len(filt) > 0:
    print(filt)
else:
    print('ERROR')
