import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(layout="wide")

st.header("CENSO CORDOBA:")

@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

datos = cargar_datos('depurado.csv')
st.write(datos, use_container_width=True)


st.sidebar.markdown("## SERVICIOS PUBLICOS EN LOS HOGARES DE CORDOBA SEGUN SU ESTRATO")

lista_estrato = list(datos['estrato'].unique())
opcion_estrato = st.sidebar.selectbox(label="Selecione su estrato",
                                    options=lista_estrato)


otras_variables=list(datos.columns)
otras_variables.pop(otras_variables.index('Nom_municipio'))
otras_variables.pop(otras_variables.index('estrato'))
otras_variables.pop(otras_variables.index('total_hogares'))

opcion_y = st.sidebar.selectbox(label="Selecione un servicio",
                                    options=otras_variables)

st.sidebar.markdown("---")

st.header("Graficos de los servicios publico segun su estrato en cordoba: ")

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["estrato"] == Nom_municipio_filter]
    fig = px.histogram(data, x=x, y=y, color=opcion_y)
    return fig, data


pl, c = pie_simple(datos, opcion_y, "total_hogares", opcion_estrato)
st.plotly_chart(pl,use_container_width=True)
#st.write(c)

st.sidebar.markdown("## CONOCE LOS ESTRATO SOCIALES QUE ESTAN EN SU MUNICIPIO")

lista_Nom_municipio = list(datos['Nom_municipio'].unique())
opcion_Nom_municipio = st.sidebar.selectbox(label="Selecione su municipio",
                                    options=lista_Nom_municipio)


variables=list(datos.columns)
variables.pop(variables.index('Nom_municipio'))
variables.pop(variables.index('total_hogares'))
variables.pop(variables.index('energia_electrica'))
variables.pop(variables.index('servicio_gas'))
variables.pop(variables.index('servicio_acueducto'))
variables.pop(variables.index('servicio_alcantarillado'))
variables.pop(variables.index('recoleccion_basuras'))
variables.pop(variables.index('servicio_internet'))

opcion_z = st.sidebar.selectbox(label="",
                                    options=variables)

st.header("Grafica estrato social en su municipio: ")

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == Nom_municipio_filter]
    fig = px.pie(data, values=x, names=y)
    return fig, data


pl, c = pie_simple(datos, "total_hogares", opcion_z, opcion_Nom_municipio)
st.plotly_chart(pl,use_container_width=True)
#st.write(c)
