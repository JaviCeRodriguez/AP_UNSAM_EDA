import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Participación",
    page_icon="✋",
    layout="wide",
)

st.title("✋ Participación")

df_inicial = pd.read_excel('./data/inscriptos/INICIAL.xlsx')

# Limpieza de valores erróneos
provincias_no_validas = ['LA PLATA', 'EXALTACION DE LA CRUZ']
df_inicial.PROVINCIA.replace(provincias_no_validas, 'BUENOS AIRES', inplace=True)

st.dataframe(data=df_inicial, use_container_width=True)

st.write("""
## 👶 Participación inicial

Observemos los datos de participación al programa inicialmente. Se incluyen a todos los estudiantes que realizaron la
inscripción, hayan rendido o no, o abandaron antes de arrancar.
""")

st.write("### Geografía (por provincia)")

provincia_counts = df_inicial.PROVINCIA.value_counts()
df_provincia = pd.DataFrame({
    "Provincia": provincia_counts.index,
    "Cantidad": provincia_counts.values,
})
fig_participacion = px.bar(
    data_frame=df_provincia,
    y="Cantidad",
    x="Provincia",
    color="Provincia",
    title='Cantidad de estudiantes por Provincia'
)
st.plotly_chart(figure_or_data=fig_participacion, use_container_width=True)


st.write("### Nivel educativo")

edu_counts = df_inicial.NIVELEDUCATIVO.value_counts()
df_edu = pd.DataFrame({
    "Nivel educativo": edu_counts.index,
    "Cantidad": edu_counts.values
})
fig_edu = px.bar(
    data_frame=df_edu,
    y="Cantidad",
    x="Nivel educativo",
    color="Nivel educativo",
    title='Cantidad de estudiantes por Nivel educativo'
)
st.plotly_chart(figure_or_data=fig_edu, use_container_width=True)


st.write(""""
## 👴 Participación final (3er módulo)

Observemos los datos de participación en el último módulo hasta el día 08/09/2023.
""")