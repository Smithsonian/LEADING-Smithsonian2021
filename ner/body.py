# For extracting abstracts out of PMC .nxml files
# This strategy is necessary because these files were made for the web, and have HTML tags in them
# Without this "tostring" function, it will return no text because it parses HTML tags as XML tags, and will say "abstract" is an empty tag

# Loop over files from https://newbedev.com/how-to-iterate-over-files-in-a-given-directory
# XML stuff from https://stackoverflow.com/questions/11122397/how-do-i-get-the-whole-content-between-two-xml-tags-in-python
# File writing loop from https://stackoverflow.com/questions/12560600/creating-a-new-file-filename-contains-loop-variable-python

import os
from  lxml.etree import parse, tostring
from bs4 import BeautifulSoup

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\pmc_oa'):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".nxml"):
            print (filepath)
            # To make sure it's doing something

            doc = parse(filepath)
            if doc.xpath('//body'):
                #This way, if there is no abstract tag it will just continue to loop
                element = doc.xpath('//body')[0]
                element = str(tostring(element))
                cleantext = BeautifulSoup(element, "html.parser").text
                #print(tostring(element))
                f = open("body-text/" + str(filename) + ".txt", "a", encoding="utf-8")
                # ^ This works as long as "body-text" directory already exists in target folder
                f.write(cleantext)
                f.close()

            
