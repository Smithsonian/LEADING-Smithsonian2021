# Subject sorting algorithm

The python files in this folder make up an attempt to create a bag-of-words model using NLTK, which was intended to sort the abstracts of a set of PMC papers by topic.

## Steps

1. Find Open Access journal articles with Smithsonian authors; we are using a set of PMC articles
2. Pull down OA article info using cURL statements; this step is in hidden directory
3. PMC API gives us .tar.gz files. Extract info using [open.py file](./open.py).
4. Inside extracted folders, we want to pull information from .nxml files. Extract this using [abstracts.py](./abstracts.py).
5. Start preprocessing extracted text. To start, I want to remove HTML tags from the abstracts, which do not add meaning. I do this using [remove_html.py](./remove_html.py).
6. Further preprocessing. Each abstract started with the characters b' and ended with ', and some had n\ throughout. I removed these; put everything in lowercase; removed numbers, punctuation, and stopwords; and stemmed the remaining words. All of this happens using [preprocessing.py](./preprocessing.py).
7. Combine the abstracts into one CSV file, to make it easier to process, using [combine_csv.py](./combine_csv.py).
8. Create a tf-idf matrix. I attempted this with tf-idf.py and fmatrix_attempt.py.
