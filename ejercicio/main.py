import pandas as pd
import numpy as np
import charts2 as ch

df=pd.read_csv("/home/oleon/Escritorio/platzi/ccvPrueba/ejercicio/Electric_Vehicle_Population_Data.csv")
'''
df.head()
df.info()
df.describe()
df.isnull().sum()
'''
#print(df.head())


#funciones
def run():
    df=df[df['City']=='Everett']
    countries=df['Model'].values
    utilidadElectrica= df['Legislative District'].values
    ch.generateBarChart(countries,utilidadElectrica)
    ch.generatePieChart(countries,utilidadElectrica)
    #print(df.columns=='City')
    #print(df.columns)
    #valores=df.groupby(['City']).count()
    #print(valores)


if __name__ == '__main__':
 run()