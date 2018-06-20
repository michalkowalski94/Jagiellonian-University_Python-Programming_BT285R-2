#Create function that will count apperance of each codon/letter in string
from ex3_1 import openFASTA
import collections as c
#My method with collections module
#Returns class 'collections.Counter'
def countletters(var_name = 'seq1.fa'):
    """This function returns class 'collections.Counter'.
        To access objects assign function to variable and simply find
        counter of apperance by index method e.g
        a = countletters()
        Tcount = a['T']
        Function can operate on fasta files if extension *.fa or *.fasta
        occurs in var_name string"""
    if ('.fasta' or '.fa') in var_name:
        fasta = openFASTA(var_name)
        seqs = fasta[1]
    else:
        seqs = var_name
        counter = c.Counter(seqs)
    return counter

#Another method, more respected by lecturer and enchanced with
#distribution percentage
def countletters2(var_name = 'seq1.fa'):
    """This function returns tuple with two dictionaries.
        First one contains counter of elements of string.
        Second one contains distribution percentage
        Function can operate on fasta files if extension *.fa or *.fasta
        occurs in var_name string"""
    if ('.fasta' or '.fa') in var_name:
        fasta = openFASTA(var_name)
        seqs = fasta[1]
    else:
        seqs = var_name
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
