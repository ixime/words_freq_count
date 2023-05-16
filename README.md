# words_freq_count
Simple script to count words frequency in a text.  

In order to do so, we did the following steps:  
-  Separate the text into words
-  Convert all letters into lower letters
-  Get rid of not important words, like "the", "and", "I"
-  Do lemmatization to avoid counting as different words derivated words i.e. "food" and "foods"

---
Input: text in a txt file  
Output: word stems and its count in a csv file in the same directory as the input file  
---

## Installation

create an environment and install the dependencies  
```
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
./script.py <txt file>
```

Note: Don't forget to give execution permission to the script
