import random

def generate_random_dna_sequence(length):
    """Generate a random DNA sequence of specified length using A, C, T, G."""
    nucleotides = ['A', 'C', 'T', 'G']
    return ''.join(random.choice(nucleotides) for _ in range(length))

def main():
    sequence_length = 10000  # 10KB = 10,000 nucleotides
    num_sequences = 100
    
    print(f"Generating {num_sequences} random DNA sequences of {sequence_length} nucleotides each...")
    
    for i in range(1, num_sequences + 1):
        sequence = generate_random_dna_sequence(sequence_length)
        filename = f"sequence_{i}.txt"
        
        with open(filename, 'w') as f:
            f.write(sequence)
        
        print(f"Generated {filename}")
    
    print("All sequences generated successfully!")

if __name__ == "__main__":
    main()
