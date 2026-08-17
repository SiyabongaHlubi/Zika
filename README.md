# Zika

Forward-time simulations of Zika virus evolution with [SANTA-SIM](https://github.com/santa-dev/santa-sim), used to study how mutation rate and recombination probability shape viral diversity.

## Experimental design

Nine conditions cross three mutation rates with three recombination probabilities. Each condition contains 100 independent replicate variants (`Zika_var1` … `Zika_var100`), each seeded with its own random 10,000 bp sequence.

| Condition | Mutation rate | Recombination probability |
| --------- | ------------- | ------------------------- |
| C1 | 2.5E-5 | 0.005 |
| C2 | 2.5E-5 | 0.010 |
| C3 | 2.5E-5 | 0.020 |
| C4 | 1E-4   | 0.005 |
| C5 | 1E-4   | 0.010 |
| C6 | 1E-4   | 0.020 |
| C7 | 2E-4   | 0.005 |
| C8 | 2E-4   | 0.010 |
| C9 | 2E-4   | 0.020 |

All other simulation settings are shared, coming from the template `C5/configs/Zika_var1.xml`:

- population size 1000, full inoculum, 5000 generations, 1 replicate
- genome features `E` (1200-2500), `NS3` (4800-6500), `NS5` (9200-11520)
- population-size-dependent fitness on `NS5` sites 1-100 (decline rate 0.003, max population 30000)
- nucleotide mutator with a rate bias matrix, recombinant replicator with dual infection probability 0.1
- sampling every 10 generations (`frequency_%r.csv`) plus a final 50-sequence sample (`final_sample_%r.fasta`)

## Layout

```
C1..C9/
  configs/
    Zika_var1.xml ... Zika_var100.xml   SANTA config per replicate
    generated sequences/
      sequence_1.txt ... sequence_100.txt   starting 10,000 bp sequences
  results/
    Zika_varN/
      frequency_1.csv        per-generation diversity/fitness statistics
      final_sample_1.fasta   final sampled sequences
generate_all_configs.py   populates every condition from the C5 template
```

Only `C5` currently has committed results; the other conditions hold configs ready to run.

## Regenerating configs

`generate_all_configs.py` rewrites the sequences and configs for C1-C4 and C6-C9 from the C5 template, substituting each condition's mutation rate, recombination probability and output paths. Sequences are random, so rerunning it replaces the existing ones.

```bash
python3 generate_all_configs.py
```

The scripts in `generate_configs.py`, `generate_dna_sequences.py` and `replace_sequences.py` (also copied into `C1/`) are the earlier single-condition helpers that `generate_all_configs.py` supersedes.

## Running a simulation

Run SANTA-SIM from the condition directory so the relative `results/` paths in the config resolve correctly:

```bash
cd C1
java -jar /path/to/santa.jar configs/Zika_var1.xml
```
