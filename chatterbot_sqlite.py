from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

print("setting up ChatBot")
chatbot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='./database.sqlite3'
)
print("training completed")


@app.route("/")
def home():
    return render_template("chatterbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True, port=80)
