# Bioinformatics 
Useful code for the bioinformatics community at large. 

## EC_automation 
Takes in a list of Enzyme Comission Numbers from Expasy and writes them to a CSV file. 
  - useful for anyone who needs EC numbers in any sort of workflow

## TSV_to_CSV 
Converts a TSV file from Uniport and converts it to a FASTA

## MetaCyc Smarttable Download 
Pulls a premade metacyc smart table and gets rid of the STRING THEY PUT IN THE MIDDLE OF THE TABLE so you can actually use the data

## SPLENDA
Takes in BRENDA's entire JSON file and outputs a file that is just EC numbers and their Inhibitors. Can be tweaked to output other information stored in the JSON that is on the same key level as inhibitor. 

## Directory_Cleaner
For use with Joint Genome Institutes Metaganemoic Bin download - iterates through the download and deletes everything that isn't an .faa

## faa_extractor
For use with Joint Genome Institutes Metagenomic Bin Download - iterates through the download and unzips all .tar.gz files. 
