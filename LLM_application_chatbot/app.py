from flask import Flask,request, render_template
from flask_cors import CORS
import json, torchvision, torchaudio
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"

print("Loading Model... Please wait...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Model Loaded. SUCCESSFULLY !!.")

conversation_history = []

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/chatbot", methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    print(data) # DEBUG
    input_text = data['prompt']

    #TODO: Task1 -> Create conversation history string
    history = "\n".join(conversation_history)

    #TODO: Task2 -> Tokenize the input text and history
    inputs = tokenizer(
        history,
        input_text,
        return_tensors="pt"
    )

    #TODO: Task3 -> Generate the response from the model
    outputs = model.generate(**inputs,
                             max_length=60)  # max_length will cause the model to crash at some point as history grows

    #TODO: Task4 -> Decode the response
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    ).strip()

    #TODO: Task5 -> Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response


if __name__ == "__main__":
    app.run()