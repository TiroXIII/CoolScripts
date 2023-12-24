# Calculate the Hamming Distance between two DNA strands.

# Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they
# achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion cell
# divisions in a lifetime!

# When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA
# get encoded with the incorrect information. If we compare two strands of DNA and count the differences between them
# we can see how many mistakes occurred. This is known as the "Hamming Distance".

# We read DNA using the letters C,A,G and T. Two strands might look like this:

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^
# They have 7 differences, and therefore the Hamming Distance is 7.

# The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to be
# familiar with :)

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_count = []
    count = 0
    while len(hamming_count) < len(strand_a):
        if strand_a[count] == strand_b[count]:
            hamming_count.append(0)
        else:
            hamming_count.append(1)
        count += 1
    print(hamming_count)
    return sum(hamming_count)
