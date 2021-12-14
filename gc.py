#Calculates the gc percent of a dna sequence

dna='acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag'
ct_c=dna.count('c')
ct_g=dna.count('g')
dna_length=len(dna)
gc_percent=((ct_c+ct_g)*100)/dna_length
print(gc_percent)