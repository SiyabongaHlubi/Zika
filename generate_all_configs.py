import os
import random
import re

TEMPLATE = 'C5/configs/Zika_var1.xml'
CONDITIONS = ['C1', 'C2', 'C3', 'C4', 'C6', 'C7', 'C8', 'C9']
NUM_VARIANTS = 100
SEQUENCE_LENGTH = 10000
NUCLEOTIDES = 'ACTG'


def generate_random_dna_sequence(length):
    """Generate a random DNA sequence of specified length using A, C, T, G."""
    return ''.join(random.choice(NUCLEOTIDES) for _ in range(length))


def build_config(template_content, sequence, variant):
    """Return the config for a variant with its sequence and output paths set."""
    content = re.sub(
        r'<sequences>.*?</sequences>',
        f'<sequences>\n\t\t\t\t{sequence}\n\t\t\t</sequences>',
        template_content,
        flags=re.DOTALL,
    )
    return content.replace('Zika_var1/', f'Zika_var{variant}/')


def populate_condition(condition, template_content):
    configs_dir = os.path.join(condition, 'configs')
    sequences_dir = os.path.join(configs_dir, 'generated sequences')
    os.makedirs(sequences_dir, exist_ok=True)
    os.makedirs(os.path.join(condition, 'results'), exist_ok=True)

    for i in range(1, NUM_VARIANTS + 1):
        sequence = generate_random_dna_sequence(SEQUENCE_LENGTH)

        with open(os.path.join(sequences_dir, f'sequence_{i}.txt'), 'w') as f:
            f.write(sequence)

        with open(os.path.join(configs_dir, f'Zika_var{i}.xml'), 'w') as f:
            f.write(build_config(template_content, sequence, i))

    print(f'Populated {condition} with {NUM_VARIANTS} sequences and configs')


def main():
    with open(TEMPLATE) as f:
        template_content = f.read()

    for condition in CONDITIONS:
        populate_condition(condition, template_content)

    print('All conditions populated successfully!')


if __name__ == '__main__':
    main()
