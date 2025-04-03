# render_app

Esta es una aplicación web interactiva desarrollada con Streamlit para realizar un análisis exploratorio de datos de vehículos. La aplicación permite a los usuarios visualizar y analizar datos clave sobre anuncios de venta de vehículos mediante gráficos dinámicos.

## Funcionalidades

- **Histograma**: Construcción de un histograma para analizar la distribución de la columna `odometer` (kilometraje).
- **Gráfico de dispersión**: Visualización de la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos.
- **Interactividad**: Los gráficos se generan dinámicamente al hacer clic en los botones correspondientes.

## Cómo ejecutar la aplicación

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación con el siguiente comando:
   ```bash
   streamlit run app.py
   ```

## Conjunto de datos

El archivo `vehicles_us.csv` contiene información sobre anuncios de venta de vehículos, incluyendo las siguientes columnas:
- `price`: Precio del vehículo.
- `odometer`: Kilometraje del vehículo.
- `model_year`: Año del modelo.
- `condition`: Condición del vehículo (nuevo, usado, etc.).
- `fuel`: Tipo de combustible utilizado por el vehículo.

## Despliegue

La aplicación puede ser desplegada en plataformas como Render o ejecutada localmente. Si está desplegada, puedes acceder a la versión en línea de la aplicación en el siguiente enlace:

**Mi primer deploy en Render**: [Enlace a la aplicación](https://tu-enlace-render.com)

## Autor

Edna Sánchez