# Autor: Christoffer de Paula

import math
import operator
import csv
import Dados
from sklearn import metrics
# Importando Módulo prar obter tempo de execução
import time


def carrega_dados(arquivo_carros, arquivo_teste):
    grupo_treino = []
    grupo_teste = []

    for i in arquivo_carros:
        linha = list(arquivo_carros.readline())
        print(linha)

        for j in range(len(linha) - 1):
            linha[j] = float(linha[j])

        grupo_treino.append(linha)

    for i in arquivo_teste:
        linha = list(arquivo_teste.readline())

        for j in range(len(linha) - 1):
            linha[j] = float(linha[j])

        grupo_teste.append(linha)

    return grupo_treino, grupo_teste


def calcula_distancia_euclidiana(dado1, dado2):
    distancia = 0

    for i in range(len(dado1)):
        # Fazendo a potencia da diferença das cordenadas
        distancia += pow(dado1[i] - dado2[i], 2)

    # Retornando a raiz soma
    return math.sqrt(distancia)


def encontrar_vizinhos(dados_treino, dado_teste, k):
    distancias = []
    vizinhos = []

    for i in range(len(dados_treino) - 1):
        # Calculando a distancia euclidiana do dado teste entre todos os dados de treinamento
        dist_euclidiana = calcula_distancia_euclidiana(dado_teste, dados_treino[i])

        # Armazenando na distancia com tupla
        distancias.append((dado_teste, dist_euclidiana))

    # Deixando as tuplas mais perto primeiro
    distancias.sort(key=operator.itemgetter(1))

    # Armazenando os k vizinhos mais proximos na lista vizinhos
    for i in range(k):
        vizinhos.append(distancias[i][0])

    return vizinhos


def classificacao(vizinhos):
    votos = {}

    for i in range(len(vizinhos)):

        resposta = vizinhos[i][-1]

        if resposta in votos:
            votos[resposta] += 1
        else:
            votos[resposta] = 1

    votos_organizados = sorted(votos.items(), key=operator.itemgetter(1), reverse=True)

    return votos_organizados[0][0]


def obterPrecisao(conjunto_de_teste,predicoes):
    correto = 0
    for i in range(len(conjunto_de_teste)):
        if conjunto_de_teste[-1] in predicoes:
            correto += 1
    return (correto/float(len(conjunto_de_teste)))*100.0


def main():
    # Arquivo que contém Carros
    arq_carros = open('arquivoknn.txt', 'r')

    # Arquivo que contém Carros para Teste
    arq_teste = open('arquivoknnteste.txt', 'r')

    conjunto_de_teste, conjunto_de_treino, alvos = Dados.carrega_dados_knn()

    predicoes = []
    k = 3

    # Pegar tempo de execução
    inicio = time.time()

    for x in range(len(conjunto_de_treino)):
        vizinhos = encontrar_vizinhos(conjunto_de_treino, conjunto_de_teste[x], k)
        resultado = classificacao(vizinhos)
        predicoes.append(resultado)

    fim = time.time()

    expected = alvos
    predicted = predicoes

    print("Relatório de classificação para o classificador %s:\n%s\n"
          % ('knn', metrics.classification_report(expected, predicted)))

    print(f'Acurácia: {metrics.accuracy_score(expected, predicted)}\n')

    print("Matrix de confusão:\n%s" % metrics.confusion_matrix(expected, predicted))

    print(f'Tempo de execução: {fim - inicio}')

    arq_carros.close()
    arq_teste.close()


main()
