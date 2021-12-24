from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model


app = Flask(__name__)


model = load_model('Indonesian Abusive and Hate Speech Twitter Text/model.h5')


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("home.html")

def get_encode(teks):
    global padded
    tokenizer = Tokenizer(num_words= 15, oov_token='x')
    tokenizer.fit_on_texts(teks)
    sekuens = tokenizer.texts_to_sequences(teks)
    padded = pad_sequences(sekuens, 
                         maxlen=20,
                         padding='post',
                         truncating='post')
    return padded

def get_classes(classes):
        if max(classes[0]) == classes[0][0] :
            return("Bukan Ujaran Kebencian")
        elif max(classes[0]) == classes[0][1] :
            return("Ujaran Kebencian Agama")
        elif max(classes[0]) == classes[0][2] :
            return("Ujaran Kebencian Ras")
        elif max(classes[0]) == classes[0][3] :
            return("Ujaran Kebencian Fisik")
        elif max(classes[0]) == classes[0][4] :
            return("Ujaran Kebencian Gender")
        elif max(classes[0]) == classes[0][5] :
            return("Ujaran Kebencian Lain-lain")
    

@app.route("/predict", methods=["GET", "POST"])
def home():
    global classes
    if request.method == "POST":
        teks = request.form['form-input']
        encode_text = get_encode(teks)
        classes = model.predict(encode_text)

    return render_template("index.html", classes=get_classes(classes))


if __name__ == "__main__":
    app.run(debug=True)