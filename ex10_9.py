#Open ex10_9.fasta, create two vars (headers, sequences)
#Parse text with width frame set to 70 characters
#Chagne header to "known sequence"
#Write vars down to a new file

with open("ex10_9.fasta") as f:
	header = f.readline()
	seqs = f.read()

header = ">known sequence" #well... simple
sq1 = seqs.split("\n")
sq2 = "".join(sq1)
width = 70
temp = sq2
linelist = []
while len(temp) != 0: #while loop for creating 70 characters line with replacing
    linelist.append(temp[0:width])#already taken with empty string
    result = temp.replace(temp[0:width], "")
    temp = result
newlines = '\n'.join(linelist)
with open("ex10_9_after.fasta", "w") as f:
    f.write(header+"\n")
    f.write(newlines)
