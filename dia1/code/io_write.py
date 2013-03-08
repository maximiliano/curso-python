arquivo = open('teste2.txt', 'w')
arquivo.write("Uma string qualquer\n")

frases = ["Linha um\n", "Linha dois\n"]
# Não adiciona quebra de linha
arquivo.writelines(frases)
arquivo.close()

# Apaga todo arquivo antes de escrever
arquivo = open('teste2.txt', 'w')

# Comeca a escrever no final do arquivo, 
# preserva os dados anteriores
arquivo = open('teste2.txt', 'a')

# Escreve mudanças no arquivo
arquivo.flush()
