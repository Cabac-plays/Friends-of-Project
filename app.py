from flask import Flask, render_template, request
import math
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    grafico = None

    if request.method == "POST":
        tipo = request.form.get("tipo")

        # 🔹 Operações básicas
        if tipo == "basica":
            op = request.form.get("operacao")
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            if op == "soma":
                resultado = a + b
            elif op == "sub":
                resultado = a - b
            elif op == "mult":
                resultado = a * b
            elif op == "div":
                resultado = a / b if b != 0 else "Erro: divisão por zero"

        # 🔹 Bhaskara (equação do 2º grau)
        elif tipo == "bhaskara":
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))
            delta = b**2 - 4*a*c
            if delta < 0:
                resultado = "Sem raízes reais"
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                resultado = f"x1 = {x1:.2f}, x2 = {x2:.2f}"

        # 🔹 Trigonometria
        elif tipo == "trig":
            ang = math.radians(float(request.form.get("angulo")))
            sen = math.sin(ang)
            cos = math.cos(ang)
            tan = math.tan(ang)
            resultado = f"sen = {sen:.3f}, cos = {cos:.3f}, tan = {tan:.3f}"

        # 🔹 Juros simples e compostos
        elif tipo == "juros":
            capital = float(request.form.get("capital"))
            taxa = float(request.form.get("taxa")) / 100
            tempo = float(request.form.get("tempo"))
            modo = request.form.get("modo")

            if modo == "simples":
                montante = capital * (1 + taxa * tempo)
            else:
                montante = capital * ((1 + taxa) ** tempo)

            resultado = f"Montante final = R$ {montante:.2f}"

        # 🔹 Gráfico de função
        elif tipo == "grafico":
            expr = request.form.get("expressao")
            x = [i for i in range(-10, 11)]
            y = []
            for val in x:
                try:
                    y.append(eval(expr.replace("x", str(val))))
                except:
                    y.append(0)

            plt.figure()
            plt.plot(x, y, label=f"y = {expr}")
            plt.legend()
            plt.grid(True)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Gráfico da Função")

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            grafico = base64.b64encode(buf.getvalue()).decode("utf-8")
            buf.close()

    return render_template("index.html", resultado=resultado, grafico=grafico)

if __name__ == "__main__":
    app.run(debug=True)
