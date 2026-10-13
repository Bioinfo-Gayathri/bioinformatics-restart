#Rosalind: Computing GC content
# Calculating perscentage of G and C bases in the DNA

dna = "AGCTATAG" 

g_count = dna.count("G")

c_count = dna.count("C")
gc_content = (g_count + c_count) / len(dna) * 100
print(gc_content) 