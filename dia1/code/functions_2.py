def somatorio(*argumentos):
    soma = 0
    for i in argumentos:
        soma += i
    print soma

somatorio(2, 7, 20, 10, 5)

def imprimir_opcoes(**chaves):
    for chave, valor in chaves.items():
        print "chave: %s, valor: %s" % (chave, valor)

imprimir_opcoes(nome='John', idade=33)

