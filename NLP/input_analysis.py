# NOTE: THIS IS MOSTLY NOTES AND TESTING

# getting sentence transformers from hugging face
# from application import user_input
from sentence_transformers import SentenceTransformer

# creating the model and embedding user input
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
user_input = "I want something cool and powerful, like lightning"
embedding = model.encode(user_input)

# printing output
# print(embedding)

# NOTE: This embedding data can be used for additional features. For example, if a user uploads an image, and we want to generate a board of SIMILAR images.
# Can also be used to compare similarity of text and images.

# using spacy to categorize words and keyword extraction
import spacy

nlp = spacy.load("en_core_web_sm") # loading a trained pipeline... will "return a Language object containing all components and data needed to process text"
doc = nlp(user_input) # calling our new nlp object on a string
keywords = [token.text for token in doc if token.pos_ in ["ADJ", "NOUN"]]
# ^ token.text = each token, like "is", etc.
# token.pos_ = part-of-speech tag for token
print(keywords)