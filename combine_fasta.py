from Bio import SeqIO

# Input files
snare_file = "snare.fasta"
non_snare_file = "non_snare.fasta"

# Load and label
snare_records = list(SeqIO.parse(snare_file, "fasta"))
non_snare_records = list(SeqIO.parse(non_snare_file, "fasta"))

# Update IDs
for i, record in enumerate(snare_records):
    record.id = f"snare_{i+1:03}"
    record.description = ""

for i, record in enumerate(non_snare_records):
    record.id = f"non_{i+1:03}"
    record.description = ""

# Write combined file
combined = snare_records + non_snare_records
SeqIO.write(combined, "combined.fasta", "fasta")

print("✅ combined.fasta created successfully!")
