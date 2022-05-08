from sklearn.datasets import fetch_covtype
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from tune_sklearn import TuneGridSearchCV


forest = fetch_covtype()
data = forest['data']
label = forest['target']
print(data[:5])
print(label)

data = data[:10000]
label = label[:10000]

rf = RandomForestClassifier()

cv_results = cross_validate(rf, data, label, cv=3, scoring="accuracy")
print(sorted(cv_results.keys()))

print(cv_results['test_score'])

params = {
        "max_depth": [5, 10, 11],
        "n_estimators": [20, 30, 40],
        "ccp_alpha": [0.0, 0.1, 0.2]
        }

tune_search = TuneGridSearchCV(rf, params)
import time
start = time.time()
tune_search.fit(data, label)
end = time.time()
print("Tune Fit Time: ", end - start)
print(tune_search.get_params())



