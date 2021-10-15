from flask import request, redirect, url_for, render_template, session, Response
from tester import app
from tester.application.morphological import Morphology

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        texts = request.form['formHolder']
        
        inst = Morphology(texts)
        print(inst.sepalate())

    return render_template('form.html')