from sklearn.datasets import fetch_covtype
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate

forest = fetch_covtype()
data = forest['data']
label = forest['target']
print(data[:5])
print(label)

rf = RandomForestClassifier()

cv_results = cross_validate(rf, data, label, cv=3, scoring="accuracy")
print(sorted(cv_results.keys()))

print(cv_results['test_score'])



