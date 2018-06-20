
def readPhonebook(filename='phonebook.txt'):
    fh = open(filename,'r')
    entries = fh.readlines()
    fh.close()
    #
    data = []
    for item in entries:
        if not item.strip(): continue
        data.append( tuple(item.split()) )
    return data

def redefine(entries):
    return [ (ln, fn, n) for n, fn, ln in entries ]

def writePhonebook(entries):
    data = redefine(entries)
    data.sort()
    for entry in data:
        print '%15s %-10s ::: %s' % entry

def searchPhonebook(fullname, entries):
    phonebook = dict([ ('%s %s' % (ln, fn), n) \
                           for ln, fn, n in redefine(entries) ])
    if phonebook.has_key(fullname):
        return phonebook[fullname]

if __name__ == '__main__':
    entries = readPhonebook()
    writePhonebook(entries)
    print searchPhonebook('Gowin Jaro', entries)
    print searchPhonebook('Szydlo Beata', entries)


