#Create program that will generate 5 random DNA sequences (lenght = 10),
#compute Hamming's error of them and write down results to *.txt file in three columns:
#Sequence1 || Sequence2 || Hamming error



# Importing essentials

import ex5_1 as h
import ex4_3 as d
from itertools import combinations
import os
# Creating random DNA sequences
seq1 = d.randomDNA(10)
seq2 = d.randomDNA(10)
seq3 = d.randomDNA(10)
seq4 = d.randomDNA(10)
seq5 = d.randomDNA(10)

# Setting a combination of comparison
lista_sekwencji = {seq1:'seq1', seq2:'seq2', seq3:'seq3', seq4:'seq4', seq5:'seq5'}
comb = list(combinations(lista_sekwencji.keys(), 2))
combv = list(combinations(lista_sekwencji.values(), 2))
print "Lista kombinacji obliczania odleglosci Hamminga:\n", combv, "\n\n"
combz = zip(*comb)

# Tworzenie listy odleglosci dla zadanych kombinacji
comb1 = list(combz[0])
comb2 = list(combz[1])
list_h_error = [h.H_error(comb1[i],comb2[i]) for i in range(len(comb1))]

print "List of errors for above combinations: %s \n" %list_h_error

# Zapisywanie do pliku
with open('hamming.txt','w') as f:
    for i in range(len(comb)):
        tekst = str(comb[i][0]) + " || " + str(comb[i][1]) +  " || "\
                + str(list_h_error[i]) + "\n"
        f.write(tekst)
print 'Plik z zestawieniem zapisany pod nazwa "hamming.txt" w katalogu ', os.getcwd()

#Koniec dzialania skryptu
