class Tarefa(object):
    estados = {'N': 'Nao iniciado', 
               'A': 'Em andamento', 
               'F': 'Finalizado'}
    def __init__(self):
        self.estado = 'N'
    def imprimir_estado(self):
        print self.estados[self.estado]

if __name__ == '__main__':
    nova_tarefa = Tarefa()
    nova_tarefa.imprimir_estado()

    # Eh a mesma coisa que
    Tarefa.imprimir_estado(nova_tarefa)



