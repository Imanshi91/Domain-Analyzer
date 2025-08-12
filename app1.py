from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'Add your API KEY here !!'
API_URL = 'https://emailrep.io/'

def get_email_reputation(email):
    headers = {
        'Key': API_KEY,
        'User-Agent': 'emailrep.io Python Client'
    }
    response = requests.get(f'{API_URL}{email}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Failed to retrieve data: {response.status_code}'}

@app.route('/')
def index():
     return send_from_directory(os.getcwd(), 'index.html')

@app.route('/check', methods=['POST'])
def check():
    email = request.form['email']
    reputation_data = get_email_reputation(email)
    return jsonify(reputation_data)

if __name__ == '__main__':
    app.run(debug=True)
