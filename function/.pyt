import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não possui raízes reais"
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return f"x1 = {x1}, x2 = {x2}"

def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa/100)**tempo
    return f"Montante final: {montante:.2f}"

