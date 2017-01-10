#python-2.7.9
#biopython-1.66

import sys
from Bio import SeqIO

wanted=set()

for i in open(sys.argv[1],"r"): # select NLR-Parser output.mast.txt file
    i=i.split("\t")
    wanted.add(str(i[0]))

for record in SeqIO.parse(open(sys.argv[2]),'fasta'): # Select the FASTA file containing the sequences analyzed with the NLR-Parser
    if record.id in wanted:
        print(">"+record.description)
        print(record.seq)
    else:
        pass
