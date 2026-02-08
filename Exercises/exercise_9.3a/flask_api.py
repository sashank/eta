
# app.py - Flask API for Traffic Classification
from flask import Flask, request, jsonify
import pickle
import numpy as np
import time

app = Flask(__name__)

# Load model and preprocessors
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

FEATURE_NAMES = [...]  # List of feature names

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/classify', methods=['POST'])
def classify():
    start_time = time.time()

    try:
        data = request.json

        # Extract features
        features = [data.get(f, 0) for f in FEATURE_NAMES]
        X = np.array(features).reshape(1, -1)

        # Preprocess
        X_scaled = scaler.transform(X)

        # Predict
        prediction = model.predict(X_scaled)[0]
        probabilities = model.predict_proba(X_scaled)[0]

        # Decode label
        application = label_encoder.inverse_transform([prediction])[0]
        confidence = float(max(probabilities))

        inference_time = (time.time() - start_time) * 1000

        return jsonify({
            'application': application,
            'confidence': confidence,
            'priority': get_priority(application),
            'inference_time_ms': inference_time
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_priority(application):
    priorities = {
        'VoIP': 'HIGH',
        'Video_Conferencing': 'HIGH',
        'Web_Browsing': 'MEDIUM',
        'Email': 'MEDIUM',
        'File_Transfer': 'MEDIUM',
        'Gaming': 'MEDIUM',
        'Video_Streaming': 'LOW',
        'Social_Media': 'LOW'
    }
    return priorities.get(application, 'MEDIUM')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
