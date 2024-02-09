from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    client_id = request.form['client_id']
    session_id = request.form['session_id']

    # Validate client_id and session_id using the API
    url = "https://ant.aliceblueonline.com/rest/AliceBlueAPIService/api/customer/accountDetails"
    headers = {
        'Authorization': f'Bearer {client_id} {session_id}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # If validation is successful, show the response in the next page
        return render_template('account_details.html', account_details=response.json())
    else:
        # If validation fails, redirect back to the login page with an error message
        return redirect(url_for('index', error="Invalid credentials"))

if __name__ == '__main__':
    app.run(debug=True)
