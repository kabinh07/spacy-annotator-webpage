from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# Path to your JSON files
input_json_path = './data/sentences.json'
output_json_path = './data/annotated.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load-data', methods=['GET'])
def load_data():
    with open(input_json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/save-annotations', methods=['POST'])
def save_annotations():
    annotations = request.json
    with open(output_json_path, 'w', encoding='utf-8') as file:
        json.dump(annotations, file, ensure_ascii=False, indent=2)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)