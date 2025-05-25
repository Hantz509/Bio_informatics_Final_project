from Bio import SeqIO
import pandas as pd
import numpy as np
from itertools import product

AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'
DIPEPTIDES = [''.join(p) for p in product(AMINO_ACIDS, repeat=2)]

def compute_aac(seq):
    length = len(seq)
    return [seq.count(aa) / length for aa in AMINO_ACIDS]

def compute_dpc(seq):
    dpc_counts = {dp: 0 for dp in DIPEPTIDES}
    for i in range(len(seq) - 1):
        dp = seq[i:i+2]
        if dp in dpc_counts:
            dpc_counts[dp] += 1
    total = sum(dpc_counts.values())
    return [dpc_counts[dp] / total if total > 0 else 0 for dp in DIPEPTIDES]

def extract_features_from_fasta(file_path, label):
    records = list(SeqIO.parse(file_path, 'fasta'))
    data = []
    for record in records:
        seq = str(record.seq).upper()
        if not set(seq).issubset(set(AMINO_ACIDS)):
            continue
        aac = compute_aac(seq)
        dpc = compute_dpc(seq)
        row = [record.id] + aac + dpc + [label]
        data.append(row)
    return data

snare_file = 'snare.fasta'
non_snare_file = 'non_snare.fasta'

snare_data = extract_features_from_fasta(snare_file, 1)
non_snare_data = extract_features_from_fasta(non_snare_file, 0)

columns = ['id'] + [f'AAC_{aa}' for aa in AMINO_ACIDS] + [f'DPC_{dp}' for dp in DIPEPTIDES] + ['label']
df = pd.DataFrame(snare_data + non_snare_data, columns=columns)
df.to_csv('aac_dpc_features.csv', index=False)

print("✅ Feature extraction complete! Saved as 'aac_dpc_features.csv'")
