import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

data = {
    "IMC":   [18.5,  22.0,  24.0,  26.0, 28.0, 32.0, 38.0, 39.0, 40.0, 45.0],
    "Obeso": [False, False, False, False, False, True, True, True, True, True]
}

df = pd.DataFrame(data)
df.to_csv("imc_data.csv", index=False)

print("Arquivo CSV criado com sucesso!")

df = pd.read_csv("imc_data.csv")

X = df[["IMC"]]
y = df["Obeso"]

model = LogisticRegression()
model.fit(X, y)
print("Máquina treinada!")

# IMC fora do intervalo
novo_imc = np.array([[27.0]])
previsao = model.predict(novo_imc)

print(f"O IMC {novo_imc[0][0]} é considerado obeso? {previsao[0]}")