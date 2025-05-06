from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
print(len(X))
print(len(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.4, random_state=42)

print(f'Quantidade de itens na amostra de teste: {len(X_test)}')