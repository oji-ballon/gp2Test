from flask import Flask

app = Flask(__name__)
app.config.from_object('tester.config')

from tester.application import view
