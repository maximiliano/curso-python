# import tarefa
# class TarefaPessoal(tarefa.Tarefa):

from tarefa import Tarefa
class TarefaPessoal(Tarefa):
     def __init__(self):
         super(TarefaPessoal, self).__init__()

t = TarefaPessoal()
t.estado
    
# Se um atributo nao for encontrado na classe
# ira procurar na classe pai, recursivamente

# Classes herdadas podem 
# sobrescrever metodos da classe pai

