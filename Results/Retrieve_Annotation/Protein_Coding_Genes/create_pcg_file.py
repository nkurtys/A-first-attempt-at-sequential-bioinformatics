
def gene_to_file(gene, file):
    """
    Parses gene information to file
    :param gene
    :param file
    """
    name = str(gene.gene_name)
    #id = str(gene.gene_id)
    contig = str(gene.contig)
    start = str(gene.start)
    end = str(gene.end)
    strand = str(gene.strand)
    length = str(gene.end - gene.start)

    file.write(name + ',' + contig + ',' + strand + ',' + start + ',' + end + ',' + length)
