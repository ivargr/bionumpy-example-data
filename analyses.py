import bionumpy as bnp
import numpy as np


def scan_file(file_name):
    pass


def count_gs_in_fastq(file_name):
    f = bnp.open(file_name)
    n = 0
    for chunk in f.read_chunks(min_chunk_size=10000000):
        n += np.sum(chunk.sequence == "G")

