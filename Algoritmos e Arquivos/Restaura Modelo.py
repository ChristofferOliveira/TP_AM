import tensorflow as tf
import Dados
import dnn_classifier
from sklearn import metrics

# Importando Módulo prar obeter tempo de execução
import time

# Carregando os carros (Similar a função load_digits)

notes, notes_test, target_notes, target_test = Dados.carrega_dados()

# Para aplicar um classificador a esses dados, precisamos nivelar a imagem para
# transformar os dados em uma matriz (amostras, recurso):
n_samples = len(notes)
n_samples_teste = len(notes_test)

data = notes.reshape((n_samples, -1))
data_teste = notes_test.reshape((n_samples_teste, -1))

# Pegar tempo de execução
inicio = time.time()

he_init = tf.contrib.layers.variance_scaling_initializer()
rede = dnn_classifier.DNNClassifier(n_hidden_layers=5, n_neurons=100, optimizer_class=tf.train.AdamOptimizer, learning_rate=0.01,
                 batch_size=64, activation=tf.nn.elu, initializer=he_init, batch_norm_momentum=None, dropout_rate=None,
                 max_checks_without_progress=20, show_progress=10, tensorboard_logdir=None, random_state=None)

rede.fit(data, target_notes)

expected = target_test
predicted = rede.predict(data_teste)

fim = time.time()

print("Relatório de classificação para o classificador %s:\n%s\n"
       % (rede, metrics.classification_report(expected, predicted)))

print(f'Acurácia: {metrics.accuracy_score(expected, predicted)}\n')

print("Matrix de confusão:\n%s" % metrics.confusion_matrix(expected, predicted))

print(f'Tempo de execução: {fim - inicio}')