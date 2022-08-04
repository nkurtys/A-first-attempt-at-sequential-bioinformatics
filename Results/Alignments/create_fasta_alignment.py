from skbio.alignment import StripedSmithWaterman
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO


def align(seq: [], number: int):
    """
    Creates multi fasta or phylip file for given sequence list
    :param seq : list of transcripts
    :param number : of transcripts
    """
    alignments = [SeqRecord(seq[0], id="query")]
    target_sequences = []
    for i in range(number - 1):
        target_sequences.append(str(seq[i + 1]))
    query_sequence = str(seq[0])
    query = StripedSmithWaterman(query_sequence)
    count = 0
    for target_sequence in target_sequences:
        alignment = query(target_sequence)

        ''' all sequences need to be the same lenght
            filling in gaps with "-"
        '''
        diff_begin = alignment.query_begin - alignment.target_begin
        gaps_begin = "-" * diff_begin
        diff_end = alignment.query_end - len(alignment.query_sequence)
        gaps_end = "-" * (abs(diff_end) - 1)

        target_seq = gaps_begin + alignment.aligned_target_sequence + gaps_end
        alignments.append(SeqRecord(Seq(target_seq), id=str(count)))
        count += 1

    align1 = MultipleSeqAlignment(alignments)
    AlignIO.write(align1, "alignment.fa", "fasta")       #adjust phylip to fasta to create multi fasta file


def get_alignment(sequences: [], gene_name):
    """
    Creates alignment for given gene.
    :param sequences
    :param gene_name
    """
    print(sequences)
    if len(sequences) == 0:
        print("gene not found")
    else:
        name = sequences[0]
        trans = sequences[1]
        start = 2
        seqs = []
        if name == gene_name:
            for i in sequences[start:trans + 2]:
                seqs.append(i[3])
            align(seqs, trans)
        else:
            get_alignment(sequences[trans + 2:], gene_name)
