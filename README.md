# trgn_assignment3b
## extract_phonenum.py
### usage: 
You can input "python3 extract_phonenum.py mytextfile.txt" in command line.
### description:
A lot of phone numbers should be put into the file mytextfile.txt, you should input command line "python3 extract_phonenum. Py mytextfile.txt" in the terminal , this program can return the standard format of the phone numbers.
### limit:
This function can be implemented only when the input phone number contains "-", like "+44-20-7183-8750".
### known issues：
The phone number cannot be extracted if there are more than 4digits between "-".

## ensg2hugo.py
### usage:
"wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz"
at first, users should use this command to download this gtf file, then use comman gunzip this file.
then, input the command "python3 ensg2hugo.py [-f][0-9] [file]", the number following '-f' means the order of the colume contains gene id in a specific file including gene information.
### description:
this program can replace gene_id with the hugo name of the gene in a specific file. 
### limit:
users should download the Homo_sapiens.GRCh37.75.gtf file instead of Homo_sapiens.GRCh38.75.gtf since I edited this program based on the gene_id without decimal points.
### known issues:
A reasonable output is not effectively returned if the only argument entered by the user is a filename.

## histogram.py
### usage:
This program produces png picture of histograms of specified columns in a file.
### description:
input "histogram.py -f4 expression_analysis.csv" in terminal
### limit:
this program could make pictures for only one colume in a file. 
### known issues:
I edited this program based on csv file, this may not be work if a the input document is other types of file.
