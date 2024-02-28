from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_word():
    return  render_template('index.html')

@app.route('/identificacao')
def identificacao():
    return  render_template('identificacao.html')

@app.route('/contextodarequisicao')
def contextodarequisicao():
    return  render_template('contextodarequisicao.html')

