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

st.dataframe(df_pe, use_container_width=True)
