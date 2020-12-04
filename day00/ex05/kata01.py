# Dictionaries are used to store data values in key:value pairs.
# They are unordered, changeable and do not allow duplicates.
languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf'
    }
for key in languages:
    print("{0} was created by {1}".format(key, languages[key]))
