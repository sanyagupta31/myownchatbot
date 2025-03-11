from flask import Flask , render_template,request,jsonify
import nltk 
from nltk.chat.util import Chat,reflections
app=Flask(__name__)
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name?", ["I am a chatbot created by Sanya!", "You can call me SanyaBot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing great!", "I'm fine! Thanks for asking."]],
    [r"bye|goodbye", ["Goodbye!", "See you soon!", "Bye! Take care."]],
    [r"how can you help me?", ["I can chat with you, answer basic questions, and help you feel less lonely!"]],
    [r"what can you do?", ["I can chat with you, answer general questions, and make your day better!"]],
    [r"who created you?", ["I was created by Sanya!", "Sanya developed me to chat with you."]],
    [r"what is your favorite color?", ["I like blue, just like the sky!", "Maybe yellow, like the sun!"]],
    [r"tell me a joke", [
        "Why don’t programmers like nature? It has too many bugs.",
        "Why did the computer go to therapy? It had too many issues."
    ]],
    [r"what is the capital of India?", ["The capital of India is New Delhi."]],
    [r"who is the president of India?", ["The current president of India is Droupadi Murmu."]],
    [r"who is the prime minister of India?", ["The Prime Minister of India is Narendra Modi."]],
    [r"what is machine learning?", ["Machine learning is a branch of AI that enables computers to learn from data without explicit programming."]],
    [r"what is data science?", ["Data Science is an interdisciplinary field that uses scientific methods, algorithms, and systems to extract knowledge from data."]],
    [r"what is your purpose?", ["My purpose is to assist and chat with you!"]],
    [r"tell me a fun fact", [
        "Did you know that honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
        "A group of flamingos is called a 'flamboyance'!"
    ]],
    [r"what is 2 + 2?", ["2 + 2 is 4, quick maths!"]],
    [r"how old are you?", ["I was created recently, so I guess I am quite young!"]],
    [r"can you sing?", ["I wish I could! Maybe I can hum some binary code for you: 0101010!"]],
]

chatbot=Chat(pairs,reflections)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        user_input = request.json.get("user_input", "")
        if not user_input:
            return jsonify({"response": "Please type something!"})

        response = chatbot.respond(user_input)
        return jsonify({"response": response if response else "I didn't understand that."})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)