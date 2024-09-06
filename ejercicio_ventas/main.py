import numpy as np
import matplotlib as mp
import pandas as pd
import charts as ch

def run():
    df = pd.read_csv(r'ejercicio_ventas/ventas.csv')
    df['total_ventas']=df.apply(lambda x: x['Cantidad'] * x['Precio_Unitario'], axis=1)
    sumastotales=df['total_ventas'].agg(['min','max'])
    #print(df)
    #print(sumastotales)
    print(df['total_ventas'].sum())
    
    labels = []
    for i in range(len(df)):
        labels.append(df.index[i])
    
    values = df['total_ventas']
    #ch.generateBarChart(labels=labels, values=values)

if __name__ == '__main__':
    run() 
    