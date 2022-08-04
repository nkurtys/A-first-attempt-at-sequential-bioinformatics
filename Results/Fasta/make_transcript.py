def get_exons_from_file(file_name):
    """
    From generated file returns a list containing all genes with their respective exons and introns
    :param file_name
    :return genome
    """
    f = open(file_name, "r")
    f1 = f.read()
    genome = []
    exons = []
    gene = []
    start_end = []
    word = ''
    count_tab = 0
    count_com = 0
    for letter in f1:
        if count_tab == 0:  # gene annotation
            if letter == '\t':
                count_tab += 1
                count_com = 0
            elif count_com >= 3:
                continue
            elif letter == ',':
                gene.append(word)
                word = ''
                count_com += 1
            else:
                word = word + letter

        elif count_tab == 1:  # transcript annotation
            if letter == '\t':
                count_tab += 1
            elif letter == '|':
                gene.append(start_end)
                count_com = 0
                start_end = []
                word = ''
            elif count_com > 3:
                continue
            elif letter == ',':
                if count_com == 0:
                    count_com = count_com + 1
                else:
                    start_end.append(word)
                    word = ''
                    count_com = count_com + 1

            elif count_com < 1:
                continue
            else:
                word = word + letter

        elif count_tab >= 2:  # exon annotation
            if letter == '\n':
                genome.append(gene)
                count_tab = 0
                count_com = 0
                exons = []
                gene = []
                word = ''

            elif letter == ')':
                word = word + letter
                exons.append(word)
                word = ''
            elif letter == ']':
                gene.append(exons)
                exons = []
            elif letter == '[' or letter == ',':
                continue
            else:
                word = word + letter
        else:
            continue
    f.close()
    return genome
