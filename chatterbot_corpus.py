from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

print("loading ChatBot")
chatbot = ChatBot('corpus example')
print("setting trainer")
trainer = ChatterBotCorpusTrainer(chatbot)
print("training")
trainer.train('chatterbot.corpus.english')
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
