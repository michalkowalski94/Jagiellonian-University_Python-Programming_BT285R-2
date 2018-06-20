#Create functions from recent scripts
import os
import string
# Opening of file
def openFASTA(filename):
    """Please insert file name with extension in '' to open file as list
        in which element indexed by [0] will be a header string
        and indexed by [1] will be string with sequences without EOL signs"""
    with open(filename) as f:
        if not f.readline().startswith('>'):
            header = "No ID in file"
            f.seek(0)
        else:
            f.seek(0)
            header = f.readline()
        seqs = f.read()
        forbidden = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
        for i in range(len(forbidden)):
            if forbidden[i] in seqs:
                seqs = "Not a fasta file"
            else:
                if '\n' in seqs:
                    header = header.strip('\n')
                    seqslist = seqs.split('\n')
                    seqslist.remove('')
                    seqs = ''.join(seqslist)
    return header, seqs
# Writing down to fasta format
def outputFASTA(header, seqs, filename, width = 60):
    """Fasta format by standard contains 60 characters in one line.
        Plese insert variables of header, sequence and filename (if filename
        variable is not defined, insert file name in '')
        Do not forget to add an extension *.fasta to filename"""
    lines = []
    while len(seqs) != 0:
        lines.append(seqs[0:width])
        result = seqs.replace(seqs[0:width], "")
        seqs = result
    seqs = '\n'.join(lines)
    with open(filename, 'w') as f:
        f.write(header + '\n')
        f.write(seqs)
    print 'File saved in ', os.getcwd(), ' under the name: ', filename
#Wyszukiwanie pozycji patternu po podanych parametrach
def searchPAT(seqs, pattern):
    """Please  pattern as a variable or in ''.
        As seqs assign proper variable"""
    n = len(seqs)
    m = len(pattern)
    s = 0
    for s in range(n-m):
        if pattern[1:m] == seqs[s+1:s+m]:
            print "Patttern occurs at %s position" %s
