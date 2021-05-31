#Aplicación web para análisis exploratorio de datos. Adaptada de: https://towardsdatascience.com/how-to-build-an-eda-app-in-python-af7ec4b51528

#Se importan las librerias necesarias, numpy y pandas para el trabajo con datos
#Streamlit una bibloteca usada pra facilitar la creación de aplicaciones web y pandas_profiling una extensión de pandas para 
#facilitar la creación de reportes rapidos de análisis de datos
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# El titulo de la aplicación
st.markdown('''
# **Aplicación para análisis exploratorio de datos**
Está es una **Aplicación para análisis exploratorio de datos(EDA)** creada en Streamlit usando la libreria **pandas-profiling**.
Aplicación construida en `Python` + `Streamlit` por [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) 
---
''')

# Carga del archivo CSV
#Se muestran mensajes y botones para cargar el archivo
with st.sidebar.header('1. Sube tu archivo .CSV'):
    uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])
    st.sidebar.markdown("""
[Ejemplo usando un archivo CSV de prueba](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

#Reporte usando Pandas Profiling
#Si un archivo CSV ha sido cargado se procede a leerlo
if uploaded_file is not None:
    #Función para leer un archivo CSV
    #El decorador @ st.cache permite que la aplicación omita una ejecución potencialmente costosa de las siguientes líneas de código
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    #Se asigna el contenido del archivo leido a la variable df    
    df = load_csv()
    #Se asigna la funcionalidad de ProfileReport a la variable pr
    pr = ProfileReport(df, explorative=True)

    #Se muestra el resultado del reporte creado
    st.header('**Dataframe cargado**')
    st.write(df)
    st.write('---')
    st.header('**Reporte con Pandas Profiling**')
    #Genera el reporte HTML interactivoq que permite el analisis exploratorio de los datos
    st_profile_report(pr)
#Si no se carga ningun archivo se indica que se está a la espera de uno
else:
    st.info('Esperando para cargar un archivo CSV.')
    if st.button('Presione para usar un Dataset de Ejemplo'):
        # Se crean datos de prueba creados con NumPy y conformados por 5 columnas
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        #Se genera un reporte con los datos de prueba creados
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Dataframe cargado**')
        st.write(df)
        st.write('---')
        st.header('**Reporte con Pandas Profiling**')
        st_profile_report(pr)
#La aplicación se corre ejecutando streamlit run app.py