# RAG chatbot with Cohere API and Hugging Face 🤗

Retrieval Augmented Generation Chatbot with Cohere API and HuggingFace 🤗

## Overview

Introducing the Retrieval Augmented Generation Chatbot, a groundbreaking fusion of Cohere API and Hugging Face's technology, revolutionizing conversational AI by seamlessly blending factual accuracy with fluent dialogue. Leveraging Cohere API's robust knowledge retrieval and Hugging Face's generative capabilities, this innovative chatbot delivers contextually relevant and human-like conversations across domains like customer service and education, setting a new standard in interactive technology.

## Getting Started

### Environment Setup

To get started, create a virtual environment and activate it:

```bash
virtualenv venv
source venv/bin/activate
```

Create a local environment file (`.env`) and add your huggingface API key:

```bash
COHERE_API=your_cohere_api_key
```

### Install Dependencies

Next, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Run the Application

Now, you can run the application:

```bash
gradio app.py
```

This will start the application, allowing you to chat with the RAG model.

## Usage

Once the application is up and running, you can interact with the chatbot through a web interface.

## Additional Resources

- Check out the chatbot on [![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mca183/rag-cohere)
- Explore more about the Dynamic-TinyBERT model [here](https://huggingface.co/Intel/dynamic_tinybert)
