# Rosalind: Computing Point Mutation (Hamming Distance)
# Counts the number of Positions where two equal lengt DNA strings differ
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = 0
for i in range(len(s)):
	if s[i] != t[i]:
	 distance += 1

print(distance)
