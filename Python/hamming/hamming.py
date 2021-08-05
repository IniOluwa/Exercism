# Check Hamming Distance Between DNA Sequences
def distance(dna, evolved_dna):

    # Check Length of Both Sequences
    if len(dna) is not len(evolved_dna):
        # Raise Mismatch Exception
        raise ValueError("DNA Lengths Do Not Match!")

    # Declare Hamming Count
    hamming_distance = 0

    # Check Hamming Distance
    for fragment in range(len(dna)):

        # Compare DNA Fragemnts
        if dna[fragment] is not evolved_dna[fragment]:

            # Increment Hamming Distance
            hamming_distance += 1

    # Return Hamming Distance
    return hamming_distance
