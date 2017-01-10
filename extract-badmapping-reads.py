#python-2.7.9
#biopython-1.66

import sys
from Bio import SeqIO

#1. specify FASTA file with reads
#2. specify BLASTN output.blast.txt file

mapped_reads = []

counter=0

###############
#Determine all reads that don't map
###############

for i in open((sys.argv[2]),"r"):
        i=i.replace("\n","").split("\t")
        mapped_reads.append(i[0])

for record in SeqIO.parse(open(sys.argv[1]),'fasta'):
        if record.id in mapped_reads:
                print(str(">")+record.id)
                print(record.seq)




