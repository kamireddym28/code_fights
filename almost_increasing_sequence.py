def almostIncreasingSequence(sequence):
    seq1 = sequence[:]
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            sequence.remove(sequence[i])
            del(seq1[i+1])
            break
    return (all(i < j for i,j in zip(sequence, sequence[1:])) or
            all(i < j for i,j in zip(seq1, seq1[1:])))
