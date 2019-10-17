
import pandas as pd
import numpy as np
from sklearn import metrics

from sklearn.linear_model import LinearRegression, Ridge, ElasticNet
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_validate
from estimator import InputTransform




model = InputTransform(LinearRegression(), contamination=0.05)

X_t = pd.read_csv('task1/X_train.csv', ',')
y_t = pd.read_csv('task1/y_train.csv', ',')

X_t = pd.DataFrame(X_t.values[0:, 1:])
y_t = pd.DataFrame(y_t.values[0:, 1:])


cv_results = cross_validate(model, X_t, y_t, cv=10, scoring=make_scorer(metrics.r2_score))

print(cv_results['test_score'])
print("Average: " + str(np.average(cv_results['test_score'])))