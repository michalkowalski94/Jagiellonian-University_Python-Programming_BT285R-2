#Define funcion that will count apperance of each letter in string
from ex3_1 import openFASTA

#My method
def countletters(filename = 'seq1.fa'):
    """This function return class 'collections.counter"""
    import collections
    fasta = openFASTA(filename)
    seqs = fasta[1]
    counter = collections.Counter(seqs)
    return counter
#Method respected by lecturer with addition
#of displaying percentage distribution
def countletters2(filename = 'seq1.fa'):
    """This function returns tuple with two dictionaries
        First contains counter of each letter/nucleotide
        Sedond contains distribution percentage"""
    fasta = openFASTA(filename)
    seqs = fasta[1]
    dictn = {}
    lenseq = len(seqs)
    for x in seqs:
        if x not in dictn: dictn[x] = 0
        dictn.setdefault(x,0)
        dictn[x] = dictn[x] + 1
    keys = dictn.keys()
    freqs = []
    for i in dictn:
        freq = dictn[i]/float(lenseq)
        freqs.append(freq)
    answer = {}
    for i in range(len(keys)):
        answer[keys[i]] = freqs[i]
    return dictn, answer
