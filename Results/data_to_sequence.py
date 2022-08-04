from Fasta.do_fasta import do_fasta
from Fasta.make_transcript import get_exons_from_file


def get_seq(file_name):
    """
    Returns sequences from data_file.txt
    :param file_name:
    :return: sequences
    """
    genome = get_exons_from_file(file_name)
    print(genome)
    print("Genome sequenced!")
    sequences = do_fasta(genome)
    print("Process finished! Start printing!")
    #for x in sequences:
        #print(x)
    return sequences
