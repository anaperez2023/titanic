# LIBRERÍAS
import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px

# CONFIGURACIÓN DE LA PÁGINA# 
layout='centered' or 'wide' 
st.set_page_config(page_title="Titanic", layout="wide", page_icon="🚢")
# Esto es para no mostrar los errores de deprecation en pyplot al usuario
st.set_option("deprecation.showPyplotGlobalUse", False)

#### LOGO
col1, col2, col3 = st.columns(3)
with col1:
    st.title("Titanic")
with col2:
    st.image(
"img/logo.jpg",
        width=500,
    )

with col2:
    st.title("")
    

# COSAS QUE VAMOS A USAR EN TODA LA PÁGINA
df = pd.read_csv(r"data/titanic.csv")


#### SIDEBAR
st.sidebar.image("img/logo.jpg",width=150)
st.sidebar.title("Menú")

# CONTENIDO
dfcopy = df.copy()
st.dataframe(dfcopy)


# Header 2, texto justificado, color blanco
st.markdown("""<h2 style='text-align: justify; color: white;'>Gráficos</h2>""", unsafe_allow_html=True)

st.text("Edad de los pasajeros")
fig = px.histogram(dfcopy, x="Age", nbins=50, color_discrete_sequence=["#ef553b"])
st.plotly_chart(fig,use_container_width=True)


st.text("Survivors / Deceased")
total = len(dfcopy)
sobrevivieron = df['Survived'].sum()
no_sobrevivieron = total - sobrevivieron
porcentaje_sobrevivieron = sobrevivieron / total * 100
porcentaje_no_sobrevivieron = no_sobrevivieron / total * 100
fig2 = px.pie(names=['Survivors', 'Deceased'], values=[porcentaje_sobrevivieron, porcentaje_no_sobrevivieron])
fig2.update_traces(textposition='outside', textinfo='percent+label')
st.plotly_chart(fig2,use_container_width=True)


# EL SEÑOR QUIQUE NO ME DEJA BORRAR
# st.text("Survivors by number")
# colors = ['#FF4136', '#636EFB']
# fig3 = px.bar(dfcopy, x='Survived', color='Survived', title='Supervivientes del Titanic',
#              color_discrete_sequence=colors)
# st.plotly_chart(fig3,use_container_width=True)


st.text("Survivors / Deceased")
colors = ['#FF4136', '#636EFB']
fig4 = px.bar(dfcopy, x='Embarked', color='Sex', title='Pasajeros embarcados en cada puerto',
             color_discrete_sequence=colors)
st.plotly_chart(fig4,use_container_width=True)

