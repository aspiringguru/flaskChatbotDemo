from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

print("loading ChatBot")
chatbot = ChatBot('Charlie')
print("setting trainer")
trainer = ListTrainer(chatbot)
print("training")
trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked.",
    "Can I book a car?",
    "Yes we can book a car for you."
])
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
