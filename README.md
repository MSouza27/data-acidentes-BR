# Análise de Acidentes de Trânsito no Brasil

Este projeto realiza a **análise e visualização de dados de acidentes de trânsito no Brasil** utilizando Python, Pandas, Matplotlib e Folium. Ele processa arquivos CSV anuais da PRF, gera gráficos de acidentes por ano e cria um **mapa interativo com clusters de acidentes**.

## Funcionalidades

* Leitura e concatenação de múltiplos arquivos CSV de acidentes por ano.
* Limpeza de dados, incluindo remoção de valores ausentes e conversão de tipos.
* Análise temporal: número de acidentes por ano e por mês.
* Visualização:

  * Gráfico de barras com cores graduais indicando a quantidade de acidentes por ano.
  * Mapa interativo com marcadores agrupados por ano (MarkerCluster).
* Exportação do mapa interativo em HTML.

## Tecnologias e Bibliotecas

* **Python 3.x**
* **Pandas** – manipulação e limpeza de dados
* **Matplotlib** – gráficos de barras
* **Folium** – mapas interativos e clusters
* **Jupyter Notebook** ou IDEs compatíveis (PyCharm, VSCode, etc.)

## Estrutura de Arquivos

```
├── data/
│   ├── datatran2020.csv
│   ├── datatran2021.csv
│   ├── datatran2022.csv
│   ├── datatran2023.csv
│   ├── datatran2024.csv
│   └── datatran2025.csv
├── mapa_acidentes.html
├── analise_acidentes.py
└── README.md
```

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/analise-acidentes.git
cd analise-acidentes
```

2. Instale as dependências (recomenda-se criar um ambiente virtual):

```bash
pip install pandas matplotlib folium
```

3. Execute o script Python:

```bash
python analise_acidentes.py
```

4. O mapa interativo será salvo como `mapa_acidentes.html` na raiz do projeto.

## Observações

* Os arquivos CSV devem conter, pelo menos, as colunas `latitude`, `longitude` e `data_inversa`.
* As coordenadas geográficas devem estar no formato decimal.
* A coluna `data_inversa` deve estar no formato `dd/mm/yyyy`.

## Contribuição

Contribuições são bem-vindas! Para melhorias, abra uma **issue** ou envie um **pull request**.
