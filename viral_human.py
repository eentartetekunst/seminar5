

import gzip
from glob import glob
from Bio.Seq import Seq

def kmer_dict(k, genome):
    positions = dict()
    for i in range(len(genome) - k + 1):
        k_cur = genome[i: i + k]
        if k_cur not in positions.keys():
            positions[k_cur] = [i]
        else:
            positions[k_cur].append(i)
    return positions

def range_mers(x, y, genome): # будет писать в список х-у меры
    kmers_set = set()
    for n in range(x, y):
        cov_kmer = kmer_dict(n, genome)
        kmers_set = kmers_set | set(cov_kmer.keys())
    return kmers_set

covids = glob('covids/*.txt') # returns list with paths to files on the folder

all_kmers_set = set()

for covids_file in covids: # проходим по каждому текстовому файлу
    with open(covids_file, 'rt') as f:
        covid_genome = f.readlines()
        full_genome = ''  # сюда запишем большой строкой содержимое
        for line in covid_genome:
            if '>' not in line:
                full_genome += line.replace('N', '').replace('\n', '').replace('*', '') # чистый геном  в строке
        file_kmers = range_mers(8, 13, full_genome) # 8-12 меры данного файла
        all_kmers_set = all_kmers_set | file_kmers # пишем все кмеры всех файлов в один сет


with gzip.open('GRCh38_latest_genomic.fna.gz', 'rt') as f1:
    complete_genome = f1.readlines()

human_genome = ''
for line in complete_genome:
    if '>' not in line:
        human_genome += line.replace('N', '').replace('\n', '').upper().replace('S', '').replace('K', '').replace('R', '').replace('W', '').replace('B', '')

human_aa = translate(human_genome)
human_kmers = range_mers(8, 13, human_aa)
all_human_kmers_set = all_human_kmers_set | human_kmers


viral_in_human = all_kmers_set & all_human_kmers_set
print(viral_in_human)