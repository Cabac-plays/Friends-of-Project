import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem raízes reais"
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

def juros_simples(capital, taxa, tempo):
    return capital * (1 + taxa * tempo)

def juros_compostos(capital, taxa, tempo):
    return capital * ((1 + taxa) ** tempo)

def seno(angulo):
    return math.sin(math.radians(angulo))

def cosseno(angulo):
    return math.cos(math.radians(angulo))
