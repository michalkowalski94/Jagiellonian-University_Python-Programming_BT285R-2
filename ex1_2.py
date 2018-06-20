#Perform program that will ask user for his same,
#then it will make comment on it's length

print "Please enter Yout name here:"
name = raw_input()
name1 = list(name)
namelength = len(name)

if namelength < 6:
    print "Your name is %s letters long... That's a short name" %namelength
elif (namelength >= 6) and (namelength <= 8):
    print "Your name is %s letters long... That's an average name" %namelength
else:
    print "Your name is %s letters long... That's a long name" %namelength

