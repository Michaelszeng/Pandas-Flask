"""
To run this program:

Use Powershell terminal

>.\enc\Scripts\activate
>flask run
"""

from flask import Flask, render_template
import pandas as pd
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
CORS(app)

# df = pd.read_csv('data.csv')
# df.to_csv('data.csv', index=None)

@app.route('/', methods=['GET'])
def index():
    data = pd.read_csv('data.csv')
    print(data.values.tolist())
    return render_template('index.html', data_list=data.values.tolist())