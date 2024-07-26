import numpy as np
import pandas as pd

lista_numeros=np.random.randint(1,100,(10))
arr=np.array(lista_numeros)
print(arr)

lista_numeros2=np.random.randint(1,100,(100))
arr2=np.array(lista_numeros2)
print(arr2) 



def Numeros_pares(x):
    return arr[arr%2==0]

print(Numeros_pares(arr))



def controlDeflujo(numero):
    for x in  numero:
        if x%3==0:
            print('Fizz')
        elif x%5==0:
            print('Buzz')
        else:
            print(x)
        

print(controlDeflujo(lista_numeros2))

    