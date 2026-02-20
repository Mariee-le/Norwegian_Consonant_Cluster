# Consonant Cluster Finder

A small Python script that uses NLTK and regex to identify and print consonant clusters consisting of exactly five consecutive consonants from the `Norwegian_Norsk-Nynorsk-Latin1` text in the UDHR corpus.

---

## What the Script Does

- Loads the `Norwegian_Norsk-Nynorsk-Latin1` file from the UDHR corpus via NLTK
- Uses regular expressions (regex)
- Identifies words containing exactly five consecutive consonants
- Prints those words

---

## Requirements

This project depends on:

```
nltk
regex
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python konsonantklynge.py
```

---

## Technical Details

- Language: Python 3
- Corpus: UDHR via NLTK
- Method: Regex pattern matching five consecutive consonants

---
