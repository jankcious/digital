import time
import os
import zipfile


#EDIT THIS FILE PATH TO CUSTOMIZE
#filepath = 'c://AUTOBOT - RCAs/Reports'
filepath = 'C://users/jason.becker/documents/ipython notebooks/ipython/data'

#Extracts all Zip Files in the Folder specified above
print('Extracting excel files from all .Zip Export (If Applicable) ...')
filelist = [ f for f in os.listdir(filepath) if f.endswith(".zip") ]
for f in filelist:
    print(f)
    os.chdir(filepath)
    zfile = zipfile.ZipFile(f)
    zfile.extractall(filepath)
print('All Files have been extracted from Zip Files...')