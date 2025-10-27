# NCBI Blast simulator : find the peptide  position in the human proteome   

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


