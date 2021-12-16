#https://stackoverflow.com/questions/60926489/#how-to-merge-multiple-text-files-into-one-csv-file-in-python

import os
import pandas as pd

csvout_lst = []


for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\preprocessing'):
    for filename in sorted(files):
        filepath = subdir + os.sep + filename
        print(filepath)
        data = pd.read_csv(filepath, sep=':', index_col=0, header=None)
        csvout_lst.append(data)

pd.concat(csvout_lst).to_csv('abstracts.csv')

# This works!
# First line was just '0' for some reason so I deleted that, then moved CSV to "files" folder