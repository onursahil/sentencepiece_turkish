# Turkish Sentencepiece Tokenizer

Sentencepiece tokenizer trained with tr-wiki data

# Train

- python src/download-wiki-extract.py
- bash wiki-preprocessing.sh
- python train-sentencepiece.py

# Output

- /model_vocab/wiki-tr.model
- /model_vocab/wiki-tr.vocab