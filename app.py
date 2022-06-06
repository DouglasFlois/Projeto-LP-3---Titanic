import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  sex = int(request.form['sex'])
  pclass = int(request.form['pclass'])
  age = int(request.form['age'])
  sibsp = int(request.form['sibsp'])
  parch = float(request.form['parch'])
  predicao = model.predict([[sex, pclass, age, sibsp, parch]])
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
