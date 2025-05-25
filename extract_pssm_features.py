import os
import pandas as pd
from pathlib import Path

def parse_pssm_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    data_started = False
    values = []

    for line in lines:
        if line.strip().startswith("Last position-specific scoring matrix computed"):
            break
        if data_started:
            parts = line.strip().split()
            if len(parts) >= 22 and parts[0].isdigit():
                row = list(map(int, parts[2:22]))
                values.append(row)
        elif line.strip().startswith("  Pos"):
            data_started = True

    if not values:
        return [0] * 20  # fallback
    matrix = pd.DataFrame(values)
    return matrix.mean().tolist()

# Set paths
pssm_folder = Path("pssm_outputs")
aac_dpc_csv = Path("aac_dpc_features.csv")
output_csv = Path("final_features.csv")

# Load AAC + DPC features
df = pd.read_csv(aac_dpc_csv)

# Prepare PSSM features
pssm_features = []
missing_ids = []

for seq_id in df['id']:
    pssm_path = pssm_folder / f"{seq_id}.pssm"
    if pssm_path.exists():
        vector = parse_pssm_file(pssm_path)
    else:
        vector = [0] * 20
        missing_ids.append(seq_id)
    pssm_features.append(vector)

# Append to DataFrame
pssm_columns = [f"PSSM_mean_{i+1}" for i in range(20)]
pssm_df = pd.DataFrame(pssm_features, columns=pssm_columns)
final_df = pd.concat([df.reset_index(drop=True), pssm_df], axis=1)

# Save
final_df.to_csv(output_csv, index=False)
print(f"✅ Final merged file saved as '{output_csv}'")

if missing_ids:
    print(f"⚠️ Missing PSSM files for {len(missing_ids)} sequences.")
