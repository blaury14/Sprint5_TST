import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV del conjunto de datos en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Configuración de la página
st.set_page_config(page_title="Proyecto Sprint 5 - Bastian Laury")
st.title("Anuncio de Venta de Vehículos - Gráficos")

# Histograma
st.header("Histograma")
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Dispersión
st.header("Gráfico de Dispersión")
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Construir un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="model_year", y="price", color="fuel")
    st.plotly_chart(fig, use_container_width=True)

# Enlaces
st.markdown("Link al repositorio: [GitHub - blaury14/Sprint5_TST](https://github.com/blaury14/Sprint5_TST)")
st.markdown("Lo invito a mirar el otro proyecto que hice. Puede ver una demostración aquí: [DEMO](https://da-17-vehicles-us.onrender.com/)")
