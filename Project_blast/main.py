kinase = [
    ['AKT1', 'TERNS___'],
    ['AKT2', 'TERNS___'],
    ['AKT3', 'TERNS___'],
    ['AAK1', '___MTTEV'],
    ['ALK2', '___MTTEV'],
    ['YANK2', '___MTTEV'],
    ['DLK', 'TNIQS___'],
    ['PKCG', 'LRKKS___'],
    ['ERK5', '___MSARG'],
    ['ERK7', '___MSARG'],
    ['KHS2', 'GSKLTIQE'],
    ['LOK', 'GSKLTIQE'],
]

with open("sequence.csv") as f:
    sequences = f.readlines()



# for kin in kinase:
#     kinase_name = kin[0]
#     peptide = kin[1]
#     left = len(peptide) - len(peptide.lstrip("_"))
#     right = len(peptide) - len(peptide.rstrip("_"))
#     clean_peptide = peptide.strip("_")

#     for seq in sequences:
#         seq = seq.split(",")
#         protein = seq[0]
#         fasta = seq[1]

#         pos_start = fasta.find(clean_peptide)

#         if pos_start != -1:
#             pos_end = pos_start + len(peptide)
#             print(f"{kinase_name}  with petide{peptide} found at positions {pos_start} to {pos_end} in the protein-> {protein}") 

