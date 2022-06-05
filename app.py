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
  data1 = request.form['sex']
  data2 = request.form['pclass']
  data3 = request.form['age']
  data4 = request.form['sibsp']
  data5 = request.form['parch']
  arr = np.array([[data1, data2, data3, data4, data5]])
  pred = model.predict(arr) 
  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
