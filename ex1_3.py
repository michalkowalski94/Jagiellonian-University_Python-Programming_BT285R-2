#Write a program which will display a number of sequences,
#sort them by length, compute length of each of them and will find
#max and min length. Operation on nn_seqs.txt
import operator
with open("nn_seqs.txt") as f:
    seqs0 = f.read()
seqs1 = seqs0.split('\n')
seqs1.remove('')

seqs_quant = len(seqs1)
lenlist = [len(i) for i in seqs1]
seqscombine = []
for i in range(len(seqs1)):
    element = [lenlist[i], seqs1[i]]
    seqscombine.append(element)
seqsend = sorted(seqscombine, key = operator.itemgetter(0))
minimalval = min(lenlist)
maximalval = max(lenlist)
print "List of list of sequences and lengths: %s \n" %seqsend
print "Maximal value: %s \n" %maximalval
print "Minimal value: %s \n" %minimalval

