from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Importar el DataFrame
df = pd.read_csv('dfListo.csv')

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
    peliculas_dia = df[df['release_date'].dt.day == dia]
    cantidad = len(peliculas_dia)
    respuesta = {'dia': dia, 'cantidad': cantidad}
    return respuesta

@app.get("/franquicia/{franquicia}")
async def franquicia(franquicia):
    peliculas_franquicia = df[df['name_collection'] == franquicia]
    cantidad = len(peliculas_franquicia)
    ganancia_total = peliculas_franquicia['return'].sum()
    ganancia_promedio = peliculas_franquicia['return'].mean()
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
    ganancia_total = df_productora['return'].sum()
    cantidad = df_productora['id'].count()
    respuesta = {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}
    
    return respuesta


@app.get("/retorno/{titulo}")
async def retorno(titulo):
    pelicula = df[df['title'] == titulo]
    inversion = pelicula['budget'].iloc[0]
    ganancia = pelicula['revenue'].iloc[0]
    retorno = (ganancia - inversion) / inversion if inversion != 0 else 0
    anio = int(pelicula['release_date'].iloc)

