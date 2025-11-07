from flask import Flask, render_template, request, jsonify
import calculos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bhaskara', methods=['POST'])
def calc_bhaskara():
    data = request.json
    a, b, c = float(data['a']), float(data['b']), float(data['c'])
    resultado = calculos.bhaskara(a, b, c)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
