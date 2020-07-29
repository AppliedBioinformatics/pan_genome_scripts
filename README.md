# pan_genome_scripts

Python scripts for constructing pangenomes using the iterative mapping style for the Bioinformatics Methods Book chapter

Please contact @philippbayer for any comments, questions and queries regarding the scripts

# splitFiles.py
This script is used to split the unmapped fastq files into R1, R2 and unpaired reads for assembly by MaSuRCA.

Usage: `python splitFiles.py filename_unmapped_merged_sortedName.fastq`

# filter_blast.py
This script removes contaminants from the blast output based on the plant genus list. The All_plant_genus_list_updated.txt file can be replaced with any list of genuses

Usage: `python filter_blast.py [merged blast output file] All_plant_genus_list_updated.txt > genome.best.hits.contaminantion.blast`
