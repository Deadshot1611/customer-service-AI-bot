from transformers import pipeline
import gradio as gr
from fastapi import FastAPI
from gradio_client import Client
from typing import Union
import uvicorn


app = FastAPI()

chatbot = pipeline(model="Kaludi/Customer-Support-Assistant-V2")

def DS_chatbot(message,history):
    conversation = chatbot(message)
    return conversation[0]['generated_text']

io = gr.ChatInterface(DS_chatbot, title="Customer Service Bot", description="Enter your query.")


# Mount the Gradio app onto the FastAPI app
app = gr.mount_gradio_app(app, io, path='/')
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
