import os
from Bio import SeqIO
import subprocess

# Paths
combined_fasta = "combined.fasta"
output_folder = "pssm_outputs"
blast_db = "C:\\blastdb\\swissprot\\swissprot"  # Adjust if your path is different

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Split combined.fasta and run PSI-BLAST on each
for record in SeqIO.parse(combined_fasta, "fasta"):
    seq_id = record.id
    fasta_file = os.path.join(output_folder, f"{seq_id}.fasta")
    pssm_file = os.path.join(output_folder, f"{seq_id}.pssm")
    
    # Save individual fasta
    with open(fasta_file, "w") as f:
        SeqIO.write(record, f, "fasta")
    
    # Run PSI-BLAST
    print(f"🔄 Running PSI-BLAST for {seq_id}...")
    cmd = [
        "psiblast",
        "-query", fasta_file,
        "-db", blast_db,
        "-num_iterations", "3",
        "-evalue", "0.001",
        "-out_ascii_pssm", pssm_file
    ]
    subprocess.run(cmd)

print("✅ All PSSM profiles generated in 'pssm_outputs/'")
