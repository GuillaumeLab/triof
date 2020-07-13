from imageio import imread
import os
from flask import Flask, render_template, request
from src.utils import *
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():
    open_waste_slot()
    return render_template('insert.html')


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()
    imagi = take_trash_picture()
    return render_template('type.html', image=imagi)


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    