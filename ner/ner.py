import spacy, os

nlp = spacy.load("./grouped_model")

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\body-text'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        # To make sure it's doing something
        with open(filepath, encoding="utf-8") as f:
            contents = f.read()
            doc = nlp(contents)
            for ent in doc.ents:
                print(ent.text, ent.label_)
