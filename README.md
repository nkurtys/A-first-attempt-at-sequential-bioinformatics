#### README ####


## Introduction

The following project was created in the context of a four week course in sequential bioinformatics.
The goal was to retrieve genomic annotation from the human genome GTF file, find all
intron and exons positions and then "frankenstein" them together to the respective transcript.
Afterwards the idea was to first align those created transcripts to the original ones and then
align the paralogous transcripts. These MSAs were then saved in a multi FASTA file so they can then be
visualized. Python itself does not support a package that would allow doing that inside the IDE.

The packages used are PyEnsembl, Biopython and scikit-bio.
[PyEnsembl](https://github.com/openvax/pyensembl) is a Python interface to ensembl reference genome metadata 
such as exons and transcripts PyEnsembl downloads GTF and FASTA files from the Ensembl FTP server and loads them into a local
database. The [Biopython Project](https://biopython.org) is an international association of developers of freely available
Python tools for computational molecular biology and offers a FASTA file parser. 
[Scikit-bio](http://scikit-bio.org) is an python package providing data structures and algorithms for bioinformatics
including alignment algorithms.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed packages.

A minimum python version of 3.8 is recommended and can be downloaded from http://www.python.org/

```bash
pip install pyensembl
pip install biopython
pip install scikit-bio 
```

Dowload the GRCh38.98 Human Genome gtf file into the **Result** Directory.
Download all 24 chromosome FASTA files and the mitochondrial FASTA file into the **Result** Directory. All files are available  on http://www.ensembl.org

## Usage

```python
from Retrieve_Annotation.Data.get_data import return_data
from data_to_file import data_to_file
from data_to_sequence import get_seq
from Alignments.do_alignment import align_para_transcripts
from data_to_multiFasta import aligned_multiFasta_for

if __name__ == '__main__':
    data = return_data()                        
    data_to_file(data)                       
    sequences = get_seq('data_file.txt')
    align_para_transcripts(sequences, True)
    aligned_multiFasta_for("TSPAN6")
```


## Methods

The code is structured depending on the kind of data being retrieved.

Important to add is that all functions asking for a file_name ask for the data_file.txt created by the data_to_file function.
It is not compatible with any other file. The reason is that the purpose of the file is to make repeated running of the code
easier.
The way this file is structured is as following:

	gene_name, chromosome, strand, start_pos, end_pos, lenght	transcript_name, start_pos, end_pos, lenght|...other transcripts|	[(exon_start, exon_end), ...other exons][...other exons]

_Retrieve_Annotation.Data.get_data._**return_data**():

        Given the path to the gtf file "Homo_sapiens.GRCh38.98.gtf.gz", this function wil index the
        file and return the data the file holds with the help of the pyensembl package Genome.

_Retrieve_Annotation.Protein_Coding_Genes.create_pcg_file._**pcg_to_file**(_gene, file_):

        Given a pyensembl gene object and a reference to a file, this function retrieves all needed 
        information from the gene and writes it into the given file.


_Retrieve_Annotation.Transcripts.create_transcripts_file._**transcript_to_file**(_gene, file_):

        Given a pyensembl gene object and a reference to a file, this function retrieves all needed 
        information about the transcripts of the gene and writes it into the given file. 
        This function returns a list of all transcripts of the given gene.

_Retrieve_Annotation.Exons.create_exon_file._**exons_to_file**(_list_of_transcript, file_)
        
        Given a list of pyensembl transcript objects and a reference to a file, this function 
        writes the start and end position of exons  and introns of each transcript sorted by start position of each slice. 

_Fasta.make_transcript._**get_exons_from_file**(_file_name_):

        Parses the given file, which was created by the functions of 
        the Retrieve_Annotation Folder, into a format which can be 
        then used by by the functions in the do_fasta_things file.
        
_Fasta.do_fasta_things._**do_fasta**(_genome_):

        Returns a list containing all exons and introns from the transcripts
        contained in genome.

_Alignments.create_Fasta_alignment._**get_alignment**(_sequences, gene_name_):

        Calls align for each "gene package" in the sequence list.

_Alignments.create_Fasta_alignment._**align**(_seq, number_):

        Aligns the sequences stored in the list and adjust their lenghts so they can be
        written into an alignment-type file ("fasta" or "phylip"). It is set to phylip
        to make the alignment easier to see in the file.

_Alignments.do_alignment._**align_para_transcripts**(_sequences, align_fasta=False_):

        Saves the DNA Sequences stored in _sequences_ in a seperate list and calls
        align if no further 
        parameter is given. Else the whole "transcript package" is stored in the new list and 
        align_to_fasta is called.

_Alignments.do_alignment._**align_to_fasta**(_seq_):

        Aligns the given Sequences to the original Sequences retrieved from the respective
        fasta files. Only for testing purposes.


_Alignments.do_alignment._**align**(_seq, number_):

        Aligns the paralogous transcripts and prints them out to the terminal.

_Retrieve_Annotation.data_to_file._**data_to_file**(_data_):

        Opens "data_file.txt" and parses the information from data into the file.

_Retrieve_Annotation.data_to_multiFasta._**aligned_multiFasta_for**(_gene_name_):

        Creates an aligned multi FASTA file for the given gene_name with the 
        help of "data_file.txt".

_Retrieve_Annotation.data_to_sequence._**get_seq**(_file_name_):

        Parses the gene information stored in file_name (data_file.txt) and returns it.
        

## Discussion

This project is able to succesfully retrieve, filter and rebuild genomic information and sequences.
The greatest difficulty was parsing from and to different file types as well as finding an efficent 
datastructure to store all the needed information. In my code I have chosen a simple matrix containing 
information in a specific order, which allowed me to acces information fast through recursive functions. 
In retrospect I think I should have choosen a more OOP oriented approach and use an object instead of a 
collection of lists. Nonetheless the code processes the information fast and efficiently so I did not 
see an urgent need to adjust my code.
