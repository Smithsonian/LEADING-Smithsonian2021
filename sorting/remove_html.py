# PMC .nxml files contain HTML tags within the XML, since they are made to describe web content. Since the HTML tags do not add semantic meaning to the text, this program will remove them.

# BeautifulSoup lines from https://stackoverflow.com/a/12982689
# File reading with statement from https://www.pythontutorial.net/python-basics/python-read-text-file/
# File writing statements from https://newbedev.com/how-to-iterate-over-files-in-a-given-directory

import os
from bs4 import BeautifulSoup

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\abstracts'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        # To make sure it's doing something
        with open(filepath) as f:
            contents = f.read()
            cleantext = BeautifulSoup(contents, "html.parser").text
            #print(cleantext)
            g = open("remove_HTML/" + str(filename), "a", encoding="utf-8")
            # Only works if removes_HTML/ directory is already in current folder
            g.write(str(cleantext))
            g.close


# Below was an earlier attempt, but I couldn't get the files in a new directory the way I wanted using os.scandir(). I'll probably try something like this again later, since it's a little simpler and os.walk wasn't necessary in this case.

#directory = r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\abstracts\test'
#for entry in os.scandir(directory):
#    print(entry.path)
    # To make sure it's doing something
#    with open(entry.path) as f:
#        contents = f.read()
#        cleantext = BeautifulSoup(contents, "html.parser").text
#        print(cleantext)
#        g = open("remove_HTML/" + str(entry), "a", encoding="utf-8")
#        g.write(str(cleantext))
#        g.close

    #f = open("remove_HTML/" + str(entry), "a", encoding="utf-8")
    #f.write(str(clean))
    #f.close()