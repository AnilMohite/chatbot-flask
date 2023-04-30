from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Train the chatbot on a dataset
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@app.route("/")
def index():	
	return render_template("index.html")


@app.route("/get", methods=["GET","POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
