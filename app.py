from transformers import AutoTokenizer, pipeline
import gradio as gr
import cohere
import os
from dotenv import load_dotenv, find_dotenv

# Load the API key from the .env file
_ = load_dotenv(find_dotenv()) # read local .env file
cohere_api_key = os.environ['COHERE_API']

co = cohere.Client(cohere_api_key)

# Load the tokenizer associated with the specified model
tokenizer = AutoTokenizer.from_pretrained("Intel/dynamic_tinybert", padding=True, truncation=True, max_length=512)

# Define a question-answering pipeline using the model and tokenizer
question_answerer = pipeline(
    "question-answering", 
    model="Intel/dynamic_tinybert",
    tokenizer=tokenizer,
    return_tensors='pt'
)


def generate(question):
    result = co.chat(
              model="command",
              message=question,
              connectors=[{"id": "web-search"}])
    context = result.text
    squad_ex = question_answerer(question = question, context = context)
    return squad_ex['answer']

def respond(message, chat_history):
    bot_message = generate(message)
    chat_history.append((message, bot_message))

    return "", chat_history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(height=240) #just to fit the notebook
    msg = gr.Textbox(label="Ask away")
    btn = gr.Button("Submit")
    clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")

    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot]) #Press enter to submit

demo.queue().launch()