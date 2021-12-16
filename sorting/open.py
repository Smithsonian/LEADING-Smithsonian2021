# For extracting out of tar.gz files

# from https://www.geeksforgeeks.org/how-to-uncompress-a-tar-gz-file-using-python/
# importing the "tarfile" module
import tarfile

# Looping over files; from https://newbedev.com/how-to-iterate-over-files-in-a-given-directory
import os

directory = r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\targz'
for entry in os.scandir(directory):
    file = tarfile.open(entry)
    file.extractall('./pmc_oa')
    file.close()

  
# open file; gfg.tar.gz is their example file
# file = tarfile.open('gfg.tar.gz')

# print file names; this way you can see where it is
# print(file.getnames())

# extracting file
# file.extractall('./pmc_oa')
  
# file.close()