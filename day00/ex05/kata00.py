# Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.
t = (19, 42, 21)
length = len(t)
i = 0
print('The {0} numbers are:'.format(length), end=' ')
while i < length:
    print(t[i], end='')
    if i < length - 1:
        print(', ', end='')
    else:
        print()
    i += 1
