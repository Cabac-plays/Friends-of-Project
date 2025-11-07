from flask import Flask, render_template, request
import math
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Fórmula de Bhaskara (equação 2º grau: ax² + bx + c = 0)
@app.route('/bhaskara', methods=['POST'])
def bhaskara():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        result = f"Raízes: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        result = f"Raiz única: x = {x}"
    else:
        result = "Sem raízes reais"
    return render_template('index.html', result=result)

# Trigonometria (ex: seno, cosseno, tangente em graus)
@app.route('/trig', methods=['POST'])
def trig():
    angulo = float(request.form['angulo'])
    tipo = request.form['tipo']  # 'sin', 'cos', 'tan'
    rad = math.radians(angulo)
    if tipo == 'sin':
        valor = math.sin(rad)
    elif tipo == 'cos':
        valor = math.cos(rad)
    else:
        valor = math.tan(rad)
    result = f"{tipo}({angulo}°) = {valor:.4f}"
    return render_template('index.html', result=result)

# Raízes (quadrada ou cúbica)
@app.route('/raiz', methods=['POST'])
def raiz():
    numero = float(request.form['numero'])
    tipo = request.form['tipo']  # 'quadrada' ou 'cubica'
    if tipo == 'quadrada':
        valor = math.sqrt(numero)
    else:
        valor = numero ** (1/3)
    result = f"Raiz {tipo} de {numero} = {valor:.4f}"
    return render_template('index.html', result=result)

# Equação 1º grau (ax + b = 0)
@app.route('/eq1', methods=['POST'])
def eq1():
    a = float(request.form['a'])
    b = float(request.form['b'])
    x = -b / a
    result = f"Solução: x = {x}"
    return render_template('index.html', result=result)

# Gráfico (ex: plot de y = ax² + bx + c)
@app.route('/grafico', methods=['POST'])
def grafico():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    x = sp.symbols('x')
    y = a*x**2 + b*x + c
    x_vals = range(-10, 11)
    y_vals = [y.subs(x, val) for val in x_vals]
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals)
    ax.set_title('Gráfico da Equação')
    
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('index.html', plot_url=plot_url)

# Juros Simples (J = C * i * t)
@app.route('/juros_simples', methods=['POST'])
def juros_simples():
    capital = float(request.form['capital'])
    taxa = float(request.form['taxa']) / 100
    tempo = float(request.form['tempo'])
    juros = capital * taxa * tempo
    montante = capital + juros
    result = f"Juros: {juros:.2f}, Montante: {montante:.2f}"
    return render_template('index.html', result=result)

# Juros Compostos (M = C * (1 + i)^t)
@app.route('/juros_compostos', methods=['POST'])
def juros_compostos():
    capital = float(request.form['capital'])
    taxa = float(request.form['taxa']) / 100
    tempo = float(request.form['tempo'])
    montante = capital * (1 + taxa)**tempo
    juros = montante - capital
    result = f"Juros: {juros:.2f}, Montante: {montante:.2f}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

