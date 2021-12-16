# Step 1: Import each file
# Step 2: Create dictionary where file is the main key, and further KVPs are term-count pairs
# Step 3: Use num-py to convert to matrix

# Step 4 (next week): tf-idf calcuation and transformation

import nltk
import numpy as np
import os

# Took this flattening code from http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

# Code adapted from https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/
# This blog post just scraped some stuff from wikipedia, but I want to use my abstract files

wordfreq = {}
allwords = []

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\preprocessing\test'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        # To make sure it's doing something
        with open(filepath, encoding="utf-8") as f:
            contents = f.read()
            allwords.append(str(contents))
            # probably a clunky way of doing it, but this gives us the set of every word in our corpus
            tokens = nltk.word_tokenize(contents)
            for token in tokens:
                if token not in wordfreq.keys():
                    wordfreq[token] = 1
                else: 
                    wordfreq[token] += 1

allwords = flatten(allwords)
allwords = str(allwords)
allwords = allwords.split(' ')
allwords = set(allwords)
# ...I think that worked!

abstract_vectors = []

for subdir, dirs, files in os.walk(r'C:\Users\willi\Documents\LEADING\LEADING-Smithsonian-2021\files\preprocessing\test'):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)
        # To make sure it's doing something
        with open(filepath, encoding="utf-8") as f:
            contents = f.read()
            abstract_tokens = nltk.word_tokenize(contents)
            ab_vec = []
            for token in allwords:
                # Just realized this will only ever give a 1 or 0, not a count
                if token in abstract_tokens:
                    ab_vec.append(1)
                else:
                    ab_vec.append(0)
            abstract_vectors.append(ab_vec)

abstract_vectors = np.asarray(abstract_vectors)
# This changes the dictionary into a matrix! Easy
print(abstract_vectors)
# I think it works!! Def got a big array anyways...it won't give me the whole thing though :/