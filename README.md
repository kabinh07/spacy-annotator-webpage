# spacy-annotator-webpage

## Upload a dataframe
- Upload a `json` file with a list of data. Every element of that list must have 3 keys, **sentence**, **words**, **lemmas**. For example,
```
[
  {
    "sentence": "আমার নাম কাবিন",
    "words": ["আমার", "নাম", "কাবিন"],
    "lemmas": ["আমার", "নাম", "কাবিন"],
  },
  {
    "sentence": "আমার দেশকে ভালবাসি",
    "words": ["আমার", "দেশকে", "ভালবাসি"],
    "lemmas": ["আমার", "দেশ", "ভালবাস"],
  }, 
]
```
- After annotation is completed, you can click `save annotations` and it will download another json file.
