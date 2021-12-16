# LEADING 2021, Drexel University and Smithsonian Libraries  

## Enhancing the museum data ecosystem through linking research publications to museum systems  

Extract textual entities from Smithsonian publication PDF files and identify patterns among specimens, taxonomic names, localities, and other entities that can enable linking to museum systems.  

There are two separate parts to this project: Using Named Entity Recognition (NER) to extract museum specimen numbers from text, and separating texts into their correct respective Smithsonian museums. Files to attempt the first part are in the folder "ner," and the second in "sorting."

### Subfolders in folder "files"

1. cURL/ contains batch files with cURL statements to pull down PMC article information (step 2, sorting)
2. targz/ contains .tar.gz files pulled down in step one
3. pmc_oa/ contains contents of .tar.gz files after opening up using open.py (step 3, sorting)
4. abstracts/ contains abstracts extracted from .nxml files by abstracts.py (step 4, sorting)
5. remove_HTML/ contains abstracts after first preprocessing step, removing the HTML tags using remove_html.py (step 5, sorting)
6. preprocessing/ contains abstracts that were further preprocessed using preprocessing.py (step 6, sorting)
7. abstracts.csv is all of the abstracts in "preprocessing" put into a CSV together, where each abstract is a line in the CSV (step 7, sorting)
8. body-text/ contains just the body of text extracted from the .nxml files, with HTML tags removed, using the program body.py from the ner folder.
