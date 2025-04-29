from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def maquina():

    dados_iris = load_iris()
    x = dados_iris.data
    y = dados_iris.target

    X_treinar, X_testar, Y_treinar, y_testar = train_test_split(x, y, test_size=0.2, random_state=42)

    estimator = KNeighborsClassifier(n_neighbors=3)

    estimator.fit(X_treinar, Y_treinar)

    try:
        print("Insira as características da flor:")
        comprimento_sepala = float(input("Comprimento da sépala (cm): "))
        largura_sepala = float(input("Largura da sépala (cm): "))
        comprimento_petala = float(input("Comprimento da pétala (cm): "))
        largura_petala = float(input("Largura da pétala (cm): "))
    except ValueError:
        print("Por favor, insira apenas números.")
        return

    dados_entrada = [[comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]]
    previsao = estimator.predict(dados_entrada)

    nome_da_flor = dados_iris.target_names[previsao[0]]
    print(f"A flor prevista é: {nome_da_flor}")

maquina()