# SAM-analyzer
This is part of my final assessement for the microcredential Basic Digital Competences for Computational Biology.

## Introduction to the programme

This program enables post-alignment quality analysis of SAM files. It processes the file line-by-line, examining read alignments to quantify both the total volume and mapping precision.

The script records the total number of alignments by filtering out all header lines (starting with the '@' symbol). It specifically identifies alignments with confidence that a read is correctly positioned within the reference genome.

## Use of the program

You can run the analysis in two ways depending on your needs:

Option A: Standard Execution (using uv)
Ideal for a quick analysis of a single file.

```bash
uv run main.py path/to/your/file.sam
```
It is required to have the uv dependent rich installed, which is possible with the following command:

```bash
uv add rich
```

Option B: Pipeline Execution (using Nextflow)
Ideal for integrating this script into bioinformatics workflows.

```bash
nextflow run main.nf --sam
```
