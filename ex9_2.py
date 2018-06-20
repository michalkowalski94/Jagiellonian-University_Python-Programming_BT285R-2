#Create class "RNA" that will take id and sequence as and argument.
#As an atribute of class create function that computes length
#of a sequence automatically.
#Operator of adding two RNA instances should generate a new "RNA" instance (__add__).
#Also create class "DNA(RNA)" that will have inheritance after RNA(object).
#"DNA(RNA)" should contain a method that will develop an complementary sequence.

#Defining RNA class

class RNA(object):
        #Initial parameters
        def __init__(self, sequence, identificator):
                self.id = identificator
                self.seq = sequence
        #Defining legth of sequence
        def length(self):
                if "\n" in self.seq:
                        sq1 = self.seq.split("\n")
                        sq2 = ''.join(sq1)
                        length = len(sq2)
                else:
                        length = len(self.seq)
                return length #returns attribute
        
        #Defining merged sequences
        def __add__(self, sequence2, newid):
                return RNA(self.seq + sequence2, newid)

class DNA(RNA):

        #Initial parameters
        def __init__(self, sequence, identificator):
                super(DNA,self).__init__(sequence, identificator)

        #Defining revertase
        def revertase(self, newid):
                complementary = {"A":"T", "G":"C", "C":"G", "U":"A"}
                if "\n" in self.seq:
                        sq1 = self.seq.split("\n")
                else:
                        sq1 = list(self.seq)
                rDNA = [complementary[i] for i in sq1]
                rvDNA = ''.join(rDNA)
                return DNA(rvDNA, newid)#returns new class
        
        #Defining complementary
        def complementary(self, newid):
                complementary = {"A":"T", "G":"C", "C":"G", "T":"A"}
                sq1 = list(self.seq)
                rDNA = [complementary[i] for i in sq1]
                cDNA = ''.join(rDNA)
                return DNA(cDNA, newid) #returns new class


#Sample result when running as __main__
if __name__ == "__main__":
        header = ">sample sequence"
        sequence = "AUGCGUCGAUC"
        rna = RNA(sequence,header)
        print "RNA SEQUENCE: %s \n" %rna.seq + "RNA ID: %s \n" %rna.id \
              + "RNA LENGTH: %s \n" %rna.length()
        classdna = DNA(rna.seq, rna.id)
        rvDNA = classdna.revertase(">reverted seq")
        cDNA = rvDNA.complementary(">complementary seq")
        print "REVERSED DNA: %s \n" %rvDNA.seq + "ID: %s" %rvDNA.id
        print "COMPLEMENTARY DNA: %s \n" %cDNA.seq + "ID: %s" %cDNA.id
