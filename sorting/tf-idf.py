# Trying a different approach
# From https://medium.com/swlh/text-classification-using-the-bag-of-words-approach-with-nltk-and-scikit-learn-9a731e5c4e2f
import pandas as pd
dataset = pd.read_csv('abstracts.csv')
# abstracts.csv must be moved into same folder first

from sklearn.feature_extraction.text import CountVectorizer
matrix = CountVectorizer(max_features=1000)
# Only takes 1000 most common words
freq = matrix.fit_transform(dataset.Text)
# This works because I added a single column header called "Text"
# Got idea from https://stackoverflow.com/questions/44083683/countvectorizer-with-pandas-dataframe/44083903

print(freq.shape)
# Output: (302, 6725)
# After adding max_features: (302, 1000)