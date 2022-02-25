import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSLl_Vn1NvAWYTPuwu8PVXFN9BrAd4gdBbyTIfpDDLdjucELrQRtm9pg9DdL-q-xsjsEVKPCEnBB378/pub?gid=888799103&single=true&output=csv'
st.set_page_config(layout="wide")
st.sidebar.markdown("## Censo en el departamento de córdoba")
st.sidebar.markdown("Lista oficial de los habitantes de córdoba, con indicación de sus condiciones sociales, económicas, etc.")
@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

datos = cargar_datos(url)


st.sidebar.markdown("---")

st.markdown("##  Descripcion las vivienda por municipio donde pueden encontrar su uso, tipo, su ocupacion, etc.")

lista_nom = list(datos['MUNICIPIOS'].unique())
opcion_nom = st.sidebar.selectbox(label="Selecione su municipio: ",
                          options=lista_nom)

servicios = list(datos.columns)
servicios.pop(servicios.index('MUNICIPIOS'))
servicios.pop(servicios.index('TOTAL HOGARES'))
servicios.pop(servicios.index('ESTRATO'))
servicios.pop(servicios.index('ENERGIA ELECTRICA'))
servicios.pop(servicios.index('SERVICIO DE GAS'))
servicios.pop(servicios.index('SERVICIO DE ACUEDUCTO'))
servicios.pop(servicios.index('SERVICIO DE ALCANTARILLADO'))
servicios.pop(servicios.index('RECOLECCION BASURAS'))
servicios.pop(servicios.index('SERVICIO DE INTERNET'))
select_servicios = st.selectbox('Seleciona los servicios', options=servicios)

st.markdown("Grafica descripcion de los hogares que hay en un municipio.")


@st.cache
def p_simple(df: pd.DataFrame, x: pd.DataFrame, y, N_filter: str):
    data = df.copy()
    data = data[data["MUNICIPIOS"] == N_filter]
    fig = px.histogram(data, x=x, y=y, color_discrete_sequence=px.colors.sequential.Aggrnyl, color='ESTRATO')
    return fig, data


p, c = p_simple(datos, select_servicios, "TOTAL HOGARES", opcion_nom)
st.plotly_chart(p, use_container_width=True)


@st.cache
def p_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
    fig = px.density_heatmap(data, x=x, y=y, color_continuous_scale=px.colors.sequential.Emrld)
    return fig, data


p, c = p_simple(datos, select_servicios, "TOTAL HOGARES", opcion_nom)
st.plotly_chart(p,use_container_width=True)

variables = list(datos.columns)
variables.pop(variables.index('MUNICIPIOS'))
variables.pop(variables.index('TOTAL HOGARES'))
variables.pop(variables.index('ENERGIA ELECTRICA'))
variables.pop(variables.index('SERVICIO DE GAS'))
variables.pop(variables.index('SERVICIO DE ACUEDUCTO'))
variables.pop(variables.index('SERVICIO DE ALCANTARILLADO'))
variables.pop(variables.index('RECOLECCION BASURAS'))
variables.pop(variables.index('SERVICIO DE INTERNET'))
variables.pop(variables.index('DESCRIPCION USO VIVIENDA'))
variables.pop(variables.index('DESCRIPCION TIPO VIVIENDA'))
variables.pop(variables.index('DESCRIPCION CONDICION OCUPACION'))
variables.pop(variables.index('DESCRIPCION MATERIAL PARED'))
variables.pop(variables.index('DESCRIPCION MATERIAL PISO'))
variables.pop(variables.index('DESCRIPCION TIPO SERVICIO SANITARIO'))

st.markdown("Grafica que muestra la sumatoria de los hogares por municipio y cual es estrato.")

opcion_z = st.radio(label="  ",
                    options=variables)

count = c.shape[0]
st.write('TOTAL DE HOGARES EN', opcion_nom ,count)

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
    fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
    return fig, data


pl, c = pie_simple(datos, "TOTAL HOGARES", opcion_z, opcion_nom)
st.plotly_chart(pl,use_container_width=True)

st.markdown("Grafica que muestra el porcentaje  y el total de hogares que si y no cuentan con servios publicos.")

col1, col2 = st.columns(2)

with col1:
    varias = list(datos.columns)
    varias.pop(varias.index('MUNICIPIOS'))
    varias.pop(varias.index('TOTAL HOGARES'))
    varias.pop(varias.index('ESTRATO'))
    varias.pop(varias.index('SERVICIO DE GAS'))
    varias.pop(varias.index('ENERGIA ELECTRICA'))
    varias.pop(varias.index('SERVICIO DE ALCANTARILLADO'))
    varias.pop(varias.index('RECOLECCION BASURAS'))
    varias.pop(varias.index('SERVICIO DE INTERNET'))
    varias.pop(varias.index('DESCRIPCION USO VIVIENDA'))
    varias.pop(varias.index('DESCRIPCION TIPO VIVIENDA'))
    varias.pop(varias.index('DESCRIPCION CONDICION OCUPACION'))
    varias.pop(varias.index('DESCRIPCION MATERIAL PARED'))
    varias.pop(varias.index('DESCRIPCION MATERIAL PISO'))
    varias.pop(varias.index('DESCRIPCION TIPO SERVICIO SANITARIO'))
    opcion_a = st.radio(label="",
                        options=varias)


    @st.cache
    def agua_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data


    plotA, c = agua_simple(datos, "TOTAL HOGARES", opcion_a, opcion_nom)
    st.plotly_chart(plotA, use_container_width=True)
