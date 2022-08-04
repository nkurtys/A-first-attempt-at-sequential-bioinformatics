def transcript_to_file(gene, file):
    """
    Parses transcript information to file and returns list containing transcripts
    :param gene
    :param file
    :return: tc_new
    """
    tc = gene.transcripts  # list of transcripts
    tc_new = []

    for j in tc:
        # filtering out long non coding RNA
        if j.biotype == "protein_coding":
            id = str(j.transcript_id)
            # biotype = str(j.biotype)
            name = str(j.transcript_name)
            start = str(j.start)
            end = str(j.end)
            lent = str(abs(j.end - j.start))
            tc_new.append(j)
            file.write(name + ',' + start + ',' + end + ',' + lent + ',' + id + '|')

    return tc_new
