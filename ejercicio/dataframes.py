import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("/home/oleon/Escritorio/platzi/ccvPrueba/ejercicio/Electric_Vehicle_Population_Data.csv")


print(df.head())

#print(df.columns)

valores=df.groupby('City').agg({'Legislative District':['min','max']})

print(valores)
