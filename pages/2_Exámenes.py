import streamlit as st
import pandas as pd
import re
import plotly.express as px
import plotly.graph_objects as go


def extraer_nota(nota):
    match = re.match(r'(\d+)\s*/\s*\d+', nota)
    if match:
        return int(match.group(1))
    else:
        return None


st.set_page_config(
    page_title="Exámenes",
    page_icon="📚",
    layout="wide",
)

st.write("""
# 📚 Exámenes

El objetivo de esta parte es observar los datos de exámenes en la Diplomatura en Ciencia de Datos, en cada una de 
sus etapas.

> _⚠️ El programa de esta diplomatura aún no finalizó! Pueden haber cambios en los próximos meses._
""")

df_pe_primer_examen = pd.read_excel('./data/examenes/1er_modulo/Notas-primer-examen.xlsx')
df_pe_segundo_examen = pd.read_excel('./data/examenes/1er_modulo/Nota-segundo-examen.xlsx')
df_pe_segundo_examen_martes = pd.read_excel('./data/examenes/1er_modulo/notas-segundo-Examen-martes.xlsx')
df_pe_primer_recu = pd.read_excel('./data/examenes/1er_modulo/Notas-recuperatorio.xlsx')
df_pe_segundo_recu = pd.read_excel('./data/examenes/1er_modulo/notas-recuperatorio-segundo-examen.xlsx')
df_se_primer_examen = pd.read_excel('./data/examenes/2do_modulo/notas-1examen-segundomodulo.xlsx')
df_se_segundo_examen = pd.read_excel('./data/examenes/2do_modulo/Notas-segundoexamen-modulo2.xlsx')
df_se_primer_recu = pd.read_excel('./data/examenes/2do_modulo/recuperatorio-primerparcial.xlsx')
df_se_segundo_recu = pd.read_excel('./data/examenes/2do_modulo/recuperatorio-segundo.xlsx')
df_te_primer_examen = pd.read_excel('./data/examenes/3er_modulo/notas-tercermodulo-primerexamen.xlsx')

df_pe_primer_examen = df_pe_primer_examen.assign(EXAMEN='primer')
df_pe_primer_examen = df_pe_primer_examen.assign(RECUPERATORIO=False)
df_pe_primer_examen = df_pe_primer_examen.assign(ETAPA='primera')
df_pe_primer_examen['NOTA'] = df_pe_primer_examen['NOTA'].apply(extraer_nota)
df_pe = df_pe_primer_examen[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]

df_pe_segundo_examen = df_pe_segundo_examen.assign(EXAMEN='segundo')
df_pe_segundo_examen = df_pe_segundo_examen.assign(RECUPERATORIO=False)
df_pe_segundo_examen = df_pe_segundo_examen.assign(ETAPA='primera')
df_pe_segundo_examen['NOTA'] = df_pe_segundo_examen['Nota Segundo examen']
df_pe_segundo_examen = df_pe_segundo_examen[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_pe_segundo_examen], ignore_index=True)

df_pe_segundo_examen_martes = df_pe_segundo_examen_martes.assign(EXAMEN='segundo')
df_pe_segundo_examen_martes = df_pe_segundo_examen_martes.assign(RECUPERATORIO=False)
df_pe_segundo_examen_martes = df_pe_segundo_examen_martes.assign(ETAPA='primera')
df_pe_segundo_examen_martes['NOTA'] = df_pe_segundo_examen_martes['Nota segundo Examen'].apply(extraer_nota)
df_pe_segundo_examen_martes = df_pe_segundo_examen_martes[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_pe_segundo_examen_martes], ignore_index=True)

df_pe_primer_recu = df_pe_primer_recu.assign(EXAMEN='primer')
df_pe_primer_recu = df_pe_primer_recu.assign(RECUPERATORIO=True)
df_pe_primer_recu = df_pe_primer_recu.assign(ETAPA='primera')
df_pe_primer_recu['NOTA'] = pd.to_numeric(df_pe_primer_recu['NOTA'], errors='coerce')
df_pe_primer_recu = df_pe_primer_recu[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_pe_primer_recu], ignore_index=True)

