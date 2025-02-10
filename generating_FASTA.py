import requests

# List of UniProt accession numbers
accessions = ["Q6P6C2", "Q3TSG4", "D3ZKD3", "E1BH29", "Q6GPB5", "Q66JG8", "Q08BA6", "Q9BT30", "Q0C0C9", "Q58DM4", "P0CB42", "Q13686", "Q9D8F1", "Q8K2U2", "Q2M2S8", "Q9D6Z0", "Q9AC39", "A7HQ17", "B8IJ69", "Q5PQ59", "A2SM89", "Q3KI64", "Q02GS6", "A6VBN0", "Q89ND7", "C1DC72", "Q21GW0", "Q9UT12", "Q9HVQ7", "Q1LQ52", "Q88PI8", "Q3Z3Y1", "B7UM00", "B0UEE1", "Q46X95", "A9BUB4", "Q1IEH2", "B5XT12", "Q2JRM5", "Q2JHA7", "B1LM96", "Q0TJP4", "B2I3B8", "B0V4R8", "B7H096", "B7I4X6", "B7V055", "Q5N1Z8", "Q31SC2", "A1VQD4", "B1JBH6", "A8INH8", "B2ICK3", "B4RDA2", "B0KPJ6", "Q0B7X8", "Q5FTF9", "B1YY34", "Q8PIF6", "F4J0A8", "Q4KID6", "Q8FJM6", "Q128T0", "Q1QN61", "Q39N21", "A6T7W1", "A4Z1C6", "Q6N461", "A5VYU4", "Q0C1R0", "B7MGR2", "A1A944", "Q1REC1", "B1K943", "A0B1L8", "Q1BPK4", "C5CUN1", "Q2IYB5", "A6T463", "A3M1Y4", "Q68F54", "B7LC87", "A9IQD9", "A6T461", "P75779", "B1IXG4", "B1X7D4", "A7ZY61", "C4ZXX6", "A8ESR5", "B3QEW0", "A8G5V8", "Q3BQZ6", "B7NAA4", "A9BBH5", "Q3KRA9", "B0VL49", "B1X0X7", "B7MQQ8", "B7NNN5", "A7ZJL8", "B7LJV5", "Q0B744", "B7M779", "Q6FEQ1", "Q9NXW9", "B2JNF0", "Q13JL5", "A4VI91", "B1YZQ0", "Q8L970", "Q398V5", "Q0T6F7", "P59728", "B5YS96", "Q8X7W8", "B2TVC6", "Q32I80", "Q0AP20", "Q1LIS6", "B2TA88", "Q323Z0", "Q47YL9", "A1W3D7", "Q87BA5", "B2I7E8", "B7KDQ8", "B0U431", "A4GAG3", "Q8LAN3", "Q5UR03", "Q2T602", "A5EBK6", "P59727", "Q0AJ18", "B0RQK3", "Q1GYV3", "A4XQF5", "B9MCK8", "Q134D1", "A3P5N3", "Q4UX14", "A3NK14", "Q8P741", "Q3SUS4", "Q3JM44", "Q63L05", "A1BB44", "Q7V8P9", "C5BLP4", "P0A3X3", "P0A3X2", "P0A3X4", "A2CBC7", "A9HE41", "A5VDM4", "Q3AUN6", "B8E9P5", "B1XLW1", "B0C4F3", "A1K320", "B4SN50", "A5EHJ0", "Q0I9X3", "Q13L77", "B0T179", "Q46S75", "Q3AJA6", "Q6IQE9", "Q1QHD2", "Q9PFQ9", "Q7VB29", "B2FRZ7", "Q5R7X0", "A0A2I1BSW6", "A4YWV8", "A9L129", "A6WJ89", "A1WMG0", "G8GV69", "B7K077", "Q8DHN8", "A7HP27", "Q9C0B1", "Q15TJ8", "P47181", "A2C3W6", "P9WEP3", "A2BS76", "Q1GRV0", "B6JGF2", "Q8BGW1", "Q2L2D7", "Q8EAI9", "Q0HF55", "P0DUL2", "Q91UZ4", "Q46JR2", "B1XWG9", "B4RYP8", "Q5UQY2", "Q0HYV7", "Q9H6Z9", "A3D8P6", "Q07HT7", "Q2A121", "A0KT36", "F4JAU3", "Q8GXT7", "A0A097ZPD5", "Q4WAW9", "B9WZX5", "Q8MNT9", "Q10115", "Q5QUG6", "A2BXM8", "Q087U3", "Q5MNH2", "F1PLN3", "A3PE10", "A0A3G9H185", "Q62630", "A0A2Z5TIR0", "Q319X4", "B8GUF9", "A0A0U5GJ41", "A0A3G9GR23", "Q5MNH9", "Q9SL49", "A5WFM3", "A3KP59", "P37462", "A0A097ZPD9", "Q58DS6", "Q6NYC1", "Q5R6G2", "Q0C8A0", "Q4WAZ3", "A1DA64", "P67773", "P9WI89", "P9WI88", "Q6PFM0"]  # Replace with actual UniProt IDs

# Function to fetch FASTA sequence from UniProt
def fetch_fasta(uniprot_id):
    url = f"https://rest.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch {uniprot_id}: {response.status_code}")
        return None

# Formatting the sequences
formatted_fasta = ""

for acc in accessions:
    fasta_data = fetch_fasta(acc)
    if fasta_data:
        lines = fasta_data.strip().split("\n")
        header = lines[0]  # UniProt header
        sequence = "".join(lines[1:])  # Merge sequence lines

        # Extract species name from the header (example: ">sp|P69905|HBA_HUMAN Homo sapiens (Human)")
        species_name = "Unknown species"
        if "(" in header and ")" in header:
            species_name = header.split("(")[-1].split(")")[0]  # Extract species name dynamically

        # Construct custom header
        custom_header = f">ENA|{acc}|{acc}.1 {species_name}"
        formatted_fasta += f"{custom_header}\n{sequence}\n"

# Save or print the formatted FASTA sequences
with open("formatted_sequences.fasta", "w") as f:
    f.write(formatted_fasta)

print("FASTA sequences saved to formatted_sequences.fasta")
