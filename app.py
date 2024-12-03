from flask import Flask, jsonify, request
from flask_cors import CORS
from connect import get_top
import subprocess
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/api/data', methods=['GET'])

def get_data():
    # Retrieve query parameters
    artist = request.args.get('artist', '')  # Default to an empty string if not provided
    song = request.args.get('song', '')      # Default to an empty string if not provided
    get_top(artist,song)
    print(f"Received query: Artist={artist}, Song={song}")
    
    # Example response
    results = {
        'artist': artist,
        'song': song,
        'message': f"Results for artist '{artist}' and song '{song}'"
    }
    return jsonify(results)

@app.route('/api/data', methods=['POST'])

def post_data():
    data = request.json
    text_input = data.get('textInput', '')  # Get the text input from the POST request
    text_input2 = data.get('textInput2', '')
    print(f"Received text: {text_input}, {text_input2}")  # Log or process the input as needed
    
    get_top(text_input,text_input2)
    return jsonify({'receivedText': (text_input,text_input2), 'message': 'Data received successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
    