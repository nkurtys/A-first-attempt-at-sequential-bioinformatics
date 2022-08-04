from pyensembl.genome import Genome


def return_data():
    """
    Parse GTF and construct database of genomic features
    Enter gtf path, add r at the start to signal raw string
    :return data
    """
    data = Genome(
        reference_name="GRCh38",
        annotation_name="homo_sapiens",
        gtf_path_or_url=r"..\Homo_sapiens.GRCh38.98.gtf.gz")
    data.index()
    return data
