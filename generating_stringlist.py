import pandas as pd

# Load Excel file
df = pd.read_excel("uniprot_id.xlsx")  # Update with your actual file name

# Extract and format the accession numbers
accessions = ', '.join(f'"{acc}"' for acc in df["Accession"].dropna())

# Print the formatted list
print(accessions)