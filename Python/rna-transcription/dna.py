# DNA - RNA dictionary
rna = {
    'A': 'U',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}


def to_rna(dna):
    # Looping for conversion to RNA
    scrambled = 'I'
    for char in dna:
        for key in rna.keys():
            if char == key:
                dna = dna.replace(char, rna.get(key))
                scrambled = scrambled + dna[0]
                dna = dna[1:]
    scrambled = scrambled[1:]
    return scrambled