import pyodbc
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Establecer configuración de la página
st.set_page_config(page_title="Mi Reporte", layout="wide")

#writer = pd.ExcelWriter('C:/ReportesPython/datos.xlsx')
#df = pd.t('C:/Users/Gabriel/Desktop/datos.xlsx')
df = pd.read_excel('C:/Users/Gabriel/Desktop/datos.xlsx', sheet_name='Hoja1')

# Crear gráfico interactivo
fig = px.bar(df, x='paises', y="poblacion")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Listado de Paises y sus poblaciones")
    st.dataframe(df)

with col2:
    st.plotly_chart(fig)