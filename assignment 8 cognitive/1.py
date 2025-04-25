from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import classification_report, confusion_matrix


iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.3, random_state=24, stratify=iris.target
)


pipe = Pipeline([
    ('scaler', MinMaxScaler()),
    ('ovo_lr', OneVsOneClassifier(
        LogisticRegression(solver='lbfgs', max_iter=500)
    ))
])


param_grid = {'ovo_lr__estimator__C': [0.01, 0.1, 1, 10]}
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)


print("Best C:", grid.best_params_['ovo_lr__estimator__C'])
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
