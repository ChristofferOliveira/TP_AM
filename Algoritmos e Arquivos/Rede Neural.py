from sklearn.metrics import accuracy_score
from dnn_classifier import DNNClassifier
import Dados

from sklearn.model_selection import RandomizedSearchCV

# Carregando os carros (Similar a função load_digits)

carros, carros_test, target_carros, target_test = Dados.carrega_dados()

carros, carros_test, target_carros, target_test = Dados.carrega_dados()
n_exemplos = len(carros)
n_exemplos_teste = len(carros_test)
data_sklearn = carros.reshape((n_exemplos, -1))
data_sklearn_teste = carros_test.reshape((n_exemplos_teste, -1))

X_train = data_sklearn
y_train = target_carros

X_validation = data_sklearn[: 100]
y_validation = data_sklearn_teste[: 100]

X_test = data_sklearn_teste
y_test = target_test

dnn = DNNClassifier(show_progress=None, random_state=42)

parameter_distributions = {
    'n_hidden_layers': [3, 4, 5],
    'n_neurons': [40, 50, 100],
    'batch_size': [64, 128]
}

random_search = RandomizedSearchCV(dnn, parameter_distributions, n_iter=15, scoring='accuracy', verbose=2)
random_search.fit(X_train, y_train)

best_notas_dnn = random_search.best_estimator_
mnist_predictions = best_notas_dnn.predict(X_test)

print("Accuracy on test set: {:.2f}%".format(accuracy_score(y_test, mnist_predictions) * 100))

print(random_search.best_params_)


random_search.best_estimator_.save("models/mnist_random_best_model")