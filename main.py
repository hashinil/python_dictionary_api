from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

filename = "data/dictionary.csv"
df = pd.read_csv(filename)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
def details(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    #word = word.capitalize()
    result = {"definition": definition, "word": word}
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5001)