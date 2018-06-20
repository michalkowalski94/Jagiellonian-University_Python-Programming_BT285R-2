#Write a program to open seq1.fa (fasta) file
#Read a header and a sequences
#Display header and sequence length
with open("seq1.fa") as f:
    header = f.readline()
    seqs = f.read()
lines = seqs.split('\n')#removing end of line sign
seqs_pars = ''.join(lines)
lenseq = len(seqs_pars)
print 'Header: %s' %header
print 'Sequence: %s' %seqs_pars
print 'Length of sequence: %s' %lenseq

#Write header and sequence to new fasta file with propper format of the text
lenmax = 60
linelist = []
s0 = seqs_pars
while len(s0) != 0: #while loop for creating 60 characters line with replacing
    linelist.append(s0[0:lenmax-1])#already taken with empty string
    result = s0.replace(s0[0:lenmax-1], "")
    s0 = result
newlines = '\n'.join(linelist)#creating string out of new lines
with open("seq2.fasta", "w") as f:
    f.write(header)
    f.write(newlines)
