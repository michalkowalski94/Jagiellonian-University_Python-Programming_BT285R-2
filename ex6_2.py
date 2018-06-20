#Define function subDNA() that will find substrings in DNA sequence
#with respect to 3 codon reading frame
#Each substring should contain at least one repetition of each codon
#Function must return list of substrings


import ex4_3 as rDNA #for random DNA to test funcions in interpreter
import ex3_3 as count
from sets import Set

#Substring searching function
def subDNA(sequence, frame = 3):
        """Variable frame can be set to any integer you want, if you are searching
                for example for periodic redundancies
                Function returns list of substrings"""
        length = len(sequence)
        opt = [sequence[i:j+1] for i in range(0,length,frame)\
               for j in range(i,length) if (j+1)-i >=4 and ((j+1)-i)%frame == 0]
        pre_substrings = [i for i in opt if (len(set(i)\
                      & set('ATCG')) == 4)]
        substrings = [str(pre_substrings[i]) for i in xrange(len(pre_substrings)) if \
                      (not str(pre_substrings[i]).startswith(str(pre_substrings[i-1])))]
        return substrings

#Create function that will count letters in substring, and will show last letter of ech substring
#Result must be in list of tuples

def subCOUNT(substrings):
        """This function creates a list of tuples of counter of letters in substrings and last letters in substrings"""
        sbst = substrings
        sbst_counter = [(sbst[j], count.countletters2(sbst[j])[0], sbst[j][len(sbst)-1])\
                               for j in range(len(sbst))]
        return sbst_counter
