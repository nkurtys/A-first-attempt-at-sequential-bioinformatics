from data_to_sequence import get_seq
from Alignments.create_fasta_alignment import get_alignment


def aligned_multiFasta_for(gene_name: str):
    """
    Aligns sequences of given gene name
    :param gene_name
    """
    sequences = get_seq('data_file.txt')
    get_alignment(sequences, gene_name)


