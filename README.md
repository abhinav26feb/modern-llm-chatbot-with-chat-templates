# Modern LLM Chatbot using Hugging Face Chat Templates

A modern AI chatbot built with Python, Hugging Face Transformers, and the instruction-tuned SmolLM2-360M model. This project demonstrates how contemporary conversational AI systems use chat templates, structured messages, and causal language models to generate intelligent responses.

## Overview

Unlike traditional Seq2Seq chatbots, this implementation uses a modern Causal Large Language Model (LLM) with Hugging Face Chat Templates. The chatbot maintains conversation history using structured message roles and automatically formats prompts for the model.

The project provides hands-on experience with:

- Large Language Models (LLMs)
- Hugging Face Transformers
- Chat Templates
- Prompt Engineering
- Tokenization
- Conversational AI Development

## Features

- Modern instruction-tuned LLM
- Chat Template support
- Structured conversation history
- Context-aware responses
- Adjustable creativity and response style
- Lightweight and CPU-friendly
- Open-source implementation

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- SmolLM2-360M-Instruct

## Model Information

**Model Used**

HuggingFaceTB/SmolLM2-360M-Instruct

SmolLM2-360M-Instruct is a lightweight instruction-tuned causal language model designed for conversational AI applications. It supports chat templates and structured message formatting similar to modern AI assistants.

## Project Architecture

User Input
    │
    ▼
Structured Messages
(System, User, Assistant)
    │
    ▼
Chat Template
    │
    ▼
Tokenization
    │
    ▼
SmolLM2-360M-Instruct
    │
    ▼
Generated Response
    │
    ▼
Conversation History Update


## Installation

Clone the repository:

git clone https://github.com/abhinav26feb/modern-llm-chatbot-with-chat-templates.git/n
cd modern-llm-chatbot-with-chat-templates

Install required dependencies:

pip install transformers torch accelerate


## Running the Chatbot


python chatbot_llm.py

Type:

exit
to end the conversation.

## Example Conversation


> Hello, how are you?

Bot: I'm doing well, thank you! How can I assist you today?

> What is Machine Learning?

Bot: Machine Learning is a branch of Artificial Intelligence that enables computers to learn patterns from data and improve performance without explicit programming.

> Explain NLP in one sentence.

Bot: Natural Language Processing is a field of AI focused on enabling computers to understand and generate human language.


## Chat Template Format

The chatbot uses structured messages:


messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "What is AI?"
    }
]


### Supported Roles

| Role | Purpose |
|--------|---------|
| System | Defines chatbot behavior |
| User | User questions and requests |
| Assistant | Model-generated responses |

## Learning Outcomes

By completing this project, you will learn:

- How modern LLM chatbots work
- Difference between Seq2Seq and Causal LLMs
- Transformer-based text generation
- Chat Templates in Hugging Face
- Managing conversation history
- Prompt engineering fundamentals
- Deploying open-source AI models

## Generation Parameters

The chatbot uses:


max_new_tokens=60
temperature=0.5
top_p=0.8
do_sample=True
repetition_penalty=1.3
no_repeat_ngram_size=3


These settings help generate concise, coherent, and less repetitive responses.

## Future Improvements

- Streamlit web interface
- Flask API integration
- Voice-enabled conversations
- Persistent chat history
- GPU acceleration
- Multiple model selection
- Custom system prompts

## Author

**Abhinav Bhaskar**

GitHub: https://github.com/abhinav26feb

## License

This project is created for educational and learning purposes.
