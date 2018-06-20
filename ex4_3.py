#Create runction that will generate random DNA sequence
#Function must be defined with options of assaging distribution to each nucleotide
import random as r
def randomDNA (length, dist={'pA':0.25, 'pC':0.25,'pG':0.25,'pT':0.25}):
    """This function generates random DNA string
        'dist' is dictionary containing distribution
        to change distribution assign percentage values to 'pA', 'pC', 'pG'
        and 'pT' keys.
        'length' is variable responsible for length of string."""
    nucs = ['A','C','T','G']
    dnalist = [nucs[j] for j in range(len(nucs))\
               for i in range(int(length*dist['pA'])\
                              and int(length*dist['pC'])\
                              and int(length*dist['pG'])\
                              and int(length*dist['pT']))]
    while len(dnalist) != length:
        dnalist.append(nucs[r.randrange(3)])
    r.shuffle(dnalist)
    dnaseq = ''.join(dnalist)
    return dnaseq
