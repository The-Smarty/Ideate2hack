from flask import Flask, render_template, request
import PIL
from model import upload_predict
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def model():
    print("hello")
    file = request.files['image']
    print(file)
    image = PIL.Image.open(file)
    answer = upload_predict(image)
    print(answer)
    return render_template('index.html',answer=answer)


app.run(host='0.0.0.0',debug=True)