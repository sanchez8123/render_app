import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv(r'C:\Users\User\Documents\analisis de datos\Repositorio\analytics_portfolio-Edna-Sanchez-\render_app\vehicles_us.csv')

# Crear un histograma
fig_hist = px.histogram(df, x='price', title='Histograma de precio')
fig_hist.show()
