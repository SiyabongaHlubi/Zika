import re

def replace_sequence_in_xml(xml_file, sequence_file):
    """Replace the sequence in an XML file with the content from a sequence file."""
    
    # Read the new sequence
    with open(sequence_file, 'r') as f:
        new_sequence = f.read().strip()
    
    # Read the XML file
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    
    # Update the length to 10000
    xml_content = re.sub(r'<length>\d+</length>', '<length>10000</length>', xml_content)
    
    # Replace the sequence content between <sequences> and </sequences>
    xml_content = re.sub(r'<sequences>.*</sequences>', f'<sequences>\n\t\t\t\t{new_sequence}\n\t\t\t</sequences>', xml_content, flags=re.DOTALL)
    
    # Write the updated XML back
    with open(xml_file, 'w') as f:
        f.write(xml_content)
    
    print(f"Updated {xml_file} with sequence from {sequence_file}")

def main():
    # Generate mapping for 100 sequences, but skip Zika_var5.xml to preserve original sequence
    files_mapping = []
    for i in range(1, 101):
        if i == 5:
            continue  # Skip Zika_var5.xml to preserve original sequence
        seq_file = f'sequence_{i}.txt'
        xml_file = f'../Zika_var{i}.xml'
        files_mapping.append((seq_file, xml_file))
    
    print("Replacing sequences in XML files...")
    
    for seq_file, xml_file in files_mapping:
        replace_sequence_in_xml(xml_file, seq_file)
    
    print("All sequences replaced successfully!")

if __name__ == "__main__":
    main()
