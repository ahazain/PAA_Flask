import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Ahmad Farid Zainudin','email': '222410102093@mail.unej.ac.id'})
app.run()