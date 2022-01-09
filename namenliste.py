import numpy as np
import pandas as pd
import os
dir0='/home/ll/Downloads/'
dir1='/home/ll/Dropbox/schule/namenlist/'
list_of_files = []
for root, dirs, files in os.walk(dir0):
	for file in files:
		if file.endswith(".txt") and 'save-users' in file:
			list_of_files.append(file)
#latest_file = max(list_of_files, key=os.path.getctime)
for ind1, name1 in enumerate(list_of_files):
    print(ind1,name1)
nummer=input('Welche Datei: ')
file1=list_of_files[int(nummer)]
n1=open(dir0+file1,'r')
nlist1=n1.read().split('\n')
endelist=nlist1.index('  ')
nlist=nlist1[endelist+3:]
vollliste=[]
for nummer in [9,10,11]: #save all 3 namenlist
    vollliste=open(dir1+'vollliste'+str(nummer)).read().split('\n')
    vollliste.pop() #remove the end empty element
    if (nlist[0] in vollliste):
        klasse=nummer
        break
abwesen=''
abwesenIndex=''
for i in range(len(vollliste)):
    if vollliste[i] in nlist:
        abwesenIndex=abwesenIndex+'O\n'
    else:
        abwesenIndex=abwesenIndex+'XX\n'
        abwesen=abwesen+vollliste[i]+'\n'
abwesenList=abwesenIndex.split('\n')
abwesenList.pop()
abwesenArr = np.array(abwesenList)

df1 = pd.read_excel(dir1+str(klasse)+'.xlsx',header=None) #reading file
array1=df1.to_numpy()
array2=np.hstack((array1, np.atleast_2d(abwesenArr).T))
df2 = pd.DataFrame (array2)
filepath = 'my_excel_file.xlsx'
df2.to_excel(dir1+str(klasse)+'.xlsx',header=False,index=False)
print(abwesen)
# with open(dir1+nummer+' index', 'w') as f:
#     f.write(abwesenIndex)
with open(dir1+file1+' Name', 'w') as f:
    f.write(abwesen)