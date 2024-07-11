# cd D:\ML\Upshifters\Appl_task\REST_API

from flask import Flask, request, jsonify, current_app, g as app_ctx
from transformers import pipeline
import numpy as np
import time
import re

# initialize pipline
output_dir = "./arabert-model-v5-with-mixed"
class_map = {3:"Mixed", 2:"Positive", 1:"Neutral", 0:"Negative"}
pipe = pipeline("sentiment-analysis", model=output_dir, return_all_scores=True)

# preprocess input text
def get_clean_text(text):
    text = re.sub(r"[إأٱآا]", "ا", text) # Replace various Arabic characters with standard Arabic character 'ا'

    # remove hashtags at the end of the text
    while True:
        # Remove hashtags at the end of sentences
        updated_text = re.sub(r'\s*#\w+\s*$', '', text)
        # If text remains unchanged, break the loop
        if updated_text == text:
            break
        text = updated_text

    # Remove hashtag symbol and replace underscore with space in hashtags within text
    text = re.sub(r'#', '', text)  # remove hashtag symbol
    text = re.sub(r'_', ' ', text)  # replace underscore with space


    text = re.sub(r'@[\w_]+', '', text) # Remove mentions

    text = re.sub(r"\n", " ", text) # remove newlines
    text = re.sub(r"\s+", " ", text) # remove multiple spaces

    text = re.sub(r'[^\w\s]', '', text) # Remove special characters and punctuation marks except spaces (( without imojis approach))
    
    # text = re.sub(r'[^\w\s\d\U0001F000-\U0001FFFF]', '', text)  # remove special characters except spaces, digits, and emojis ((Uncomment this with imojis approach))

    text = re.sub(r'[a-zA-z]','',text) # remove all english characters

    text = re.sub(r"\.\.\.", "", text) # Remove ellipsis
    text = re.sub(r"\d+", " ", text) # remove all numbers (No need for them)
    text = re.sub(r"\s+", " ", text) # remove all repeated spaces

    return text

app = Flask(__name__)

# curl -i -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"text\": \"المنتج حلو!\"}"
@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        text = request.json['text']
        text = get_clean_text(text)
        scores = pipe(text)[0]
        sentiment = class_map[np.argmax([score['score'] for score in scores])]
        return jsonify({'prediction': sentiment})
    
@app.route('/predict_get/<text>', methods = ['GET'])  # GET request works well
def predict_get(text):
    return jsonify(pipe(text))

@app.before_request
def logging_before():
    # store the start time for the request
    app_ctx.start_time = time.perf_counter()

@app.after_request
def logging_after(response):
    # Get total time (ms)
    total_time = time.perf_counter() - app_ctx.start_time
    time_ms = int(total_time * 1000)
    # log the time token for the endpoint
    current_app.logger.info('%s ms %s %s %s', time_ms, request.method, request.path, dict(request.args))
    return response


if __name__ =="__main__":
    app.run(debug=True)