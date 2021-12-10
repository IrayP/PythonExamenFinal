#Importar Pandas
import pandas as pd
from pandas.core.frame import DataFrame

#Crear una serie
#Crea una Serie de los numeros 10, 20 and 10.
s = pd.Series([10,20,10])
print(s)

#Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'.
p = pd.Series(['rojo','verde','azul'])
print(p)

# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df['Columna 1'] = s
print(df)

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df['Columna 2'] = p
print(df)

#Leer un dataframe
#Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
#El archivo está localizado en "data/avengers.csv"
ruta = "./pandas/avengers.csv"
avengers = pd.read_csv(ruta)

#Inspeccionar un dataframe
# Muestra las primeras 5 filas del DataFrame.
print(avengers.head(5))
# Muestra las primeras 10 filas del DataFrame. 
print(avengers.head(10))
# Muestra las últimas 5 filas del DataFrame.
print(avengers.tail(5))

#Tamaño del DataFrame
# Muestra el tamaño del DataFrame
print(avengers.shape)

#Data types en un DataFrame
#Muestra los data types del dataframe
print(avengers.dtypes)

#Editar el índice (index)
# Cambia el indice a la columna "fecha_inicio".
df_avengers = avengers.set_index("fecha_inicio").copy()
print(df_avengers.head())

#Ordenar el índice
# Ordena el índice de forma descendiente
print(df_avengers.sort_values(by="fecha_inicio",ascending=False))

#Resetear el índice
print(df_avengers.reset_index())