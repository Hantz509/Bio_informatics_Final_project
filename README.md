🧬 SNARE Protein Prediction – Feature Engineering Module
This repository contains the data preprocessing and feature extraction pipeline used to prepare input for SNARE protein classification.

👤 Contributor
Member 2 – Feature Extraction & Preprocessing
Responsible for transforming raw protein sequences into machine-readable features, including:

Amino Acid Composition (AAC)

Dipeptide Composition (DPC)

PSI-BLAST derived Position-Specific Scoring Matrix (PSSM)
📁 Folder Structure
blastdb/
├── snare.fasta                 # Positive samples (SNARE proteins)
├── non_snare.fasta             # Negative samples (non-SNARE proteins)
├── combined.fasta              # Merged file with labeled sequence headers
├── pssm_outputs/               # Folder containing .pssm files
├── swissprot/                  # Swiss-Prot BLAST database (local)
├── aac_dpc_features.csv        # Raw AAC+DPC feature matrix
├── final_features.csv          # Combined AAC, DPC, and PSSM features
├── extract_features.py         # Script to compute AAC and DPC
├── combine_fasta.py            # Script to merge FASTA files
├── generate_pssm.py            # PSI-BLAST runner script
├── extract_pssm_features.py    # PSSM parser and final merger
⚙️ Scripts Summary
extract_features.py
Computes 20 AAC + 400 DPC features per sequence

combine_fasta.py
Merges two FASTA files with standardized sequence IDs

generate_pssm.py
Runs PSI-BLAST on each sequence using the Swiss-Prot database

Saves output .pssm files

extract_pssm_features.py
Parses .pssm files and extracts mean-column vectors

Merges them with the AAC+DPC features

✅ Final Output
final_features.csv
A feature-rich dataset ready for classification with:

20 AAC features

400 DPC features

20 PSSM features

label column (1 = SNARE, 0 = non-SNARE)

🧪 Tools Used
Python (Biopython, Pandas, NumPy)

NCBI BLAST+ Toolkit

Swiss-Prot Database (locally stored)

