from flask import Flask, request, jsonify
import requests
import os
from gif_checker import check_gif_for_flashing_lights
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route('/check-gif-url', methods=['POST'])
def check_gif_url():
    data = request.get_json()
    url = data.get('url')
    temp_filename = "temp.gif"

    if not url:
        return jsonify({'message': 'No URL provided'}), 400

    try:
        response = requests.get(url, timeout=10)
        with open(temp_filename, "wb") as f:
            f.write(response.content)

        is_safe = check_gif_for_flashing_lights(temp_filename)
        os.remove(temp_filename)

        if is_safe:
            return jsonify({'message': '✅ Safe: This GIF does not appear to be harmful.'})
        else:
            return jsonify({'message': '🚨 Warning: This GIF might be unsafe (flashing lights detected).'})

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)
