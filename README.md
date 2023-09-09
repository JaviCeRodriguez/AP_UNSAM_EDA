# Desafío Argentina Programa - UNSAM

[Daniel de Florian y su equipo](https://argentinaprograma.unsam.edu.ar/paginas/equipo) nos propusieron un desafío:

> Les proponemos un desafio simple. Aqui van dos listas de alumnos (sin datos personales, obviamente), donde pueden encontrar edad, genero, nivel educativo, provincia, etc. Una es de quienes se inscribieron para el curso (muchos de ellos no llegaron a cursar), y la otra de quienes estan cursando el tercer módulo. A ver quienes hacen los analisis y graficos mas interesantes con esos datos, a los mejores los mostramos el miercoles.

Nos proporcionan datos sobre las notas de los examenes en cada módulo, a demás de los mencionados arriba.


## Cómo ejecutar el proyecto

Desde la terminal, realizar los siguientes pasos para preparar el entorno de trabajo:

```sh
>>> git clone https://github.com/JaviCeRodriguez/AP_UNSAM_EDA.git
>>> cd ./AP_UNSAM_EDA
>>> python -m virtualenv venv
>>> venv/Scripts/activate # En Linux: source venv/bin/activate
(venv) >>> pip install -r requirements.txt 
```

Una vez hecho esto, tendremos preparado el entorno para ejecutar el proyecto de forma local. Viene preparado para poder usar Jupyter Lab:

```sh
(venv) >>> jupyter lab
```

Pueden ejecutar notebooks con la interfaz de Jupyter de esta forma.

Pero, el proyecto core es para Streamlit. Esta librería crea una web app en pocos pasos. Para conocer como funciona, entren a la documentación. Para levantar el proyecto, ejecuten lo siguiente en terminal:

```sh
(venv) >>> streamlit run Inicio.py
```