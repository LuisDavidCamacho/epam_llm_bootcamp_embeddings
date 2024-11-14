# epam_llm_bootcamp_embeddings
Small toy code for checking embeddings

This is a small script that shows in a simple way the use of 2 specific embeddings. 
Bert embeddings and Word2Vec embeedings.
This ezample provides a way to check word or sentence embeddings and embedded space comparisons.
From this example it is possible to extend as exercise to embedding clustering and groups.

To make this project run follow these steps:

1. create in the project root a folder called model
2. create under model folder a new folder called bin
3. download word2vec model from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g
4. extract bin file to model bin
5. rename file to word2vec.bin
6. use poetry install command to install depndencies. If poetry fails you can just use pip to install listed libraries

To execute the example app just go to the project root and run:

$ python main.py
