import re
import sys
import fileinput
ens2gene={} 
#establish a dictionary, the key is gene_id, the value is gene_name
args=sys.argv[1:]

if len(args)<1:
    print('arguments are needed')
    exit
if '-f' in args[0]:
    flag=int(args[0][-1])
    input_file_to_change=args[1]
else:
    flag=1
    input_file_to_change=args[0]
    #if there is no '-f' input, then we use the second colume in the file defaultly.  

with open("Homo_sapiens.GRCh37.75.gtf",'r') as file:
    for line in file:
        matches=re.findall('gene_id "(.*?)".*gene_name "(.*?)";',line)
        #find the contents from the gene_id to gene_name in eachline, put them in "matches"
        if matches:
            # matches[0][-1]is gene_id and matches[-1][-1] is gene_name
            ens2gene[matches[0][0]]=matches[-1][-1]
            
#print(',gene_id,gene_type,logFC,AveExpr')
for line in fileinput.input(input_file_to_change):
    geneid_key=re.findall('(E[^\.]+)',line)[0]
    arrays=re.split(',',line)
    if geneid_key in ens2gene:
        newline=re.sub(str(arrays[flag-1]),str(ens2gene[geneid_key]),line)
        print(str(newline))
        #if '-f4' means the forth colume in  file
        #replace the gene_id with the gene_name

#use open command to create a new file and store the file contents after changing.

