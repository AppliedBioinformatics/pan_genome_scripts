# pan_genome_scripts

Python scripts for constructing pangenomes using the iterative mapping style for the Bioinformatics Methods Book chapter

Please contact @philippbayer for any comments, questions and queries regarding the scripts

# splitFiles.py
This script is used to split the unmapped fastq files into R1, R2 and unpaired reads for assembly by MaSuRCA.

Usage: `python splitFiles.py filename_unmapped_merged_sortedName.fastq`

# filter_blast.py
This script removes contaminants from the blast output based on the plant genus list. The All_plant_genus_list.txt file can be replaced with any list of genuses

Usage: `python filter_blast.py [merged blast output file] All_plant_genus_list.txt > genome.best.hits.contamination.blast`


# contamination_removal.py

This script is used to filter the contamination out of masurca assembly based on the blast names given by BLAST

This requires the output file of the filter_blast.py script to be filtered into the uncontaminated_chickpea_contig_names.txt file

Usage: `python contamination_removal.py [masurca assembly] uncontaminated_chickpea_contig_names.txt uncontaminated.scf.fasta`

# All_plant_genus_list.txt

A list of all known plant genera
