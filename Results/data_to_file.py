from Retrieve_Annotation.Protein_Coding_Genes.create_pcg_file import gene_to_file
from Retrieve_Annotation.Transcripts.create_transcripts_file import transcript_to_file
from Retrieve_Annotation.Exons.create_exon_file import exons_to_file


def data_to_file(data):
    """
    Parses data information to file. Uncomment second if statement to
    test function on less data points.
    :param data
    """
    f = open('data_file.txt', "w+")
    genes = data.genes()
    count = 0
    for i in genes:
        if i.biotype == "protein_coding":
            gene_to_file(i, f)
            f.write('\t')
            tc = transcript_to_file(i, f)
            f.write('\t')
            exons_to_file(tc, f)
            count += 1
            f.write('\n')
        if count == 1:
            break
    f.close()
