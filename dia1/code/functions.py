def funcao_exemplo():
    "Aqui vai a documentacao"
    pass

def soma(x, y):
    z = x + y
    return z

def potencia(a, b):
    print a**b

def calcular_distancia(x, y, vantagem=None):
    if vantagem:
        return y - (x + vantagem)
    return y - x
