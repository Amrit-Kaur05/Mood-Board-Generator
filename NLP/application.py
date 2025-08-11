# testing out gradio using demo from: https://www.gradio.app/guides/quickstart#chatbots-with-gr-chat-interface

# importing gradio
import gradio as gr

import requests

import spacy

from api import access_key

def board(input):
    user_input = input
    keywords = process(user_input)
    images = image_urls(keywords)
    # from api import image_urls

    return images[1]
    # this will return the mood board


# making a function that will process the input
def process(input):
    # from sentence_transformers import SentenceTransformer
    #
    # model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    # embedding = model.encode(user_input)

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)
    keywords = [token.text for token in doc if token.pos_ in ["ADJ", "NOUN"]]
    print(keywords)
    print(" ".join(keywords))
    return " ".join(keywords)
    # print(keywords)

# making function that will call the api
def image_urls(keywords):

    url = f"https://api.unsplash.com/search/photos?query={keywords}&client_id={access_key}"

    response = requests.get(url)
    data = response.json()

    # Get first 5 image URLs
    image_urls = [item['urls']['small'] for item in data['results'][:5]]
    print(image_urls)
    return image_urls



# using the Interface class
# demo = gr.Interface(
#     # fn: "the function to wrap a user interface (UI) around"
#     fn = board,
#     # inputs: "the Gradio component(s) to use for the
#     # input. The number of components should match the number of
#     # arguments in your function."
#     inputs = ["text"],
#     # outputs: "the Gradio component(s) to use for the output.
#     # The number of components should match the number of
#     # return values from your function."
#     outputs = ["image","image","image","image"],
# )

with gr.Blocks() as demo:
    gr.Markdown("Write out your current mood and get a personalized mood board!")
    with gr.Row():
        input = gr.Textbox(placeholder="What's your current mood?")
        btn = gr.Button("Run")
    output = gr.Image()
    btn.click(fn=board, inputs=input, outputs=output)

demo.launch()



demo.launch()
# demo.launch(share=True) # using share=True to make a public URL for sharing

# More notes:
# "Custom Demos with gr.Blocks"
# "Chatbots with gr.ChatInterface"
# "You can also build Gradio applications without writing any code.
#  Simply type gradio sketch into your terminal to open up an editor
#  that lets you define and modify Gradio components, adjust their
#  layouts, add events, all through a web editor. "