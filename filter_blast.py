#This script removes contaminants from the blast output based on the plant genus list. 
#The All_plant_genus_list_updated.txt file can be replaced with any list of genuses
###usage: python filter_blast.py [merged blast output] All_plant_genus_list.txt > genome.best.hits.contamination.blast

import sys
f1=open(sys.argv[1],'r') 
f2=open(sys.argv[2],'r') 
genus=set()
for line in f2:
    genus.add(line.rstrip())
for line in f1:
    ll = line.split('\t')
    thisgenus = ll[13].split()[0]
    if 'PREDICTED' in thisgenus:
        thisgenus = ll[13].split()[1]
    if thisgenus in genus:
       continue
    else:
       print line.replace('\n','')
