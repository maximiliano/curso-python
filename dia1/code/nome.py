def resumir(nome):
    print nome.lower().replace(' ', '_')

def expandir(nome):
    print nome.capitalize().replace('_', ' ')

if __name__ == '__main__':
    import sys
    opcao = sys.argv[1]
    nome = sys.argv[2]
    if opcao == 'resumir':
        resumir(nome)
    elif opcao == 'expandir':
        expandir(nome)
    else:
        print 'Opcao invalida.'
