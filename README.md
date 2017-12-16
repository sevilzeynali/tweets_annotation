# Tweets annotation with MElt
This is a part of speech tagging of tweets with Melt for the tweets stocked in MongoDB database and it stocks them in mongoDB.
It uses [MElt](https://team.inria.fr/almanach/fr/melt/).
# Example of MElt 's part of sppech tagging
The format of MElt 's part of speech tagging is :
[token]/[part of speech tagging]/[probability]
For a tweet like " La batterie de mon téléphone meurt plus vite que des parents dans un Disney" you will have this output in MElt:
```
La/DET/0.999997596102  batterie/NC/0.998097404522 de/P/0.999682540908  mon/DET/0.819678627324 téléphone/NC/0.998192074148  meurt/V/0.998281963964 plus/ADV/0.997822241042  vite/ADV/0.8338042831 que/CS/0.954211330489  des/DET/0.976683310825 parents/NC/0.999859599512 dans/P/0.999868242281 un/DET/0.993384823012     Disney/NPP/0.924351672686
```
## Installing and requirements
You need Python >= 2.6 or >= 3.3
You should install MElt
You need pymongo
This program uses also melt_wrapper.py program for doing a connection between Melt and Python. 
### Melt_Wrapper.py
This program contains two functions : tagListOfTexts and tag.
tagListOfTexts takes as parameter a list of texts to tag. It groups them into a string from the \n and then it returns results.
tag function This takes as parameter a text that it transmits to MElt and returns the results of MElt in the form of a large list of list of dictionaries (in the sense of Python, i. e. associative arrays).A dictionary represents a token. A document is therefore a list of dictionaries. And a list of dictionary lists is therefore a list of tagged documents. These dictionaries will have as key, tags and  as values tagged elements. Such as this exemple:
```
[[{'token': 'Au', 'tag': 'P+D', 'probability': '0.90305676909', 'normalization':
''}, {'token': 'tel', 'tag': 'ADJ', 'probability': '0.976219163052',
'normalization': ''}, {'token': 'avec', 'tag': 'P', 'probability':
'0.99319435586', 'normalization': ''}, {'token': 'Stacy', 'tag': 'NPP',
'probability': '0.997467420283', 'normalization': ''}], [{'token': '@Alananas_',
'tag': 'NPP', 'probability': '', 'normalization': '_URL'}, {'token': 'a', 'tag':
'V', 'probability': '0.99946496138', 'normalization': ''}, {'token': 'mort',
'tag': 'VPP', 'probability': '0.605760338727', 'normalization': ''}, {'token':
'...', 'tag': 'PONCT', 'probability': '', 'normalization': ''}]]
```
## Preparing your data sets
You should have stocked your tweets in Mongodb database before using this program.
You can see one example of tweet stocked in mongoDB database:
```
{"language":"fr","tweet":"J'ai envie d les monter en l'air","user":291174411,"date":1403886807,"id":"482562363758243840"}
```
to have more information about this format you can see [my master memory](https://dumas.ccsd.cnrs.fr/dumas-01260379/document).
## How to use
You need just put your path to MongoDB in tweets_annotation_with_melt.py:
```
mongodb_path=""
```
and then run tweets_annotation_with_melt.py

