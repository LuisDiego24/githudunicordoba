import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

st.header("CENSO CORDOBA:")
st.sidebar.markdown("## OPCIONES")
st.sidebar.markdown("---")

@st.cache
def cargar_datos(filename:str):
    return pd.read_csv(filename)

datos = cargar_datos('depurado.csv')


lista_Nom_municipio = list(datos['Nom_municipio'].unique())
opcion_Nom_municipio = st.sidebar.selectbox(label="Selecione un municipio",
                                    options=lista_Nom_municipio)


otras_variables=list(datos.columns)
otras_variables.pop(otras_variables.index('Nom_municipio'))
otras_variables.pop(otras_variables.index('total_hogares'))

opcion_y = st.sidebar.selectbox(label="Selecione un servicio",
                                    options=otras_variables)

st.sidebar.markdown("---")

@st.cache
def plot_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = datos[datos["Nom_municipio"] == Nom_municipio_filter]
    fig = px.histogram(data, x=x, y=y)
    return fig, data


plot, d = plot_simple(datos, "total_hogares", opcion_y, opcion_Nom_municipio)
st.plotly_chart(plot,use_container_width=True)
st.write(d)


@st.cache
def pie_simple(df: pd.DataFrame, x: pd.DataFrame, y, Nom_municipio_filter: str):
    data = df.copy()
    data = data[data["Nom_municipio"] == Nom_municipio_filter]
    fig = px.pie(data, values=x, names=y)
    return fig, data


pl, c = pie_simple(datos, "total_hogares", opcion_y, opcion_Nom_municipio)
st.plotly_chart(pl,use_container_width=True)
st.write(c)
