import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("ecommerce_preparados.csv")


# 1º Gráfico: Histograma


sns.set_theme(style="whitegrid")  # Configura o tema do seaborn
fig, axes = plt.subplots(
    1, 3, figsize=(16, 4.5)
)  # Cria uma figura com 1 linha e 3 colunas de subplots

sns.histplot(
    data=df, x="Preço", bins=30, kde=True, ax=axes[0], color="royalblue"
)  # Insere o histograma do preço com 30 bins e a curva de densidade
axes[0].set_title("Distribuição do preço (R$)")  # Define o título do primeiro subplot
axes[0].set_xlabel("Preço (R$)")  # Define o rótulo do eixo x do primeiro subplot

sns.histplot(
    data=df, x="Nota", bins=15, ax=axes[1], color="seagreen"
)  # Insere o histograma da nota com 15 bins
axes[1].set_title("Distribuição da nota")  # Define o título do segundo subplot
axes[1].set_xlabel("Nota (1 a 5)")  # Define o rótulo do eixo x do segundo subplot

sns.histplot(
    data=df, x="Desconto", bins=20, ax=axes[2], color="darkorange"
)  # Insere o histograma do desconto com 20 bins
axes[2].set_title("Distribuição do desconto (%)")  # Define o título do terceiro subplot
axes[2].set_xlabel("Desconto (%)")  # Define o rótulo do eixo x do terceiro subplot

for ax in axes:
    ax.set_ylabel("Número de produtos")

plt.tight_layout()  # Ajusta o layout para evitar sobreposição de elementos
plt.show()


# 2º Gráfico: Dispersão (Scatter Plot)


dados = df[
    ["Preço", "Nota"]
].dropna()  # Seleciona apenas as colunas 'Preço' e 'Nota' e remove valores nulos

sns.set_theme(style="whitegrid")  # Configura o tema do seaborn
plt.figure(
    figsize=(9, 5.5)
)  # Cria uma figura com tamanho de aproximadamente 13cm x 8cm
sns.scatterplot(
    data=dados, x="Preço", y="Nota", alpha=0.45, s=35, color="royalblue"
)  # Insere o scatter plot com transparência de 0,45 e tamanho dos pontos de 35

plt.title("Relação entre preço e nota")  # Define o título do gráfico
plt.xlabel("Preço (R$)")  # Define o rótulo do eixo x
plt.ylabel("Nota média (1 a 5)")  # Define o rótulo do eixo y

plt.tight_layout()  # Ajusta o layout para evitar sobreposição de elementos
plt.show()


# 3º Gráfico: mapa de calor


colunas = {
    "Preço": "Preço (R$)",
    "Nota": "Nota média",
    "N_Avaliações": "Nº de avaliações",
    "Desconto": "Desconto (%)",
}

corr = (
    df[list(colunas)].rename(columns=colunas).corr(method="spearman")
)  # Calcula a correlação entre as colunas selecionadas e renomeia as colunas para exibição

plt.figure(figsize=(8, 6))  # Cria uma figura com tamanho de aproximadamente 11cm x 8cm
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5,
    cbar_kws={"label": "Correlação de Spearman"},
)  # Insere o mapa de calor com anotações, formato de 2 casas decimais, colormap 'coolwarm', limites de - 1 a 1, quadrado, linhas de separação e rótulo da barra de cores
plt.title("Correlação entre as variáveis numéricas dos produtos")

plt.show()


# 4º Gráfico: barra


top_marcas = (
    df["Marca"].value_counts().head(10).reset_index()
)  # Seleciona as 10 marcas mais frequentes e reseta o índice
top_marcas.columns = [
    "Marca",
    "Quantidade",
]  # Renomeia as colunas para 'Marca' e 'Quantidade'

plt.figure(
    figsize=(9, 5.5)
)  # Cria uma figura com tamanho de aproximadamente 13cm x 8cm
ax = sns.barplot(data=top_marcas, x="Quantidade", y="Marca", color="royalblue")

for container in ax.containers:  # Adiciona os valores das barras no gráfico
    ax.bar_label(container, padding=3)

plt.title("10 marcas com mais produtos anunciados")
plt.xlabel("Número de produtos")

plt.show()


# 5º gráfico: pizza


contagem = df["Gênero"].value_counts()  # Conta a quantidade de produtos por gênero
principais = contagem[
    contagem >= 100
]  # Seleciona apenas os gêneros com mais de 100 produtos
outros = contagem[
    contagem < 100
].sum()  # Soma a quantidade de produtos dos gêneros com menos de 100 produtos
dados = pd.concat(
    [principais, pd.Series({"Outros": outros})]
)  # Cria um novo DataFrame com os gêneros principais e a categoria 'Outros'

plt.figure(figsize=(8, 6))  # Cria uma figura com tamanho de aproximadamente 11cm x 8cm
plt.pie(
    dados,
    labels=dados.index,
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
)  # Insere o gráfico de pizza com rótulos, porcentagem, ângulo inicial de 90 graus, sentido horário e borda branca
plt.title("Distribuição dos produtos por gênero")

plt.show()


# 6º gráfico: densidade


generos = ["Feminino", "Masculino", "Bebês"]
dados = df[
    df["Gênero"].isin(generos)
].dropna(
    subset=["Preço"]
)  # Seleciona apenas os produtos dos gêneros especificados e remove valores nulos da coluna 'Preço'

plt.figure(
    figsize=(9, 5.5)
)  # Cria uma figura com tamanho de aproximadamente 13cm x 8cm
sns.kdeplot(
    data=dados,
    x="Preço",
    hue="Gênero",
    hue_order=generos,
    fill=True,
    alpha=0.35,
    common_norm=False,
    cut=0,
    clip=(0, 400),
    linewidth=2,
)  # Insere o gráfico de densidade com preenchimento, transparência de 0,35, normalização separada para cada gênero, corte nos limites de 0 a 400 e largura da linha de 2

plt.title("Densidade de preço por gênero")
plt.xlabel("Preço (R$)")
plt.ylabel("Densidade")

plt.show()


# 7º gráfico: regressão

dados = df[
    ["N_Avaliações", "Nota"]
].dropna()  # Seleciona apenas as colunas 'N_Avaliações' e 'Nota' e remove valores nulos
dados = dados[
    dados["N_Avaliações"] > 0
].copy()  # Remove linhas com 0 avaliações para evitar problemas com logaritmo
dados["log_avaliacoes"] = np.log10(
    dados["N_Avaliações"]
)  # Cria uma nova coluna com o logaritmo base 10 do número de avaliações

sns.regplot(
    data=dados,
    x="log_avaliacoes",
    y="Nota",
    scatter_kws={"alpha": 0.3, "s": 30, "color": "royalblue"},
    line_kws={"color": "crimson", "linewidth": 2.5},
)  # Insere o gráfico de regressão com pontos de dispersão e linha de regressão, definindo a transparência, tamanho e cor dos pontos, e a cor e largura da linha

plt.title(
    "Regressão linear: nota média x número de avaliações"
)  # Define o título do gráfico
plt.xlabel("Número de avaliações (escala logarítmica)")
plt.ylabel("Nota média (1 a 5)")

plt.show()
