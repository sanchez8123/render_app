import pandas as pd
import plotly.express as px
import streamlit as st


# Ruta absoluta al archivo CSV
df = pd.read_csv(r'C:\Users\User\Documents\analisis de datos\Repositorio\analytics_portfolio-Edna-Sanchez-\render_app\vehicles_us.csv')

# Crear un histograma
fig_hist = px.histogram(df, x='price', title='Histograma de precio')
fig_hist.show()
df = pd.read_csv(r'C:\Users\User\Documents\analisis de datos\Repositorio\analytics_portfolio-Edna-Sanchez-\render_app\vehicles_us.csv')

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)