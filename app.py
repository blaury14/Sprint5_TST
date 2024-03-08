import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# Añade un encabezado
st.header('Panel de control de anuncios de venta de coches')

# Crea un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button: # Si se hace clic en el botón
    st.write('Construcción de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Agrega otro botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # Si se hace clic en el botón
    st.write('Construcción de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price", color="manufacturer")
    st.plotly_chart(fig, use_container_width=True)