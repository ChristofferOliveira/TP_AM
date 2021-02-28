import numpy as np


def carrega_dados():

    arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes = carrega_arquivos()

    # Carregando Carros
    data = np.loadtxt(arq_carros)
    carros = data.view()

    # Carreagando Carros para Teste
    data = np.loadtxt(arq_teste)
    carros_test = data.view()

    # Carregando alvo dos Carros
    data = np.loadtxt(arq_alvo_carros)
    target_carros = data.view().astype(np.int)

    # Carregando alvo dos Carros para teste
    data = np.loadtxt(arq_alvo_testes)
    target_test = data.view().astype(np.int)

    fecha_arquivo(arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes)

    return carros, carros_test, target_carros, target_test


def cria_dados_knn():
    arq_knn = open('arquivoknn.txt', 'w')
    arq_knnteste = open('arquivoknnteste.txt', 'w')

    arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes = carrega_arquivos()

    contador = 0
    for i in arq_carros:

        linha = arq_carros.read(12)
        alvo = list(arq_alvo_carros.read(2))

        arq_knn.write(linha + str(alvo[0]) + '\n')
        contador += 1

    print(contador)
    arq_knn.close()

    for i in arq_teste:

        linha = arq_teste.read(12)
        alvo = list(arq_alvo_testes.read(2))

        arq_knnteste.write(linha + str(alvo[0]) + '\n')
        contador += 1

    print(contador)
    arq_knnteste.close()

    fecha_arquivo(arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes)


def carrega_dados_knn():

    arq_knn = open('arquivoknn.txt', 'r')
    data = np.loadtxt(arq_knn)
    carros = data.view()

    arq_knnteste = open('arquivoknnteste.txt', 'r')
    data = np.loadtxt(arq_knnteste)
    carros_teste = data.view()

    arq_alvo = open('TestesAlvo.txt', 'r')
    data = np.loadtxt(arq_alvo)
    teste_alvo = data.view()

    arq_alvo.close()
    arq_knnteste.close()
    arq_knn.close()

    return carros, carros_teste, teste_alvo

def carrega_arquivos():
    # Arquivo que contém Carros
    arq_carros = open('Carros.txt', 'r')

    # Arquivo que contém Carros para Teste
    arq_teste = open('Testes.txt', 'r')
    # Arquivo que contém alvo dos Carros
    arq_alvo_carros = open('CarrosAlvo.txt', 'r')
    # Arquivo que contém alvo dos Carros para Teste
    arq_alvo_testes = open('TestesAlvo.txt', 'r')

    return arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes


def fecha_arquivo(arq_carros, arq_alvo_carros, arq_teste, arq_alvo_testes):
    arq_carros.close()
    arq_alvo_carros.close()
    arq_teste.close()
    arq_alvo_testes.close()
