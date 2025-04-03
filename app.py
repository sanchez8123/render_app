import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.title('Análisis Exploratorio de datos de vehículos')

# Botón para construir un histograma
if st.button('Construir histograma'):
    st.write('Histograma de la columna odometer')
    if "odometer" in df.columns:
        fig = px.histogram(df, x="odometer", title="Histograma de Odometer")
    else:
        fig = px.histogram(df, x=df.columns[0], title=f"Histograma de {df.columns[0]}")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Gráfico de dispersión de la columna odometer')
    if "odometer" in df.columns:
        fig = px.scatter(df, x="odometer", y="price", title="Gráfico de dispersión de Odometer vs Price")
    else:
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title=f"Gráfico de dispersión de {df.columns[0]} vs {df.columns[1]}")
    st.plotly_chart(fig, use_container_width=True)