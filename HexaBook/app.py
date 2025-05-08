from flask import Flask, jsonify, send_from_directory
import requests

from flask import Flask, send_from_directory, jsonify
import requests

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'login.html')

@app.route('/api/popular-books', methods=['GET'])
def get_popular_books():
    try:
        response = requests.get('https://www.dbooks.org/api/recent')
        response.raise_for_status()
        data = response.json()
        books = data.get('books', [])
        return jsonify({'status': 'success', 'books': books})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

