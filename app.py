from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture')
def main():
    return render_template('main.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    try:
        print("Content-Type:", request.headers['Content-Type']) # Print the MIME type of the request
        audio_file = request.files['audio']
        if audio_file:
            audio_file.save(os.path.join('uploads', 'recorded_audio.webm'))
            return jsonify({'status': 'success', 'message': 'Audio uploaded and saved successfully'})
            
        else:
            return jsonify({'status': 'error', 'message': 'No audio file received'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/capture', methods=['GET','POST'])
def capture():
    try:
        print("Content-Type:", request.headers['Content-Type']) # Print the MIME type of the request
        image_file = request.files['image']
        if image_file:
            image_file.save(os.path.join('uploads', 'captured_image.png'))
            return jsonify({'status': 'success', 'message': 'Image captured and saved successfully'})
            
        else:
            return jsonify({'status': 'error', 'message': 'No image file received'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)