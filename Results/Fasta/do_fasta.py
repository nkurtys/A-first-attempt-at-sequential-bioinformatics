import gzip
from Bio import SeqIO
from Bio.Seq import Seq


def open_fasta(start_end: [], config: str, slices, strand: str):
    """
    Opens chromosome fasta file and saves sequence
    :param start_end
    :param config
    :param slices
    :param strand
    :return slice_result
    """
    with gzip.open(
            r"..\Homo_sapiens.GRCh38.dna.chromosome." + config + ".fa.gz",
            "rt") as file:

        print("File opened!")

        record = SeqIO.parse(file, "fasta").__next__()  # works like a for loop
        slice_result = [config, start_end, strand, Seq("")]

        # slice the sequence according to the given base positions
        for x in range(len(slices)):
            var = record.seq[(((slices[x])[0]) - 1):((slices[x])[1])]
            if strand == '-':
                var = var.complement()
            slice_result[3] += var
        return slice_result


def do_fasta(genome: []):
    """
    Parses the base positions of exons and intron and finds their sequence in the respective fasta file
    :param genome
    :return gene_sequences
    """
    gene_sequences = []
    for x in genome:  # x = one gene
        name = x[0]
        chromosome = x[1]
        strand = x[2]

        transcripts = int((len(x) - 3) / 2)
        gene_sequences.append(name)
        gene_sequences.append(transcripts)
        for i in range((3 + transcripts), (2 * transcripts + 3)):  # i = a transcript

            start_end = x[i - transcripts]
            slices = []  # exons and introns for whole gene x
            for j in x[i]:  # j = an exon/intron
                numbers = ''
                pre_start = ''
                pre_end = ''
                for letter in j:
                    if letter == ' ':
                        pre_start += numbers
                        numbers = ''
                    elif letter == ')':
                        pre_end += numbers
                        numbers = ''
                    elif letter == '(':
                        continue
                    else:
                        numbers += letter

                exon = (int(pre_start), int(pre_end))
                slices.append(exon)

            gene_sequences.append(open_fasta(start_end, chromosome, slices,
                                             strand))  # not in right order rn - adjust for strand from the start maybe
            print("Got all slices for 1 transcript!")
        print("Got all Sequences for 1 gene")
    print("Got all Sequences!")
    return gene_sequences  # [name, transcript_amount, [config, start_end, strand, Seq("")]...]
