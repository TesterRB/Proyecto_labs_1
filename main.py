from fastapi import FastAPI
import pandas as pd
import numpy as np
import uvicorn
import spacy

app = FastAPI()

# Importar el DataFrame
df = pd.read_csv('funciones/dfListo.csv')

#Codigo para la funcion de Machine Learning
muestra = df.sample(n=1000, random_state=42)
nlp = spacy.load("en_core_web_md")
docs = list(nlp.pipe(muestra["overview"].fillna("").values))
embedding_matrix = np.array([doc.vector for doc in docs])
cosine_sim = np.dot(embedding_matrix, embedding_matrix.T)
muestra = muestra.drop_duplicates().reset_index(drop=True)
indices = pd.Series(muestra.index, index=muestra['title'])

# Funciones
@app.get("/peliculas/mes/{mes}")
async def peliculas_mes(mes):
    df['release_date'] = pd.to_datetime(df['release_date'])
    
    if type(mes) == str:
        meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, 
                 "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}
        mes = mes.lower()
        if mes not in meses:
            raise ValueError("El mes ingresado no es válido.")
        mes = meses[mes]
    
    peliculas_mes = df[df['release_date'].dt.month == mes]
    cantidad = len(peliculas_mes)
    respuesta = {'mes': mes, 'cantidad': cantidad}
    return respuesta

@app.get("/peliculas/dia/{dia}")
async def peliculas_dia(dia):
    df['release_date'] = pd.to_datetime(df['release_date'])
    dias = {'Lunes': 0, 'Martes': 1, 'Miércoles': 2, 'Jueves': 3, 'Viernes': 4, 'Sábado': 5, 'Domingo': 6}
    nombre_dia = dia.capitalize()
    peliculas_dia = df[df['release_date'].dt.dayofweek == dias[nombre_dia]]
    cantidad = len(peliculas_dia)
    respuesta = {'dia': nombre_dia, 'cantidad': int(cantidad)}
    return respuesta

@app.get("/franquicia/{franquicia}")
async def franquicia(franquicia):
    peliculas_franquicia = df[df['name_collection'] == franquicia]
    cantidad = len(peliculas_franquicia)
    ganancia_total = peliculas_franquicia['revenue'].sum()
    ganancia_promedio = peliculas_franquicia['revenue'].mean()
    respuesta = {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}
    return respuesta

@app.get("/peliculas/pais/{pais}")
async def peliculas_pais(pais):
    peliculas_pais = df[df['name_countrie'] == pais]
    cantidad = len(peliculas_pais)
    respuesta = {'pais': pais, 'cantidad': cantidad}
    return respuesta

@app.get("/productoras/{productora}")
async def productoras(productora):
    # Filtrar el DataFrame por el nombre de la productora
    df_productora = df[df['name_production'] == productora]
    ganancia_total = df_productora['revenue'].sum()
    cantidad = df_productora['id'].count()
    respuesta = {'productora': productora, 'ganancia_total': int(ganancia_total), 'cantidad': int(cantidad)}
    
    return respuesta


@app.get("/retorno/{titulo}")
async def retorno(titulo):
    pelicula = df[df['title'] == titulo]
    inversion = pelicula['budget'].iloc[0]
    ganancia = pelicula['revenue'].iloc[0]
    retorno = pelicula['return'].iloc[0]
    anio = pelicula['release_year'].iloc[0]
    respuesta = {'pelicula': titulo, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': int(anio)}
    return respuesta


@app.get("/retorno/{titulo}")
async def recomendacion(title, cosine_sim=cosine_sim, muestra=muestra, indices=indices):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    peliculas_recomendadas = list(muestra.iloc[movie_indices]['title'])
    return {'peliculas_recomendadas': peliculas_recomendadas}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)