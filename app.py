import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQHLedstzxMCoJYgyYDeywW01s8vJ3hQzty-ATB8QC64CR2SMwvEaSxwwPze2c1coLeHh8vfemJJbu5/pub?gid=788685982&single=true&output=csv'
st.set_page_config(layout="wide")
st.sidebar.markdown("## Censo en el departamento de cordoba")
st.sidebar.markdown("Lista oficial de los habitantes de cordoba, con indicación de sus condiciones sociales, económicas, etc.")
@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

datos = cargar_datos(url)



st.sidebar.markdown("---")


lista_nom = list(datos['Nom_municipio'].unique())
opcion_nom = st.sidebar.selectbox(label="Selecione su municipio: ",
                          options=lista_nom)

servicios = list(datos.columns)
servicios.pop(servicios.index('Nom_municipio'))
servicios.pop(servicios.index('total_hogares'))
servicios.pop(servicios.index('estrato'))
servicios.pop(servicios.index('energia_electrica'))
servicios.pop(servicios.index('servicio_gas'))
servicios.pop(servicios.index('servicio_acueducto'))
servicios.pop(servicios.index('servicio_alcantarillado'))
servicios.pop(servicios.index('recoleccion_basuras'))
servicios.pop(servicios.index('servicio_internet'))
select_servicios = st.selectbox('Seleciona los servicios', options=servicios)

st.markdown("Grafica descripcion de los hogares que hay en un municipio.")


@st.cache
def p_simple(df: pd.DataFrame, x: pd.DataFrame, y, N_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == N_filter]
    fig = px.histogram(data, x=x, y=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
    return fig, data


p, c = p_simple(datos, select_servicios, "total_hogares", opcion_nom)
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
variables.pop(variables.index('descripcion_uso_vivienda'))
variables.pop(variables.index('descripcion_tipo_vivienda'))
variables.pop(variables.index('descripcion_condicion_ocupacion'))
variables.pop(variables.index('descripcion_material_pared'))
variables.pop(variables.index('descripcion_material_piso'))
variables.pop(variables.index('descripcion_tipo_servicio_sanitario'))

st.markdown("Grafica que muestra la sumatoria de los hogares por municipio y cual es estrato.")

opcion_z = st.radio(label="  ",
                    options=variables)

@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == Nom_municipio_filter]
    fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
    return fig, data


pl, c = pie_simple(datos, "total_hogares", opcion_z, opcion_nom)
st.plotly_chart(pl,use_container_width=True)

st.markdown("Grafica que muestra el porcentaje  y el total de hogares que si y no cuentan con servios publicos.")

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
    varia.pop(varia.index('descripcion_uso_vivienda'))
    varia.pop(varia.index('descripcion_tipo_vivienda'))
    varia.pop(varia.index('descripcion_condicion_ocupacion'))
    varia.pop(varia.index('descripcion_material_pared'))
    varia.pop(varia.index('descripcion_material_piso'))
    varia.pop(varia.index('descripcion_tipo_servicio_sanitario'))

    opcion_a = st.radio(label="",
                        options=varia)


    @st.cache
    def luz_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data


    plotE, c = luz_simple(datos, "total_hogares", opcion_a, opcion_nom)
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
    varias.pop(varias.index('descripcion_uso_vivienda'))
    varias.pop(varias.index('descripcion_tipo_vivienda'))
    varias.pop(varias.index('descripcion_condicion_ocupacion'))
    varias.pop(varias.index('descripcion_material_pared'))
    varias.pop(varias.index('descripcion_material_piso'))
    varias.pop(varias.index('descripcion_tipo_servicio_sanitario'))
    opcion_a = st.radio(label="",
                        options=varias)


    @st.cache
    def agua_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data


    plotA, c = agua_simple(datos, "total_hogares", opcion_a, opcion_nom)
    st.plotly_chart(plotA, use_container_width=True)
