def dna_to_rna(dna):
    translation = ""
    for letter in dna:
        if letter.upper() in "T":            
            translation = translation + "U"
        else:
            translation = translation + letter
    return translation