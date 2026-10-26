import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Anuncios de coches", layout="wide")

# Leer los datos
car_data = pd.read_csv("vehicles_us.csv")

# Encabezado
st.header("Panel de anuncios de venta de coches en EE. UU.")
st.write(
    "Explora el conjunto de datos de anuncios de coches usados. "
    "Marca las casillas para generar los gráficos."
)

# Vista rápida de los datos
if st.checkbox("Mostrar una muestra de los datos"):
    st.dataframe(car_data.head(20))

# --- Histograma ---
st.subheader("Histograma")
build_histogram = st.checkbox("Construir un histograma del odómetro")

if build_histogram:
    st.write("Distribución del kilometraje (odómetro) de los coches anunciados")
    fig_hist = px.histogram(car_data, x="odometer", nbins=50)
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Gráfico de dispersión ---
st.subheader("Gráfico de dispersión")
build_scatter = st.checkbox("Construir un gráfico de dispersión: odómetro vs. precio")

if build_scatter:
    st.write("Relación entre el kilometraje y el precio de los coches")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.5,
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- Botón extra ---
st.subheader("Precio por tipo de vehículo")
if st.button("Construir gráfico de precio por tipo"):
    st.write("Precio mediano según el tipo de vehículo")
    price_by_type = (
        car_data.groupby("type")["price"].median().sort_values(ascending=False).reset_index()
    )
    fig_bar = px.bar(price_by_type, x="type", y="price")
    st.plotly_chart(fig_bar, use_container_width=True)