with col3:
    variaciones = list(datos.columns)
    variaciones.pop(variaciones.index('Nom_municipio'))
    variaciones.pop(variaciones.index('total_hogares'))
    variaciones.pop(variaciones.index('estrato'))
    variaciones.pop(variaciones.index('servicio_acueducto'))
    variaciones.pop(variaciones.index('energia_electrica'))
    variaciones.pop(variaciones.index('servicio_alcantarillado'))
    variaciones.pop(variaciones.index('recoleccion_basuras'))
    variaciones.pop(variaciones.index('servicio_internet'))
    variaciones.pop(variaciones.index('descripcion_uso_vivienda'))
    variaciones.pop(variaciones.index('descripcion_tipo_vivienda'))
    variaciones.pop(variaciones.index('descripcion_condicion_ocupacion'))
    variaciones.pop(variaciones.index('descripcion_material_pared'))
    variaciones.pop(variaciones.index('descripcion_material_piso'))
    variaciones.pop(variaciones.index('descripcion_tipo_servicio_sanitario'))
    opcion_a = st.radio(label=" ",
                        options=variaciones)

    @st.cache
    def gas_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotG, c = gas_simple(datos, "total_hogares", opcion_a, opcion_nom)
    st.plotly_chart(plotG, use_container_width=True)

colum1, colum2, colum3 = st.columns(3)
with colum1:
    variar = list(datos.columns)
    variar.pop(variar.index('Nom_municipio'))
    variar.pop(variar.index('total_hogares'))
    variar.pop(variar.index('estrato'))
    variar.pop(variar.index('energia_electrica'))
    variar.pop(variar.index('servicio_acueducto'))
    variar.pop(variar.index('servicio_gas'))
    variar.pop(variar.index('recoleccion_basuras'))
    variar.pop(variar.index('servicio_internet'))
    variar.pop(variar.index('descripcion_uso_vivienda'))
    variar.pop(variar.index('descripcion_tipo_vivienda'))
    variar.pop(variar.index('descripcion_condicion_ocupacion'))
    variar.pop(variar.index('descripcion_material_pared'))
    variar.pop(variar.index('descripcion_material_piso'))
    variar.pop(variar.index('descripcion_tipo_servicio_sanitario'))
    opcion_b = st.radio(label="          ",
                        options=variar)


    @st.cache
    def alc_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotAc, c = alc_simple(datos, "total_hogares", opcion_b, opcion_nom)
    st.plotly_chart(plotAc, use_container_width=True)

with colum2:
    otras = list(datos.columns)
    otras.pop(otras.index('Nom_municipio'))
    otras.pop(otras.index('total_hogares'))
    otras.pop(otras.index('estrato'))
    otras.pop(otras.index('servicio_gas'))
    otras.pop(otras.index('energia_electrica'))
    otras.pop(otras.index('servicio_acueducto'))
    otras.pop(otras.index('servicio_alcantarillado'))
    otras.pop(otras.index('servicio_internet'))
    otras.pop(otras.index('descripcion_uso_vivienda'))
    otras.pop(otras.index('descripcion_tipo_vivienda'))
    otras.pop(otras.index('descripcion_condicion_ocupacion'))
    otras.pop(otras.index('descripcion_material_pared'))
    otras.pop(otras.index('descripcion_material_piso'))
    otras.pop(otras.index('descripcion_tipo_servicio_sanitario'))
    opcion_b = st.radio(label="      ",
                        options=otras)


    @st.cache
    def basuras_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotB, c = basuras_simple(datos, "total_hogares", opcion_b, opcion_nom)
    st.plotly_chart(plotB, use_container_width=True)

with colum3:
    otros = list(datos.columns)
    otros.pop(otros.index('Nom_municipio'))
    otros.pop(otros.index('total_hogares'))
    otros.pop(otros.index('estrato'))
    otros.pop(otros.index('servicio_acueducto'))
    otros.pop(otros.index('energia_electrica'))
    otros.pop(otros.index('servicio_gas'))
    otros.pop(otros.index('servicio_alcantarillado'))
    otros.pop(otros.index('recoleccion_basuras'))
    otros.pop(otros.index('descripcion_uso_vivienda'))
    otros.pop(otros.index('descripcion_tipo_vivienda'))
    otros.pop(otros.index('descripcion_condicion_ocupacion'))
    otros.pop(otros.index('descripcion_material_pared'))
    otros.pop(otros.index('descripcion_material_piso'))
    otros.pop(otros.index('descripcion_tipo_servicio_sanitario'))
    opcion_b = st.radio(label="           ",
                        options=otros)


    @st.cache
    def internet_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
        data = df.copy()
        data = data[data["Nom_municipio"] == Nom_municipio_filter]
        fig = px.pie(data, values=x, names=y, color_discrete_sequence=px.colors.sequential.Aggrnyl)
        return fig, data

    plotI, c = internet_simple(datos, "total_hogares", opcion_b, opcion_nom)
    st.plotly_chart(plotI, use_container_width=True)
