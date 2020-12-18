import random


def generator(text, sep=" ", option=None):
    '''Takes a text as input, uses the string sep as a splitting parameter, \
and yields the resulting substrings.'''
    if not isinstance(text, str):
        print("ERROR")
        exit()
    words = text.split(sep)
    if option is None:
        return (words)
    elif option == "unique":
        unq_list = []
        for w in words:
            if w not in unq_list:
                unq_list.append(w)
        return (unq_list)
    elif option == "shuffle":
        random.randint(0, len(words))
        i_shf = []
        shf_list = []
        while len(i_shf) != len(words):
            i = random.randint(0, len(words) - 1)
            if i not in i_shf:
                i_shf.append(i)
                shf_list.append(words[i])
        return (shf_list)
    elif option == "ordered":
        words.sort()
        return (words)
    else:
        print("ERROR")
        exit()
