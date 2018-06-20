#Sort list considering second letters in listerd words

phrase = ["ala","ma","kota"]
print "List to sort %s" %phrase
s_phrase = sorted(phrase, key = lambda i: i[1])
print "Sorted list %s" %s_phrase