df_pe_segundo_recu = df_pe_segundo_recu.assign(EXAMEN='segundo')
df_pe_segundo_recu = df_pe_segundo_recu.assign(RECUPERATORIO=True)
df_pe_segundo_recu = df_pe_segundo_recu.assign(ETAPA='primera')
df_pe_segundo_recu['NOTA'] = df_pe_segundo_recu['Nota del recuperatorio']
df_pe_segundo_recu = df_pe_segundo_recu[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_pe_segundo_recu], ignore_index=True)

df_se_primer_examen = df_se_primer_examen.assign(EXAMEN='primer')
df_se_primer_examen = df_se_primer_examen.assign(RECUPERATORIO=False)
df_se_primer_examen = df_se_primer_examen.assign(ETAPA='segunda')
df_se_primer_examen['NOTA'] = pd.to_numeric(df_se_primer_examen['Puntuación'], errors='coerce')
df_se_primer_examen = df_se_primer_examen[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_se_primer_examen], ignore_index=True)

df_se_segundo_examen = df_se_segundo_examen.assign(EXAMEN='segundo')
df_se_segundo_examen = df_se_segundo_examen.assign(RECUPERATORIO=False)
df_se_segundo_examen = df_se_segundo_examen.assign(ETAPA='segunda')
df_se_segundo_examen = df_se_segundo_examen[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_se_segundo_examen], ignore_index=True)

df_se_primer_recu = df_se_primer_recu.assign(EXAMEN='primer')
df_se_primer_recu = df_se_primer_recu.assign(RECUPERATORIO=True)
df_se_primer_recu = df_se_primer_recu.assign(ETAPA='segunda')
df_se_primer_recu['NOTA'] = df_se_primer_recu['Nota']
df_se_primer_recu = df_se_primer_recu[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_se_primer_recu], ignore_index=True)

df_se_segundo_recu = df_se_segundo_recu.assign(EXAMEN='segundo')
df_se_segundo_recu = df_se_segundo_recu.assign(RECUPERATORIO=True)
df_se_segundo_recu = df_se_segundo_recu.assign(ETAPA='segunda')
df_se_segundo_recu = df_se_segundo_recu[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_se_segundo_recu], ignore_index=True)

df_te_primer_examen = df_te_primer_examen.assign(EXAMEN='primer')
df_te_primer_examen = df_te_primer_examen.assign(RECUPERATORIO=False)
df_te_primer_examen = df_te_primer_examen.assign(ETAPA='tercera')
df_te_primer_examen = df_te_primer_examen[['NOTA', 'EXAMEN', 'RECUPERATORIO', 'ETAPA']]
df_pe = pd.concat([df_pe, df_te_primer_examen], ignore_index=True)

df_pe['APRUEBA'] = df_pe['NOTA'].apply(lambda x: 'Si' if x >= 6 else 'No')

st.dataframe(df_pe, use_container_width=True)

st.write("""
## Notas por etapa

Veamos su distribución: En general (por el momento con solo el primer examen dado en la 3er etapa) hubo
mayor cantidad de aprobados en las últimas dos etapas. Solo en la primer etapa se observa que que la
frecuencia de notas crece paulatinamente, solo en la segunda y tercer etapa se nota un "salto" entre
aprobado y desparobado (la brecha es en nota 6).
""")

fig_notas_etapa = px.histogram(df_pe, x="NOTA", color="ETAPA", title="Distribución de Notas por Etapa")
fig_notas_etapa.update_xaxes(title_text="Nota")
fig_notas_etapa.update_yaxes(title_text="Frecuencia")
st.plotly_chart(fig_notas_etapa, use_container_width=True)


