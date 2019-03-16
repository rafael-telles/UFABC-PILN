import os
import random
import re

_, _, arquivos = next(os.walk("dados/questoes"))

questoes = []
for arquivo in arquivos:
    questoes_disciplina = open("dados/questoes/{}".format(arquivo), "r").readlines()
    disciplina = re.compile("\.txt").split(arquivo)[0]

    questoes += [(questao, disciplina) for questao in questoes_disciplina]

random.seed(1)
random.shuffle(questoes)

corte = int(len(questoes) * 0.90)
questoes_treino, disciplinas_treino = zip(*questoes[:corte])
questoes_teste, disciplinas_teste = zip(*questoes[corte:])

def pegar_dados_treinamento():
    return questoes_treino, disciplinas_treino

def pegar_dados_teste():
    return questoes_teste, disciplinas_teste
