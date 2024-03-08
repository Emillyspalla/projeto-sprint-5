# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo o arquivo CSV do conjunto de dados
car_data = pd.read_csv('vehicles.csv')

# Criando o conteúdo do aplicativo baseado em Streamlit
st.header("Análise de Anúncios de Venda de Veículos")

# Botão para criar um histograma
hist_button = st.button("Criar Histograma")

if hist_button:
    st.write("Criando um histograma para a coluna 'odometer'")

    # Criando um histograma
    fig = px.histogram(car_data, x="odometer")

    # Exibindo um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    st.write("Criando um gráfico de dispersão para as colunas 'odometer' e 'price'")

    # Criando um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # Exibindo um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
