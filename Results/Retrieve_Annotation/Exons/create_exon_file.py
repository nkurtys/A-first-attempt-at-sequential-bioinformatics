def exons_to_file(list_of_transcript: [], file):
    """
    Parses exon information to file
    :param list_of_transcript
    :param file
    """
    for k in list_of_transcript:  # k - transcript object
        slices = []
        intron_start = 0
        intron_end = 0
        exon_list = k.exon_intervals
        exon_list = sorted(exon_list, key=lambda k: k[0])       # sort list by base start so exons and introns alternate
        print(exon_list)
        for x in range(len(exon_list)):
            slices.append(exon_list[x])
            if x == (len(exon_list) - 1):
                intron_start = exon_list[x][1] + 1
                intron_end = k.end
                continue
            else:
                intron_start = exon_list[x][1] + 1
                intron_end = exon_list[x + 1][0] - 1
            slices.append((intron_start, intron_end))

        file.write(str(slices))
