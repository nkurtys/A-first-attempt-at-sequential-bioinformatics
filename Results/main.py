from Retrieve_Annotation.Data.get_data import return_data
from data_to_file import data_to_file
from data_to_sequence import get_seq
from Alignments.do_alignment import align_para_transcripts
from data_to_multiFasta import aligned_multiFasta_for
from skbio import TabularMSA, DNA
from skbio.alignment import local_pairwise_align_ssw



if __name__ == '__main__':
    data = return_data()
    data_to_file(data)         ## index file and create new file, only needs to run one time

    sequences = get_seq('data_file.txt')
    #align_para_transcripts(sequences, True)
    aligned_multiFasta_for("TSPAN6")




