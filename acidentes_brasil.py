import pandas as pd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

def ler_csv(caminho, nome):
    print(f"Lendo o arquivo {nome}")
    df = pd.read_csv(caminho,sep=";", decimal=",", encoding="latin1")

    return df

# Lendo cada CSV e armazenando em variáveis
df_2020 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2022.csv', 2020)
df_2021 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2022.csv', 2021)
df_2022 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2022.csv', 2022)
df_2023 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2023.csv', 2023)
df_2024 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2024.csv', 2024)
df_2025 = ler_csv('/Users/magnosouza/PycharmProjects/Analise-Dados/data/datatran2025.csv', 2025)

# Concatenando os DataFrames
df = pd.concat([df_2020, df_2021, df_2022, df_2023, df_2024, df_2025], ignore_index=True)

#Transformando os nomes das colunas em minúsculos
df.columns = df.columns.str.lower()

#Excluindo do DataFrame as linhas em branco das colunas latitude e longitude
df = df.dropna(subset=['latitude', 'longitude'], how='any')

#Convertendo datas
df['data_inversa'] = pd.to_datetime(df['data_inversa'], errors='coerce')
df_ano = df['data_inversa'].dt.year.value_counts().astype(int)
df_mes = df['data_inversa'].dt.month.value_counts().sort_values(ascending=True)

# Convertendo latitude/longitude para float
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

#Percorrendo df_ano para identificação dos valores no gráfico
for i, valor in enumerate(df_ano.values):
    plt.text(df_ano.index[i], valor + 1000, f'{valor:,.0f}',
             ha='center', va='bottom', color='black', fontsize=12)

#Criando o grafico de barra e cores gradientes no gráfico
gradiente = df_ano/df_ano.max()
cores = plt.cm.Blues(gradiente)

#Plotando o gráfico
plt.bar(df_ano.index, df_ano.values, color = cores)
plt.xticks(df_ano.index)
plt.title('Acidentes por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Acidentes')
print(plt.show())

# Criando o mapa base
mapa = folium.Map(location=[-15.8, -47.9], zoom_start=5, tiles='CartoDB positron')

# Criando camadas (um grupo para cada ano)
anos = sorted(df['data_inversa'].dt.year.dropna().unique())

for ano in anos:
    grupo_ano = folium.FeatureGroup(name=str(int(ano)))
    cluster = MarkerCluster().add_to(grupo_ano)

    df_ano = df[df['data_inversa'].dt.year == ano]

    for _, linha in df_ano.iterrows():
        folium.Marker(
            location=[linha['latitude'], linha['longitude']],
            popup=f"Ano: {ano}<br>Data: {linha['data_inversa'].date()}",
            icon=folium.Icon(color='blue', icon='car', prefix='fa')
        ).add_to(cluster)

    grupo_ano.add_to(mapa)

# Adicionando o controle de camadas (botão de filtro)
folium.LayerControl(collapsed=False).add_to(mapa)

# Salvando o mapa
mapa.save('mapa_acidentes.html')
print("Mapa interativo salvo como 'mapa_acidentes.html'")