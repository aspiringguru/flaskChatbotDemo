from flask import Flask, render_template, request
from chatterbot import ChatBot

app = Flask(__name__)

print("loading ChatBot")
chatbot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.UnitConversion'
    ]
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
