# Sort "phonebook" from last lecture
# The key should be a persons surname

import phonebook
a = phonebook.readPhonebook()
b = phonebook.redefine(a)
c = sorted(b, key = lambda ln: ln[0])
print c
