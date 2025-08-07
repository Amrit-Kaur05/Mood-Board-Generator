---
title: Mood-Generator-Planning

---

# Mood Generator Project Planning

## Table of Contents

1. [Brainstorm](#Brainstorm)
1. [Steps](#Steps)

# Brainstorm

### Project Overview
This website will allow users to generator their own personalized Pinterest board, allowing users to get inspiration for any of their needs!

Use cases include:
- 😊 Mood Boards: Users can input their current mood or a journal entry and get a personalized selection of images/Pins that reflect it!
- 🖼️ Vision Boards: Users can input what they want, whether it be for room planning or future travels, and can generate a board that will give them inspiration for what they'd like!
- 💭 ... And so much more!

### Tools needed
- Gradio: For the user interface and demo
- NLP to extract key themes, etc.:
    - Options: spaCy, transformers (BERT, SentenceTransformers)
- Image APIs, Pinterest API
- Possibly image generation models
    - Options: DALL·E (via OpenAI API), Stable Diffusion (locally or via Hugging Face)

# Steps
1. Getting user input and having it analyzed by NLP (can test using console messages)
2. Setting up the Image and Pinterest APIs
3. Making queries to APIs using the analysis data from NLP
4. Displaying images in organized board
5. Add option to download board or save board to Pinterest
6. Optional: Make an image generation mode