from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from selenium import webdriver
from static.funcs import insert

app = Flask(__name__)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

tweet_url = "https://x.com/i/flow/login"
driver = None

CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return render_template("home.html")

@socketio.on("OnOffBrowser")
def OnOffBrowser():
    global driver  # Declare driver as global
    if driver:
        driver.quit()  # Use quit() to completely close the driver
        driver = None
        emit("OnOff", "#f10e0e", broadcast=False)
    else:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(tweet_url)
        emit("OnOff", "#0ef119", broadcast=False)

@socketio.on("message")
def handle_message(msg):
    print("Mensagem recebida: ", msg)
    socketio.send("SUCCES")

@socketio.on("insert")
def handle_insert(json):
    text = json.get("text")
    typ = json.get("typ")
    loc = json.get("loc")
    print("Mensagem recebida: ", json)
    insert(driver, text, typ, loc)
    socketio.send("Json Insert Getted!")

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0")
