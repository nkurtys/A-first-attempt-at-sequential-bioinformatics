from skbio.alignment import local_pairwise_align_ssw
from Bio import SeqIO
import gzip
from skbio import TabularMSA, DNA


def align(target, query):
    """
    Aligns sequences with the Smith-Waterman algorithm
    :param target : Bio.Seq("...")
    :param query : Bio.Seq("...")
    """

    alignment, score, start_end_positions = local_pairwise_align_ssw(
        DNA(str(target)),
        DNA(str(query))
    )

    print(alignment)
    print(start_end_positions)



def align2(seq: [], number: int):
    """
    Aligns sequences with the Smith-Waterman algorithm
    :param seq
    :param number
    """
    for i in range(number - 1):
        alignment, score, start_end_positions = local_pairwise_align_ssw(
            DNA(str(seq[0])),
            DNA(str(seq[i + 1]))
        )

        print(alignment)
        print(start_end_positions)


def align_to_fasta(seq: []):
    """
    Aligns created Transcripts to the original Transcript retrieved from the FASTA file
    :param seq : [gene_name, number_of_transcripts [chromosome, start_end_pos, strand, Bio.Seq("..")][...]]
    """
    for i in seq:
        with gzip.open(
                r"..\Homo_sapiens.GRCh38.dna.chromosome." + i[0] + ".fa.gz", "rt") as file:
            record = SeqIO.parse(file, "fasta").__next__()

            seqs = []
            if i[2] == '-':
                seqs.append(DNA(str(record.seq[int(i[1][0]) - 1:int(i[1][1])].complement())))  # FASTA DNA
            else:
                seqs.append(DNA(str(record.seq[int(i[1][0]) - 1:int(i[1][1])])))  # FASTA DNA

            seqs.append(DNA(str(i[3])))  # created DNA

            msa = TabularMSA(seqs)
            print(msa)


#
def align_para_transcripts(sequences: [], align_fasta=False):
    """
    Recursively creates the transcript and then aligns it either to paralogous transcripts or
    the original transcript.
    :param sequences
    :param align_fasta
    :return sequences
    """
    print(sequences)
    if len(sequences) == 0:
        return sequences
    else:
        start = 2
        trans = sequences[1]
        seqs = []

        if not align_fasta:
            for i in sequences[start:trans + 2]:
                seqs.append(i[3])
            align2(seqs, trans)
            align_para_transcripts(sequences[trans + 2:])
        else:
            for i in sequences[start:trans + 2]:
                seqs.append(i)
            align_to_fasta(seqs)
            align_para_transcripts(sequences[trans + 2:])