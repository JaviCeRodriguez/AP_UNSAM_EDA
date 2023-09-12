import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
df_tercer_modulo = pd.read_excel('./data/inscriptos/alumnos-tercermodulo.xlsx')

# Limpieza de valores erróneos
provincias_no_validas = ['LA PLATA', 'EXALTACION DE LA CRUZ']
df_inicial.PROVINCIA.replace(provincias_no_validas, 'BUENOS AIRES', inplace=True)
bins = [0, 18, 30, 40, 50, 60, 70, float('inf')]
labels = ['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70+']
df_inicial['EDAD_RANGO'] = pd.cut(df_inicial['EDAD'], bins=bins, labels=labels, right=False)

with st.expander("Abrir para ver los datos!"):
    st.caption("Datos de inscripción inicial en el programa")
    st.dataframe(data=df_inicial, use_container_width=True)
    st.divider()
    st.caption("Datos de estudiantes en el 3er módulo del programa")
    st.dataframe(data=df_tercer_modulo, use_container_width=True)

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


st.write("### Cantidad de estudiantes regulares")
st.write("""Tratemos de visibilizar la cantidad de estudiantes que al menos realizaron el primer examen (SI) contra los
que abandonaron antes rendir (NO) y los que abandonaron antes de comenzar la cursada (NO COMENZO EL CURSO)""")
selected_regularidad = st.multiselect(
    label="Selecciona los estados",
    options=df_inicial["REGULAR"].unique(),
    default=df_inicial["REGULAR"].unique()
)

df_filter_regular = df_inicial[df_inicial["REGULAR"].isin(selected_regularidad)]
df_counts_regular = df_filter_regular.groupby(['REGULAR', 'EDAD_RANGO']).size().unstack(fill_value=0)
fig_regularidad = go.Figure()

for edad_rango in df_counts_regular.columns:
    fig_regularidad.add_trace(go.Bar(
        x=df_counts_regular.index,
        y=df_counts_regular[edad_rango],
        name=edad_rango,
    ))
fig_regularidad.update_layout(
    barmode='group',  # Para agrupar las barras
    xaxis_title='Regularidad',
    yaxis_title='Cantidad',
    title='Distribución de Estudiantes por Regularidad y Rango de Edad',
)
st.plotly_chart(fig_regularidad, use_container_width=True)


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


st.divider()

st.write("""
## 🧐 Participación final (3er módulo)

Observemos los datos de participación en el último módulo hasta el día 08/09/2023.

Se hará el análisis del nivel de participación con respecto a la inscripción de los datos vistos anteriormente. Se
tomarán en cuenta solamente alumnos regulares solamente.
""")
colors = {
    'Primer Módulo': 'rgb(253, 180, 98)',   # Naranja claro
    'Tercer Módulo': 'rgb(109, 105, 255)',  # Azul claro
}
# Hago transformación y limpieza de datos
df_regulares_inicial = df_inicial[df_inicial["REGULAR"] == "SI"]
df_regulares_inicial.rename(columns={
    'NIVELEDUCATIVO': 'NIVEL_EDUCATIVO',
    'TRABAJAACTUALMENTE': 'TRABAJA_ACTUALMENTE'
}, inplace=True)

outlier_index = df_tercer_modulo[df_tercer_modulo['EDAD'] == 123].index
df_tercer_modulo = df_tercer_modulo.drop(outlier_index)

st.write("""
### Comparación de Distribución demográfica

Analizamos por Género, Edad o Nivel educativo a los estudiantes. Se pueden hacer ciertas observaciones a partir de lo visto:

- :green[Hay mayor retención de estudiantes con terciario completo o más]
- :green[En cada género más de la mitad siguieron con el programa]
- :green[Hubo mayor retención en estudiantes mayores de 38 años aproximádamente]. Esto puede deberse a que a estas
edades, por lo general, los estudiantes no están realizando una formación académica.
""")

option = st.selectbox(
    'Selecciona la variable demográfica para comparar:',
    ('GENERO', 'EDAD', 'NIVEL_EDUCATIVO')
)


def create_comparison_chart(data_inicial, data_tercer_modulo, variable):
    fig_comp = go.Figure()
    for label, df in [('Primer Módulo', data_inicial), ('Tercer Módulo', data_tercer_modulo)]:
        fig_comp.add_trace(go.Histogram(x=df[variable], name=label, marker=dict(color=colors[label])))
    fig_comp.update_layout(barmode='overlay', title=f'Comparación de Distribución por {variable}')
    return fig_comp


if option == 'GENERO':
    chart = create_comparison_chart(df_regulares_inicial, df_tercer_modulo, option)
    st.plotly_chart(chart, use_container_width=True)
elif option == 'EDAD':
    chart = create_comparison_chart(df_regulares_inicial, df_tercer_modulo, 'EDAD')
    st.plotly_chart(chart, use_container_width=True)
else:
    chart = create_comparison_chart(df_regulares_inicial, df_tercer_modulo, 'NIVEL_EDUCATIVO')
    st.plotly_chart(chart, use_container_width=True)


st.write(f"### Distribución de Edades para visualizar situación laboral")
selected_situation = st.selectbox(
    placeholder='Selecciona la situación laboral',
    options=df_regulares_inicial['TRABAJA_ACTUALMENTE'].unique(),
    label="Selecciona la situación laboral (SI: tiene trabajo. NO: no tiene trabajo)"
)

filtered_data_tercer_modulo = df_tercer_modulo[df_tercer_modulo['TRABAJA_ACTUALMENTE'] == selected_situation]
filtered_data_regulares_inicial = df_regulares_inicial[df_regulares_inicial['TRABAJA_ACTUALMENTE'] == selected_situation]
filtered_data_tercer_modulo['Grupo'] = 'Tercer Módulo'
filtered_data_regulares_inicial['Grupo'] = 'Primer Módulo'
combined_data = pd.concat([filtered_data_tercer_modulo, filtered_data_regulares_inicial])

fig = px.histogram(
    combined_data,
    x='EDAD',
    color='Grupo',
    title=f'Distribución de Edades para {selected_situation}',
    color_discrete_map=colors
)
fig.update_layout(xaxis_title='Edad', yaxis_title='Cantidad')
st.plotly_chart(fig, use_container_width=True)

# Calcula y muestra estadísticas adicionales, como el promedio de edad y la cantidad total para ambos DataFrames
average_age_tercer_modulo = filtered_data_tercer_modulo['EDAD'].mean()
total_count_tercer_modulo = len(filtered_data_tercer_modulo)

average_age_regulares_inicial = filtered_data_regulares_inicial['EDAD'].mean()
total_count_regulares_inicial = len(filtered_data_regulares_inicial)


col1, col2 = st.columns(2)

col1.write(f"Promedio de Edad para {selected_situation} (Tercer Módulo): {average_age_tercer_modulo:.2f} años")
col1.write(f"Total de Estudiantes para {selected_situation} (Tercer Módulo): {total_count_tercer_modulo}")

col2.write(f"Promedio de Edad para {selected_situation} (Primer Módulo): {average_age_regulares_inicial:.2f} años")
col2.write(f"Total de Estudiantes para {selected_situation} (Primer Módulo): {total_count_regulares_inicial}")