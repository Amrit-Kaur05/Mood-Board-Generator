# getting sentence transformers from hugging face
from sentence_transformers import SentenceTransformer

# creating the model and embedding user input
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
user_input = "I'm feeling a bit nostalgic and cozy today"
embedding = model.encode(user_input)

# printing output
# print(embedding)

# NOTE: This embedding data can be used for additional features. For example, if a user uploads an image, and we want to generate a board of SIMILAR images.
# Can also be used to compare similarity of text and images.

# using spacy to categorize words and keyword extraction
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(user_input)
print(doc)
keywords = [token.text for token in doc if token.pos_ in ["ADJ", "NOUN"]]
print(keywords)