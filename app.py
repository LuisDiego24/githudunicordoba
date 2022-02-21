import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(layout="wide")
st.sidebar.image('dane.png')
st.sidebar.image('gobernacion.png')
st.sidebar.markdown("## Censo en el departamento de cordoba")
st.sidebar.markdown("Lista oficial de los habitantes de cordoba, con indicación de sus condiciones sociales, económicas, etc.")
##-------------------------------------------------------------------
@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

datos = cargar_datos('depurado.csv')


st.markdown("### Hoagares que cuentan con servicios en cordoba:")

st.sidebar.markdown("---")

st.sidebar.markdown("Escoge un municipio y un servicio publico mira los hogares cuentan con estos: ")

lista_estrato = list(datos['Nom_municipio'].unique())
opcion_estrato = st.sidebar.selectbox(label="Selecione el municipio",
                                    options=lista_estrato)

otras_variables = list(datos.columns)
otras_variables.pop(otras_variables.index('Nom_municipio'))
otras_variables.pop(otras_variables.index('estrato'))
otras_variables.pop(otras_variables.index('total_hogares'))

opcion_y = st.sidebar.selectbox(label="Selecione un servicio",
                                    options=otras_variables)

st.sidebar.markdown("---")

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, estrato_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == estrato_filter]
    fig = px.histogram(data, x=x, y=y, color_discrete_sequence=px.colors.sequential.Bluered)
    return fig, data


pl, c = pie_simple(datos, opcion_y, "total_hogares", opcion_estrato)
st.plotly_chart(pl,use_container_width=True)

st.markdown("selecione su municipio y podra resolver las siente preguntas, "
            "¿Cuantos hogares hay un vivienda y cual es su estrato?,  "
            "¿Conozca cuantos hogares hay en un municipio y su estrato social?, "
            "y ¿Cuantos hogares en cordoba cuentan con servios basicos, como energia electrica, servicio de aceducto y gas?")

lista_nom = list(datos['Nom_municipio'].unique())
opcion_nom = st.selectbox(label="Selecione su municipio: ",
                          options=lista_nom)

otras_variable = list(datos.columns)
otras_variable.pop(otras_variable.index('Nom_municipio'))
otras_variable.pop(otras_variable.index('total_hogares'))
otras_variable.pop(otras_variable.index('energia_electrica'))
otras_variable.pop(otras_variable.index('servicio_gas'))
otras_variable.pop(otras_variable.index('servicio_acueducto'))
otras_variable.pop(otras_variable.index('servicio_alcantarillado'))
otras_variable.pop(otras_variable.index('recoleccion_basuras'))
otras_variable.pop(otras_variable.index('servicio_internet'))

opcion_y = st.radio(label=" ",
                    options=otras_variable)

@st.cache
def p_simple(df: pd.DataFrame, x: pd.DataFrame, y, N_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == N_filter]
    fig = px.box(data, x=x, y=y, color=opcion_y)
    return fig, data


p, c = p_simple(datos, opcion_y, "total_hogares", opcion_nom)
st.plotly_chart(p, use_container_width=True)

variables = list(datos.columns)
variables.pop(variables.index('Nom_municipio'))
variables.pop(variables.index('total_hogares'))
variables.pop(variables.index('energia_electrica'))
variables.pop(variables.index('servicio_gas'))
variables.pop(variables.index('servicio_acueducto'))
variables.pop(variables.index('servicio_alcantarillado'))
variables.pop(variables.index('recoleccion_basuras'))
variables.pop(variables.index('servicio_internet'))

opcion_z = st.radio(label="  ",
                    options=variables)

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == Nom_municipio_filter]
    fig = px.pie(data, values=x, names=y)
    return fig, data


pl, c = pie_simple(datos, "total_hogares", opcion_z, opcion_nom)
st.plotly_chart(pl,use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1:
    varia = list(datos.columns)
    varia.pop(varia.index('Nom_municipio'))
    varia.pop(varia.index('total_hogares'))
    varia.pop(varia.index('estrato'))
    varia.pop(varia.index('servicio_gas'))
    varia.pop(varia.index('servicio_acueducto'))
    varia.pop(varia.index('servicio_alcantarillado'))
    varia.pop(varia.index('recoleccion_basuras'))
    varia.pop(varia.index('servicio_internet'))
    opcion_a = st.radio(label="",
                        options=varia)


    @st.cache
    def luz_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.RdPu)
        return fig, data


    plotE, c = pie_simple(datos, "total_hogares", opcion_a, opcion_nom)
    st.plotly_chart(plotE, use_container_width=True)
with col2:
    varias = list(datos.columns)
    varias.pop(varias.index('Nom_municipio'))
    varias.pop(varias.index('total_hogares'))
    varias.pop(varias.index('estrato'))
    varias.pop(varias.index('servicio_gas'))
    varias.pop(varias.index('energia_electrica'))
    varias.pop(varias.index('servicio_alcantarillado'))
    varias.pop(varias.index('recoleccion_basuras'))
    varias.pop(varias.index('servicio_internet'))
    opcion_a = st.radio(label="",
                        options=varias)


    @st.cache
    def agua_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.RdPu)
        return fig, data


    plotA, c = pie_simple(datos, "total_hogares", opcion_a, opcion_nom)
    st.plotly_chart(plotA, use_container_width=True)
with col3:
    variacines = list(datos.columns)
    variacines.pop(variacines.index('Nom_municipio'))
    variacines.pop(variacines.index('total_hogares'))
    variacines.pop(variacines.index('estrato'))
    variacines.pop(variacines.index('servicio_acueducto'))
    variacines.pop(variacines.index('energia_electrica'))
    variacines.pop(variacines.index('servicio_alcantarillado'))
    variacines.pop(variacines.index('recoleccion_basuras'))
    variacines.pop(variacines.index('servicio_internet'))
    opcion_a = st.radio(label=" ",
                        options=variacines)

    @st.cache
    def gas_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.RdPu)
        return fig, data

    plotG, c = pie_simple(datos, "total_hogares", opcion_a, opcion_nom)
    st.plotly_chart(plotG, use_container_width=True)
