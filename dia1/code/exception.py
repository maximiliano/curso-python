# Excecoes sao definidas no modulo exceptions
# Esse modulo nunca precisa ser importado explicitamente

class Calculadora:
    def dividir(self, x, y):
        try:
            print x / y
        except ZeroDivisionError:
            print 'O denominador nao pode ser zero!'

# Coloque a excecao especifica
# Modo errado:
try:
    print x / y
except Exception:
    print 'Ocorreu um erro'

# Outras excecoes incluidas por padrao
# KeyboardInterrupt, IOError, IndexError, KeyError
