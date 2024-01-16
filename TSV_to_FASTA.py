import os#; print('os version: ', os.__version__)
import re#; print('re version: ', re.__version__)
import requests#; print('requests version: ', requests.__version__)
import time#; print('time version: ', time.__version__)
from fake_useragent import UserAgent
import os.path

def tsv_to_fasta():
    reference_library = 'uniprot.tsv' 
    #this creates a file named 'uniprot.tsv' on the working directory. Should show within the EcoDr/EcoDr folder. 
    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}
    uniprot_url = 'https://rest.uniprot.org/uniprotkb/stream?fields=accession%2Cec%2Csequence&format=tsv&query=%28%28ec%3A*%29%29+AND+%28reviewed%3Atrue%29'
    time.sleep(4)
    uniprot = requests.get(uniprot_url, headers=header)
    if uniprot.status_code == 200:
        with open(reference_library, 'w+') as reference_library:
            reference_library.write(uniprot.text)
    print('Uniprot Reference File Has Been Created')
####this step takes it the initial tsv and converts it to FASTA
    input = os.path.abspath('uniprot.tsv')
    output = 'uniprot.fasta'
    with open(input, 'r') as input_file, open(output, 'w') as output_file:
        header=next(input_file)
        for line in input_file:
            carrot = f'>{line}'
            new_row = re.sub(r'(.*?\t.*?)\t', r'\1\n', carrot, 1)
            new_row_with_tab_replaced_by_question_mark = new_row.replace("\t", "?")
            # Be careful with the symbols used for replacement, as they have to align with the genomic summary string parsing
            output_row_with_space_replaced_with_ampersand = new_row_with_tab_replaced_by_question_mark.replace("; ", ";_")
            #new_row2 = re.sub(r'(.*?\t.*?)\t', r'$', new_row, 0)
            #this is regex, for the record. 
            output_file.write(output_row_with_space_replaced_with_ampersand)
    print('FASTA has been created from TSV and is named', output)
