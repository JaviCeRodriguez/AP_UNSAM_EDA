import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="🏠",
    layout="wide",
)

st.header("Argentina Programa 4.0 🤝 UNSAM")
st.subheader("Programa de capacitación en Ciencia de Datos para toda la Argentina")

st.write("""
Esta web app fue hecha con el único objetivo de completar el desafío de visualización de datos planteado dentro del programa.

Verán gráficos seleccionados que tratan de mostrar el progreso y estado de los estudiantes desde varias aristas según los datasets dados lo permitían.

Por el momento, se hizo únicamente análisis exploratorio (EDA). Pero, si usted quiere, puede contribuir a la expansión de esta app y cubrir también otros temas vistos como crear algún modelo de ML o clusterizar los datos para obtener otras métricas de utilidad. Para esto, puede acceder al [repositorio](https://github.com/JaviCeRodriguez/AP_UNSAM_EDA) y subir nuevos cambios que ayuden a visibilizar mejor la participación y rendimiento de los estudiantes.

En caso de que no sepa como empezar a contribuir, puede contactarme (los medios de contacto los encontrará en [mi perfil de GitHub](https://github.com/JaviCeRodriguez)).
""")

st.divider()

st.write("*Para ver el análisis realizado, seleccione una de las opciones del menú de la izquierda!*")

st.divider()

st.write("## Un breve repaso de que trata el programa...")

col1_et1, col2_et1 = st.columns(2)
col1_et2, col2_et2 = st.columns(2)
col1_et3, col2_et3 = st.columns(2)

col1_et1.write("""
### :green[Introducción - Programación en Python]

- El entorno y las variables: Diferentes entornos de programación Python (consola, IDE, notebooks). Sintaxis del lenguaje. Tipos de datos básicos. Funciones y su documentación.
- Estructuras de control: Condicionales. Iteraciones. Comprehensión de listas. Recursión.
- Estructuras de datos: Diccionarios, listas, tuplas, vectores, matrices y árboles.
- Programación orientada a objetos: Concepto de objeto. Métodos. Herencia.
- Python para el análisis de datos: Archivos de entrada/salida. Cómputo de estadísticos. Regresión lineal.
- Visualización de datos. Aplicaciones con Numpy, SciPy y Matplotlib.
- Testeo y Debuggeo de programas: Diseño de experimentos. Manejos de excepciones. Control de flujos.
- Introducción a la complejidad de algoritmos: Concepto de complejidad. Algoritmos de búsqueda. Algoritmos de ordenamiento.
- Aplicaciones de la programación a diversos ámbitos: Negocios, finanzas, seguros, ciencia.
""")

col2_et1.image("https://i.ibb.co/280VCCH/snake.png")

col1_et2.image("https://i.ibb.co/yFFMzx0/pcbits.png")

col2_et2.write("""
### :orange[Intermedio - Ciencia de Datos]

#### Elementos de matemática y probabilidad

- Elementos de Cálculo y Algebra. Funciones. Vectores y Matrices. Nociones de derivadas e integrales.
- Definición de probabilidad. Probabilidad conjunta, marginal y condicional. Leyes de la probabilidad.
- La interpretación frecuentista y bayesiana de la probabilidad.
- Distribuciones especiales: Binomial, Poisson, Gaussiana.
- Estimadores, estimación de máxima verosimilitud.

#### Análisis Exploratorio de Datos

- Programación, exploración y visualización de datos: histogramas, gráficos de caja, gráficos QQ, gráficos de dispersión. Librerías de Python.
- Preparación de datos; imputación de valores perdidos; codificación de variables categóricas.
- Técnicas de reducción de la dimensionalidad. Análisis de componentes principales.
- Algoritmos de clustering (aprendizaje no supervisado): K-means, K-vecinos más cercanos.

#### Introducción al Aprendizaje automático

- Fundamentos del aprendizaje automático.
- Entrenamiento, validación y prueba. Selección, extracción e ingeniería de características.
- Overfitting y Cross-validation. K-folding y leave-one-out CV.
- Modelos de regresión. Regresión lineal y regresión polinómica.
- Modelos de regresión regularizada.
- Modelos de clasificación. Perceptrón, regresión logística y árboles de decisión.
""")

col1_et3.write("""
### :blue[Especialización - Aprendizaje Automático]

#### Algoritmos avanzados de aprendizaje automático

- Support Vector Machines.
- Equilibrio sesgo-varianza.
- Métodos de ensamble. Bagging y stacking. Random Forest.
- Métodos de Boosting. Métodos de árboles. Gradient Boosting.

#### Redes neuronales
- Redes neuronales feed-forward. Métodos de Deep Learning.
- Entrenamiento de redes. Regularización.
- Redes neuronales convolucionales en aprendizaje de imágenes.
- Interpretabilidad. Aprendizaje por transferencia.

#### Deep Learning y Aplicaciones

- Autoenconders. Autoenconders variacionales. Redes Generativas Antagónicas (GANs).
- Redes neuronales recurrentes.
- Reinforcement Learning.
- Procesamiento de Texto y Lenguaje Natural.
- Aplicaciones en contextos comerciales, científicos, financieros, médicos y otros.
""")

col2_et3.image("https://i.ibb.co/bKgd9pf/robot.png")