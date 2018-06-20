#Create function that will compute Hammings error
def H_error(seq1, seq2):
    if len(seq1) != len(seq2):
        return 'Sekwencje nie jednakowej dlugosci'
    else:
        length = len(seq1)
        h_error = [1 for i in range(length) if seq1[i] != seq2[i]]
    return len(h_error)
