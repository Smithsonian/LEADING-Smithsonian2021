# Named Entity Recognition for museum specimens

## Files

body.py extracts the body of the selected PMC files and cleans it slightly. These files are stored in ../files/body-text.  
ner.py uses the models to pull out named entities from the body files.

## Models

Both models were created using the same dataset: a set of sentences that all contain some string related to the Smithsonian museum (USNM, NMNH, United States National Museum, National Museum of Natural History, etc.). The two models both label all museum specimens (eg., USNM 1495, YPM 10655, NMNM 703), from any museum, as MUSEUMSPECIMEN. The two models handle one common situation slightly differently. When many specimens are listed in one paper, they are sometimes listed with the museum acronym just once, and a list of numbers following:

```
USNM 1234, 1236, 1246, 1587, 1577, 2001, 2022...
```

When this happens, the "grouped model" would wrap all of those up as a single specimen, starting with the acronym and ending with the last number. "Split model" would make every number a separate specimen. There are pros and cons to each method, but both work well to capture museum specimens in most scenarios.