with col2:
    variaciones = list(datos.columns)
    variaciones.pop(variaciones.index('MUNICIPIOS'))
    variaciones.pop(variaciones.index('TOTAL HOGARES'))
    variaciones.pop(variaciones.index('ESTRATO'))
    variaciones.pop(variaciones.index('SERVICIO DE GAS'))
    variaciones.pop(variaciones.index('ENERGIA ELECTRICA'))
    variaciones.pop(variaciones.index('SERVICIO DE ACUEDUCTO'))
    variaciones.pop(variaciones.index('RECOLECCION BASURAS'))
    variaciones.pop(variaciones.index('SERVICIO DE INTERNET'))
    variaciones.pop(variaciones.index('DESCRIPCION USO VIVIENDA'))
    variaciones.pop(variaciones.index('DESCRIPCION TIPO VIVIENDA'))
    variaciones.pop(variaciones.index('DESCRIPCION CONDICION OCUPACION'))
    variaciones.pop(variaciones.index('DESCRIPCION MATERIAL PARED'))
    variaciones.pop(variaciones.index('DESCRIPCION MATERIAL PISO'))
    variaciones.pop(variaciones.index('DESCRIPCION TIPO SERVICIO SANITARIO'))
    opcion_a = st.radio(label="  ",
                        options=variaciones)

    @st.cache
    def gas_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotG, c = gas_simple(datos, "TOTAL HOGARES", opcion_a, opcion_nom)
    st.plotly_chart(plotG, use_container_width=True)

colum1, colum2, colum3 = st.columns(3)
with colum1:
    varia = list(datos.columns)
    varia.pop(varia.index('MUNICIPIOS'))
    varia.pop(varia.index('TOTAL HOGARES'))
    varia.pop(varia.index('ESTRATO'))
    varia.pop(varia.index('SERVICIO DE ALCANTARILLADO'))
    varia.pop(varia.index('ENERGIA ELECTRICA'))
    varia.pop(varia.index('SERVICIO DE ACUEDUCTO'))
    varia.pop(varia.index('RECOLECCION BASURAS'))
    varia.pop(varia.index('SERVICIO DE INTERNET'))
    varia.pop(varia.index('DESCRIPCION USO VIVIENDA'))
    varia.pop(varia.index('DESCRIPCION TIPO VIVIENDA'))
    varia.pop(varia.index('DESCRIPCION CONDICION OCUPACION'))
    varia.pop(varia.index('DESCRIPCION MATERIAL PARED'))
    varia.pop(varia.index('DESCRIPCION MATERIAL PISO'))
    varia.pop(varia.index('DESCRIPCION TIPO SERVICIO SANITARIO'))
    opcion_b = st.radio(label="   ",
                        options=varia)


    @st.cache
    def alc_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotAc, c = alc_simple(datos, "TOTAL HOGARES", opcion_b, opcion_nom)
    st.plotly_chart(plotAc, use_container_width=True)

with colum2:
    otras = list(datos.columns)
    otras.pop(otras.index('MUNICIPIOS'))
    otras.pop(otras.index('TOTAL HOGARES'))
    otras.pop(otras.index('ESTRATO'))
    otras.pop(otras.index('SERVICIO DE ALCANTARILLADO'))
    otras.pop(otras.index('ENERGIA ELECTRICA'))
    otras.pop(otras.index('SERVICIO DE ACUEDUCTO'))
    otras.pop(otras.index('RECOLECCION BASURAS'))
    otras.pop(otras.index('SERVICIO DE GAS'))
    otras.pop(otras.index('DESCRIPCION USO VIVIENDA'))
    otras.pop(otras.index('DESCRIPCION TIPO VIVIENDA'))
    otras.pop(otras.index('DESCRIPCION CONDICION OCUPACION'))
    otras.pop(otras.index('DESCRIPCION MATERIAL PARED'))
    otras.pop(otras.index('DESCRIPCION MATERIAL PISO'))
    otras.pop(otras.index('DESCRIPCION TIPO SERVICIO SANITARIO'))
    opcion_b = st.radio(label="   ",
                        options=otras)


    @st.cache
    def basuras_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotB, c = basuras_simple(datos, "TOTAL HOGARES", opcion_b, opcion_nom)
    st.plotly_chart(plotB, use_container_width=True)

with colum3:
    otros = list(datos.columns)
    otros.pop(otros.index('MUNICIPIOS'))
    otros.pop(otros.index('TOTAL HOGARES'))
    otros.pop(otros.index('ESTRATO'))
    otros.pop(otros.index('SERVICIO DE ALCANTARILLADO'))
    otros.pop(otros.index('ENERGIA ELECTRICA'))
    otros.pop(otros.index('SERVICIO DE ACUEDUCTO'))
    otros.pop(otros.index('SERVICIO DE GAS'))
    otros.pop(otros.index('SERVICIO DE INTERNET'))
    otros.pop(otros.index('DESCRIPCION USO VIVIENDA'))
    otros.pop(otros.index('DESCRIPCION TIPO VIVIENDA'))
    otros.pop(otros.index('DESCRIPCION CONDICION OCUPACION'))
    otros.pop(otros.index('DESCRIPCION MATERIAL PARED'))
    otros.pop(otros.index('DESCRIPCION MATERIAL PISO'))
    otros.pop(otros.index('DESCRIPCION TIPO SERVICIO SANITARIO'))
    opcion_b = st.radio(label="   ",
                        options=otros)


    @st.cache
    def internet_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["MUNICIPIOS"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotI, c = internet_simple(datos, "TOTAL HOGARES", opcion_b, opcion_nom)
    st.plotly_chart(plotI, use_container_width=True)