st.write("""
### Nota promedio según etapa, examen y si recupera o no

En este caso, realizamos el promedio de las notas según estas variables y las representamos separadas por
etapa, si rindió primer o segundo examen y si es recuperatorio o no. En todos los caso menos en el de
segundo examen recuperatorio de la segunda etapa, la nota promedio es mayor a 6.

Una conclusión de este caso particular mencionado es que el recuperatorio pudo haber tenido una complejida
mayor al del segundo examen (no recuperatorio) de la misma etapa.

Otra observación es que la tendencia del promedio de las notas baja a lo largo del tiempo. Esto podría ser
por el nivel del contenido que se va viendo en cada etapa como causante directa.
""")
nota_promedio_por_etapa_tipo_recuperatorio = df_pe.groupby(["ETAPA", "EXAMEN", "RECUPERATORIO"])["NOTA"].mean().reset_index()
nota_promedio_por_etapa_tipo_recuperatorio['RECUPERATORIO'] = nota_promedio_por_etapa_tipo_recuperatorio['RECUPERATORIO'].apply(lambda x: 'Si' if x else 'No')
fig_nota_etapa_examenes = px.bar(nota_promedio_por_etapa_tipo_recuperatorio, x="ETAPA", y="NOTA", color="EXAMEN",
             facet_col="RECUPERATORIO",
             title="Nota Promedio por Etapa, Tipo de Examen y Recuperatorio",
             labels={"ETAPA": "Etapa", "NOTA": "Nota Promedio", "EXAMEN": "Tipo de Examen", "RECUPERATORIO": "Recuperatorio"},
             barmode="group")
st.plotly_chart(fig_nota_etapa_examenes, use_container_width=True)


st.write("""
## Aprobación en cada etapa

Acá no hay mucho por comentar. Solo que, en cada etapa se mantiene el porcentaje de aprobación. Pero si tomaramos
en cuenta la cantidad de estudiantes que hay en cada etapa, el significado de estos porcentajes cambia.

Entonces podríamos concluir que el porcentaje de aprobación disminuye al avanzar en cada etapa (_y esto tendría
sentido si tomamos de referencia el gráfico anterior_)
""")
porcentaje_aprobacion_por_etapa = df_pe.groupby("ETAPA")["APRUEBA"].value_counts(normalize=True).unstack().fillna(0)
porcentaje_aprobacion_por_etapa.reset_index(inplace=True)
fig_aprobacion_etapa = px.bar(porcentaje_aprobacion_por_etapa, x="ETAPA", y=["Si", "No"],
             title="Porcentaje de Aprobación por Etapa",
             labels={"ETAPA": "Etapas", "value": "Porcentaje", "variable": "Aprueba"},
             color_discrete_sequence=["green", "red"])
st.plotly_chart(fig_aprobacion_etapa, use_container_width=True)


st.write("""
## Relación entre exámentes recuperatorios y aprobación

Acá queda en evidencia que la toma de exámenes recuperatorios es una estrategia efecto para mejorar
las posibilidades de aprobación. Los estudiantes que aprobaro nsin tomar recuperatorios también es un
factor a tener en cuenta, ya que destaca que obtuvieron un buen desempeño en los exámenes.
""")
relacion_recuperatorios_aprobacion = df_pe.groupby(["RECUPERATORIO", "APRUEBA"]).size().unstack(fill_value=0).reset_index()
relacion_recuperatorios_aprobacion['RECUPERATORIO'] = relacion_recuperatorios_aprobacion['RECUPERATORIO'].apply(lambda x: 'Si' if x else 'No')
fig_relacion_recu_aprobacion = px.bar(relacion_recuperatorios_aprobacion, x="RECUPERATORIO", y=["Si", "No"],
             title="Relación entre Toma de Recuperatorios y Aprobación",
             labels={"RECUPERATORIO": "Recuperatorio", "variable": "Aprobación", "value": "Cantidad"},
             barmode="group")
st.plotly_chart(fig_relacion_recu_aprobacion, use_container_width=True)