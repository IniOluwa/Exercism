# Get the sum of dna irregularities.
def distance(dna, evolved_dna):
    count = 0
    for i in range(len(dna)):
        if dna[i] != evolved_dna[i]:
            count += 1
    return count