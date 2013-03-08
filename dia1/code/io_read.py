# teste.txt
"""
Linha 1
Linha 2
"""

arquivo = open('teste.txt', 'r')
print arquivo.read()
arquivo.close()

arquivo = open('teste.txt', 'r')
print arquivo.readline()
print arquivo.readline()
print arquivo.readline()
arquivo.close()

arquivo = open('teste.txt', 'r')
print arquivo.readlines()
arquivo.close()

