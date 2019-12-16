from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

from train_and_test_definition import X_train
from fit_tune_function import fit_tune_store_sgdcv

len_n = len(X_train)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)),
])

parameters = {
    'vect__ngram_range': [(1, 1), ],
    'tfidf__use_idf': (True, False),
    'clf__random_state': (0, 1, 42, 160, ),
    'clf__alpha': (1e-2, 1e-3, 0.1 ),
    'clf__hidden_layer_sizes': [(1, ), (3, ), (len_n, )],
    #'clf__activation': ['tanh', 'relu'],
    #'clf__solver': ['sgd', 'adam'],
    'clf__learning_rate': ['constant', 'adaptive'],
}

mlp_clf_gscv = GridSearchCV(text_clf, parameters, cv=5, iid=False, n_jobs=-1)
fit_tune_store_sgdcv(mlp_clf_gscv, 'mlp')
