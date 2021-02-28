# Author: Christoffer de Paula Oliveira

# Importando módulo que retorna os dados
import Dados

# Importando Algoritmo KNN e Métricas para porcentagem de acertos e matriz de confusão.
from sklearn import neighbors, metrics

# Importando Módulo prar obter tempo de execução
import time

# Carregando os Carros (Similar a função load_digits)

carros, carros_test, target_carros, target_test = Dados.carrega_dados()

# Para aplicar um classificador a esses dados, precisamos nivelar o vetor para
# transformar os dados em (amostras, recurso):
n_samples = len(carros)
n_samples_teste = len(carros_test)

data = carros.reshape((n_samples, -1))
data_teste = carros_test.reshape((n_samples_teste, -1))

# Criar um classificador: um classificador de vizinhos mais próximos
n_neighbors = 2

X = data
y = target_carros

# Pegar tempo de execução
inicio = time.time()

for weights in ['uniform', 'distance']:
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)

# Aprendemos os carros para treinamento, ou seja, 70% dos dados

# Agora, preveja os carros com o restante dos dados, isto é, 30%
expected = target_test
predicted = clf.predict(data_teste)

fim = time.time()

print("Relatório de classificação para o classificador %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))

print(f'Acurácia: {metrics.accuracy_score(expected, predicted)}\n')

print("Matrix de confusão:\n%s" % metrics.confusion_matrix(expected, predicted))

print(f'Tempo de execução: {fim - inicio}')