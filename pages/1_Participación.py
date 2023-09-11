import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Participación",
    page_icon="✋",
    layout="wide",
)

st.write("""
# ✋ Participación

El objetivo de esta parte es observar los datos de inscripción en la Diplomatura en Ciencia de Datos, desde el momento
de inscripción hasta el primer parcial de 3er módulo.

> _⚠️ El programa de esta diplomatura aún no finalizó! Pueden haber cambios en los próximos meses._
""")

df_inicial = pd.read_excel('./data/inscriptos/INICIAL.xlsx')

# Limpieza de valores erróneos
provincias_no_validas = ['LA PLATA', 'EXALTACION DE LA CRUZ']
df_inicial.PROVINCIA.replace(provincias_no_validas, 'BUENOS AIRES', inplace=True)
bins = [0, 18, 30, 40, 50, 60, 70, float('inf')]
labels = ['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70+']
df_inicial['EDAD_RANGO'] = pd.cut(df_inicial['EDAD'], bins=bins, labels=labels, right=False)

with st.expander("Abrir para ver los datos!"):
    st.caption("Datos de inscripción inicial en el programa")
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


st.write("### Géneros y edades")
selected_generos = st.multiselect(
    label="Selecciona los géneros",
    options=df_inicial["GENERO"].unique(),
    default=df_inicial["GENERO"].unique()
)
df_filtered = df_inicial[df_inicial["GENERO"].isin(selected_generos)]
df_counts = df_filtered.groupby(['GENERO', 'EDAD_RANGO']).size().unstack(fill_value=0)
fig_edad = go.Figure()
for edad_rango in df_counts.columns:
    fig_edad.add_trace(go.Bar(
        x=df_counts.index,
        y=df_counts[edad_rango],
        name=edad_rango,
    ))
fig_edad.update_layout(
    xaxis_title='Género',
    yaxis_title='Cantidad',
    title='Distribución de Rangos de Edades por Género (Cantidad)',
)
st.plotly_chart(fig_edad, use_container_width=True)


st.write("### Regularidad por edad y nivel educativo")
selected_niveles = st.multiselect(
    label="Selecciona niveles educativos",
    options=df_inicial["NIVELEDUCATIVO"].unique(),
    default=["UNIVERSITARIO COMPLETO", "SECUNDARIO COMPLETO"]
)
fig_regularidad = px.violin(
    data_frame=df_inicial[df_inicial["NIVELEDUCATIVO"].isin(selected_niveles)],
    x="NIVELEDUCATIVO",
    y="EDAD_RANGO",
    color="REGULAR",
    category_orders={"NIVELEDUCATIVO": ["UNIVERSITARIO COMPLETO", "SECUNDARIO COMPLETO"]},
)
for nivel_educativo in df_inicial["NIVELEDUCATIVO"].unique():
    visibility = True if nivel_educativo in selected_niveles else "legendonly"
    fig_regularidad.for_each_trace(lambda trace: trace.update(visible=visibility) if trace.name == nivel_educativo else ())
st.plotly_chart(fig_regularidad, use_container_width=True)

st.write("""
## 👴 Participación final (3er módulo)

Observemos los datos de participación en el último módulo hasta el día 08/09/2023.
""")
