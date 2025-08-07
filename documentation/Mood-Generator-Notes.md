---
title: Mood-Generator-Notes

---

# Notes

---
## Table of Contents
1. [Sentence Embedding](####Sentence Embedding)

## Concepts
- Word embeddings
- Sentence embeddings
- Semantic similarity
- Cosine similarity	
- Dimensionality
- Token/Keyword Extraction 
- Part-of-speech (POS) tagging
- Multimodal learning/embedding


---
### Sentence Embedding

Sample Code (from input_analysis.py):
```
# getting sentence transformers from hugging face
from sentence_transformers import SentenceTransformer

# creating the model and embedding user input
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
user_input = "I'm feeling a bit nostalgic and cozy today"
embedding = model.encode(user_input)

# printing output
print(embedding) 
```

- Sentence embedding is a vector that encapsulates the meaning of a sentence
  - It uses semantic relationships
    - Semantic similarity: how close two pieces of text are in meaning
    - We can see how similar two sentences are by comparing their vectors (We compare the angle between two vectors: Cosine similarity)
- We got the vector for this sentence embedding by using sentence transformers, with the model being from Hugging Face
  - This model (transformer) read the sentence and encoded it to a vector
  - The model does so using "internal attention layers"
  - This model can do so because of it's training on large datasets
- This is why the output of the print statement is:
```
[ 4.14486714e-02  3.56660150e-02  9.02098045e-02  6.97052181e-02
  9.25733224e-02  1.59684122e-02 -1.53333340e-02 -9.29813311e-02
  ...
  -6.48902059e-02  4.73906994e-02  2.72066481e-02  2.18377113e-02
  4.34231944e-02 -2.14139689e-02 -6.79030046e-02 -1.57295056e-02]
```
- Why did we run this code, and why would we want this output?
  - By doing this, we can get a vector for each user input
  - Then, we can use a similar set of steps to vectorize other text (like image descriptions)
  - We can then use semantic similarity to see how similar the text are! This will allow us to assess if an image is aligned with what the user wants
  - Additionally, we can vectorize an image and use cosine similarity to compare them 
    -  Multimodal learning
    - A value close to 1 means they're semantically similar.
    - Tools that can be used to work with this include CLIP, BLIP / GIT, OpenAI API (DALL·E/CLIP)
  - That's why this embedding, although it may seem abstract, has very strong usage
    - More usage ideas: Searching for similar entries (like similar keywords in the search bar when you search something on Google), ranking things in similarity, etc.
  - Think: "semantic meaning"

