from flask import Flask, render_template, request, session, redirect
from logic import cemantix

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    secret_word = "pasta"

    if "guessed_words" not in session:
        session["guessed_words"] = []

    guessed_words = session["guessed_words"]
    result_message = None

    if request.method == "POST":
        given_word = request.form["word"]
        guessed_words, similarity = cemantix(secret_word, given_word, guessed_words)

        session["guessed_words"] = guessed_words

        if similarity == 1.0:
            result_message = "Vous avez gagné !"
        else:
            result_message = "Votre mot "+ given_word +" a une similarité de "+  str(round(similarity * 100, 2))  +" %."

    return render_template("index.html", guessed_words=guessed_words, result_message=result_message)


@app.route("/reset")
def reset():
    session.pop("guessed_words", None)
    return redirect("/")




