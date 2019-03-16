import os

import nltk
import numpy as np
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from questoes import pegar_dados_treinamento, pegar_dados_teste

CAMINHO_CLASSIFICADOR = "classificador.data"


def criar_classificador(questoes_treino, disciplinas_treino):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    text_clf = Pipeline([
        ('vect', CountVectorizer(stop_words=stopwords)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])

    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2)],
        'tfidf__use_idf': (True, False),
        'clf__alpha': (1e-2, 1e-3),
    }

    classificador = GridSearchCV(text_clf, parameters, n_jobs=-1, cv=3)
    classificador = classificador.fit(questoes_treino, disciplinas_treino)
    return classificador


def testar_acuracia(classificador, questoes_teste, disciplinas_teste):
    predicted = classificador.predict(questoes_teste)
    return np.mean(predicted == disciplinas_teste)


def pegar_classificador():
    if not os.path.exists(CAMINHO_CLASSIFICADOR):
        questoes_treino, disciplinas_treino = pegar_dados_treinamento()
        classificador = criar_classificador(questoes_treino, disciplinas_treino)
        dump(classificador, CAMINHO_CLASSIFICADOR)
    else:
        classificador = load(CAMINHO_CLASSIFICADOR)
    return classificador


if __name__ == "__main__":
    classificador = pegar_classificador()
    questoes_teste, disciplinas_teste = pegar_dados_teste()

    print(testar_acuracia(classificador, questoes_teste, disciplinas_teste))

    while True:
        q = input("Q:")
        prediction = classificador.predict_proba([q])[0]
        prediction = list(zip(classificador.classes_, prediction))
        prediction.sort(key=lambda p: -p[1])
        print(prediction)
