# Proyecto de Análisis y Recomendación de Películas

Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) y desarrollar un modelo de recomendación de películas utilizando técnicas de Machine Learning.

## EDA (Análisis Exploratorio de Datos)

1. Importación de librerías: Se importaron las librerías necesarias para el proyecto, como Pandas, NumPy y Spacy.
2. Carga del archivo CSV: Se cargó el archivo CSV que contiene los datos de películas.
3. Visualización de las primeras filas del DataFrame: Se mostraron las primeras filas del DataFrame para tener una idea de la estructura de los datos.
4. Estadísticas descriptivas: Se obtuvieron estadísticas descriptivas de las columnas numéricas del DataFrame.
5. Gráfico de valores nulos: Se generó un gráfico para visualizar la cantidad de valores nulos en el DataFrame.
6. Distribución de variables numéricas: Se analizó la distribución de las variables numéricas mediante gráficos.
7. Correlación entre variables numéricas: Se calculó la matriz de correlación y se visualizó en un mapa de calor.
8. Distribución de variables categóricas: Se exploró la distribución de las variables categóricas mediante gráficos.
9. Cantidad de películas por idioma: Se analizó la cantidad de películas en cada idioma utilizando una muestra de 1000 filas.
10. Longitud promedio de los resúmenes: Se calculó la longitud promedio de los resúmenes de las películas.
11. Películas con slogan: Se determinó la cantidad de películas que cuentan con un slogan.
12. Películas por género: Se analizó la cantidad de películas producidas por género.
13. Películas por estudio de producción: Se determinó cuántas películas ha producido cada estudio de producción hasta el momento.
14. Películas por país: Se analizó la cantidad de películas producidas por país.
15. Gráfico resumen: Se creó un gráfico resumen que muestra diferentes estadísticas y distribuciones.

## Modelo de Recomendación de Películas

Modelo de Recomendación de Películas

Se desarrolló un modelo de recomendación de películas utilizando técnicas de Machine Learning. El modelo utiliza información de resúmenes de películas para calcular la similitud entre ellas y generar recomendaciones personalizadas.

Para construir el modelo, se realizaron los siguientes pasos:

Importación de librerías: Se importaron las librerías necesarias, como NumPy, Pandas y Spacy.
Carga del archivo CSV: Se cargó el archivo CSV que contiene los datos de películas en un DataFrame.
Preprocesamiento de datos: Se seleccionó una muestra aleatoria de 1000 películas del DataFrame para reducir la carga computacional. Además, se utilizó el modelo pre-entrenado de Spacy ("en_core_web_md") para obtener representaciones vectoriales de los resúmenes de las películas.
Cálculo de la matriz de similitud: Se calculó la similitud coseno entre los vectores de los resúmenes utilizando la matriz de embeddings generada. Esto permite medir la similitud entre los resúmenes de todas las películas en la muestra.
Generación de recomendaciones: Se implementó la función get_similar_movies(title) que recibe el título de una película y devuelve una lista de las 5 películas más similares basadas en la similitud coseno. Las recomendaciones se basan en la similitud de los resúmenes de las películas.
Ejemplo de uso del modelo:

- `recommended_movies = get_similar_movies('Título de la película')`
- `print(recommended_movies)`

El modelo proporcionará una lista de las películas más similares a la película especificada, lo que puede ayudar a los usuarios a descubrir películas relacionadas o similares a sus preferencias.

Recuerda ajustar el código del modelo a tu necesidad, asegurándote de utilizar los datos adecuados y adaptar los parámetros según corresponda.

## Uso de la API

La API proporciona diferentes endpoints para realizar consultas y obtener información sobre las películas. Los endpoints disponibles son:

- `/peliculas/mes/{mes}`: Devuelve la cantidad de películas lanzadas en un mes específico.
- `/peliculas/dia/{dia}`: Devuelve la cantidad de películas lanzadas en un día de la semana específico.
- `/franquicia/{franquicia}`: Devuelve información sobre una franquicia de películas, incluyendo la cantidad total de películas y las ganancias.
- `/peliculas/pais/{pais}`: Devuelve la cantidad de películas producidas en un país específico.
- `/productoras/{productora}`: Devuelve información sobre una productora de películas, incluyendo la cantidad de películas producidasy las ganancias totales.

/retorno/{titulo}: Devuelve información sobre la inversión, ganancia y retorno de una película específica.
/recomendacion/{titulo}: Devuelve una lista de películas recomendadas basadas en la similitud con una película específica.
Ejecución de la Aplicación
La aplicación se ejecuta utilizando el framework FastAPI. Para ejecutar la aplicación, se debe utilizar el siguiente comando:
uvicorn main:app --reload
La aplicación estará disponible en http://localhost:8000.
