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


print(type(sequences))

print(len(sequences))
for items in kinase:
    peptide = items[0]
    left = len(items) - len(peptide.lstrip('_'))   # underscores on the left
    right = len(items) - len(peptide.rstrip('_'))  # underscores on the right


    for sequ in sequences:
        split_seq = sequ.split(",")
        
        protein =  split_seq[0].split('|')
        start_index = split_seq[1].find(peptide.strip('_'))

        if start_index != -1:
            end_index = start_index + len(peptide.strip('_')) - 1
            print(f"{peptide} found at positions {start_index} to {end_index} in the protein-> {protein[1]}") 
