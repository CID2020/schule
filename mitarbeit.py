import re
import csv
from os.path import exists
import os
path1='/home/ll/Dropbox/physik/'
for k1 in range(30):
  nl=[] #namenlist
  volln=path1+'v'+str(k1)+'.txt'
  if exists(volln):
    with open (volln,'r') as f:
      text1=f.read()
    with open(path1+'k9') as csvDataFile:
      csvReader = csv.reader(csvDataFile)
      for row in csvReader:
        p1=text1.count(row[0])
        m1=text1.count(row[0]+'-')
        mal1=text1.count(row[0]+'*')
        dur1=text1.count(row[0]+'/')
        text1=text1.replace(row[0],'') #remove the name
        nl.append([row[0],int(row[1])+p1-m1*2+mal1*2-dur1*2])
    klam1 = re.findall(r'\(.*?\)', text1)
    for n1 in klam1:
      print(n1)
      if not re.search('[a-zA-Z]', n1):
        print('replaced')
        text1=text1.replace(n1,'')
    #text1 = re.sub('[+-*]', '', text1)
    with open (volln,'w') as f:
      f.write(text1)
    os.remove(path1+'k9')
    with open(path1+'k9', 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      for n1 in nl:
        writer.writerow(n1)