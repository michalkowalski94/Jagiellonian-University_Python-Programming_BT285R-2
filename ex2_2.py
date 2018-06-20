#Create a program that will display postition of match to the string
with open('seq2.fasta') as fasta:
    header = fasta.readline()
    seqs = fasta.read()
lines = seqs.split('\n')
seqs = ''.join(lines)
pattern = seqs[55:79]
def przesuniecie():
	n = len(seqs)
	m = len(pattern)
	s = 0
	for s in range(n-m):
		if pattern[1:m] == seqs[s+1:s+m]:
			print "Patttern occurs at %s position" %s
przesuniecie()
