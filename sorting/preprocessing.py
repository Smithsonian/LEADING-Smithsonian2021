# Preprocessing text: Removing unwanted characters/punctuation, converting to lowercase, removing numbers, stemming/lemmatizing
# A lot of code from https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908
# This code is relatively slow, I think because of the addition of nltk

import os, re, string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\remove_HTML'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        # To make sure it's doing something
        with open(filepath, encoding="utf-8") as f:
            # I didn't have this issue in remove_html, but I ran into unicode endode errors with this loop, so added encoding here.
            contents = f.read()
            process = contents[2:-1]
            # Each abstract starts with b' and ends with ' and I want to remove these characters
            process = process.replace('\\n',' ')
            # Some abstracts include \n (line breaks) between words, which need to be removed. 
            # Replaced with a space to ensure that words are broken up. Two \ to "release" the slash
            # Code from https://stackoverflow.com/questions/9347419/python-strip-with-n
            process = process.lower()
            # Converts entire string to lowercase
            process = re.sub(r'\d+', '', process)
            # Removes numbers
            process = process.translate(str.maketrans("", "", string.punctuation))
            # Removes punctuation
            tokens = word_tokenize(process)
            # Tokenizing, important for next steps
            stop = [i for i in tokens if not i in stop_words]
            # Removes stopwords
            finalString = []
            # This next loop is the stemmer
            for token in stop:
                tokenFinal = token
                tokenFinal = stemmer.stem(token)
                finalString.append(tokenFinal)
            result = " ".join(finalString)
            #print(result)

            g = open("preprocessing/" + str(filename), "a", encoding="utf-8")
            # Only works if preprocessing/ directory is already in current folder
            g.write(str(result))
            g.close