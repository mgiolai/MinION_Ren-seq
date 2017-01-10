#python-2.7.9

import re
import string
import sys

file=open((sys.argv[1]), "r") # define BLASTN output.blast.txt output

query_contigs=set()
subject_contigs=set()

query_contigs_all=set()
subject_contigs_all=set()

besthit = set()

#outfile = open("blast-analysis.txt", "w+")

#"qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen"#


print("query"+"\t"+"qlength"+"\t"+"subject"+"\t"+"sublength"+"\t"+"p-ident"+"\t"+"align-length"+"\t"+"qstart"+"\t"+"qend"+"\t"+"substart"+"\t"+"subend"+"\t"+"eval")

for i in file:
      i = i.replace("\n","").split("\t")
      if i[0] not in besthit and float(i[10]) == 0:
            print(i[0] +"\t"+ i[12] +"\t"+ i[1]+"\t"+ i[13] +"\t"+ i[2] +"\t"+ i[3]+"\t"+ i[6]+"\t"+ i[7]+"\t"+ i[8] +"\t"+ i[9] +"\t"+ i[10])
            besthit.add(str(i[0]))
      else:
            pass
file.close()

