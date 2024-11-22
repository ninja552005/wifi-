from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    wifi_ssid = request.form.get('ssid')
    wifi_password = request.form.get('password')
    
    # In a real scenario, here you would validate the SSID and password, or attempt to connect to the Wi-Fi.
    if wifi_ssid and wifi_password:
        return f"Successfully connected to Wi-Fi SSID: {wifi_ssid} with Password: {wifi_password}"
    else:
        return "Invalid Wi-Fi credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
