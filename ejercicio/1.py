import pandas as pd
import numpy as np
import charts as ch

df=pd.read_csv("/home/oleon/Escritorio/platzi/ccvPrueba/ejercicio/Electric_Vehicle_Population_Data.csv")
'''
df.head()
df.info()
df.describe()
df.isnull().sum()
'''
#print(df.head())


#funciones
df=df[df['city']=='Everett']
countries=df['city'].values
utilidadElectrica= df['Electric Utility 2020 Census Tract'].values






