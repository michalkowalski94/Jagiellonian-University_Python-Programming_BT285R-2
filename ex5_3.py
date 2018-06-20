#Open hamming.txt and by using map() and zip()
#read data from file and display average hamming error
with open('hamming.txt','r') as f:
    text = f.readlines()
halfway = map(lambda i: i.split(), text)
columns = zip(*halfway)
errors = map(float, columns[4])
print errors
avg = int(sum(errors)/len(errors)) #Integer because Hammings error must be Natural
print "Average Hamming's error is equal to: %s" %avg
