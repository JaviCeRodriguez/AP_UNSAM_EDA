import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(
    page_title="Participación",
    page_icon="✋",
    layout="wide",
)

st.title("Participación")

df_inicial = pd.read_excel('./data/inscriptos/INICIAL.xlsx')
st.dataframe(df_inicial)


st.write("""
## Geografía (por provincia)
""")

provincia_counts = df_inicial.PROVINCIA.value_counts()
df_provincia = pd.DataFrame({
    "Provincia": provincia_counts.index,
    "Cantidad": provincia_counts.values,
})
fig = px.bar(
    data_frame=df_provincia,
    y="Cantidad",
    x="Provincia",
    color="Provincia",
    title='Porcentaje de Estudiantes por Provincia'
)
st.plotly_chart(figure_or_data=fig, use_container_width=True)