import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def visualizar_dados(df, feature_names):
    sns.set_theme(style="whitegrid", palette='muted')
    plt.rcParams["figure.figsize"] = (10,6)
    print(df.head())
    df.hist(bins=30, figsize=(15,10))
    plt.suptitle("Histograma", fontsize=16)
    plt.show()

    plt.figure(figsize=(10,8))
    corr= df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlação")
    plt.show()

def previsao_dados_usuario(feature_names):
    user_data = []
    for feature in feature_names:
        while True:
            try:
                valor = float(input(f"Digite o valor para {feature} "))
                user_data.append(valor)
                break
            except ValueError:
                print("Valor Inválido")
    return np.array(user_data).reshape(1, -1)

print("BEM-VINDO AO AKINATOR DE MÓVEIS v0.1")

#1° passo: Carregar os dados

dados = fetch_california_housing()
X,y = dados.data, dados.target
feature_names = dados.feature_names
df = pd.DataFrame(X, columns = feature_names)
df['MedHouseVal'] = y

#2° passo: Opção a partir do usuário - Visualização
visualizar = input("Deseja visualizar os dados antes de treinar o modelo?")
if visualizar == "s":
    visualizar_dados(df, feature_names)

#3° passo: Dividindo dados para treino e teste
print("Dividindo dados para treino e teste")
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
print("Processo concluído")

#4° passo: Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("Normalização concluída")

#5° passo: Treinamento do modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)
print("Treinamento concluído")

#6° passo: Avaliação do modelo - Testes
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Erro Médio Absoluto: {mae:.2f}")
print(f"Coeficiente de Determinação: {r2:.2f}")

previsao = input("Deseja inserir seus próprios dados? (s/n)")
if previsao == "s":
    user_input = previsao_dados_usuario(feature_names)
    user_input_scaled = scaler.transform(user_input)
    prev = model.predict(user_input_scaled)
    print(f"A previsão do preço médio para o imóvel é: ${round(prev[0] * 100000,2)}")



