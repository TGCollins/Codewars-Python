def DNA_strand(dna):
    map = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([map[i] for i in dna])
