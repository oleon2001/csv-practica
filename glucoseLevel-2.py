import csv
import charts
import matplotlib.pyplot as plt




def readCsv(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile,delimiter=',')
        header = next(reader)
        print(header)
        data = []

        for row in reader:
            iterable = zip(header,row)
            pacientDict = {key:value for key,value in iterable}
            data.append(pacientDict)
        

    return data


def avgGlucoseLevel(data,gender):
    newData = data.copy()

    if str(gender).capitalize() == 'Male':

        genderDictList = list(filter(lambda x: x['gender'] == str(gender).capitalize(),newData))

    elif str(gender).capitalize() == 'Female':
        genderDictList = list(filter(lambda x: x['gender'] == str(gender).capitalize(),newData))
    
    pacientID = list(map(lambda y: y['id'],genderDictList))
    pacientGlucose = list(map(lambda x: float(x['avg_glucose_level']),genderDictList))

    dictGlucose = dict(zip(pacientID,pacientGlucose))
    

    return dictGlucose
    

def classifyPacients(dictionary):
    glucoseLevel = list(dictionary.values())
    normal = list(filter(lambda x: True if x>0 and x<=140 else False,glucoseLevel))
    print(normal)
    prediabetes = list(filter(lambda x: True if x>140 and x<=199 else False,glucoseLevel))
    diabetes = list(filter(lambda x: True if x>199 else False,glucoseLevel))

    labels = ['NORMAL','PREDIABETES','DIABETES']
    #values = [len(normal),len(prediabetes),len(diabetes)]
    values = [normal,prediabetes,diabetes]
    print(values)

    return labels,values

   
   
    


if __name__ == '__main__':
    data = readCsv(r'healthcareGlucose.csv')
    gender = input('Type the gender(Male/Female) to consult: ')
    dictionary = avgGlucoseLevel(data,gender)
    labels, values = classifyPacients(dictionary)
    
    # Crea una lista de puntos (x, y)
    points = []
    for i, label in enumerate(labels):
        for value in values[i]:
            points.append((label, value))
    print(points)
    
    '''
        points = []: Aquí se crea una lista vacía llamada points. Esta lista servirá para almacenar pares de datos, donde cada par consistirá en una etiqueta (o categoría) y un valor numérico.
        for i, label in enumerate(labels):: Este primer bucle for itera sobre la lista labels. La función enumerate nos permite obtener tanto el índice (i) de cada elemento como el valor del elemento (label) en cada iteración.
        for value in values[i]:: Este segundo bucle for anidado itera sobre los valores correspondientes a la etiqueta actual. La lista values es una lista de listas, donde cada sublista contiene los valores asociados a una etiqueta.
        points.append((label, value)): En cada iteración de los bucles, se agrega un nuevo par (tupla) a la lista points. La tupla contiene la etiqueta y el valor actual.

    Ejemplo:
    Si labels = ['A', 'B'] y values = [[1, 2, 3], [4, 5]], la lista points al final de esta parte sería:

    [('A', 1), ('A', 2), ('A', 3), ('B', 4), ('B', 5)]

    '''

    # Crea un gráfico de dispersión
    plt.scatter([x[0] for x in points], [x[1] for x in points])
    plt.xlabel('Categoría')
    plt.ylabel('Valor')
    plt.title('Distribución de valores por categoría')
    '''
    plt.scatter(...): Esta línea crea el gráfico de dispersión. Los argumentos de plt.scatter son las listas de coordenadas x e y de los puntos. En este caso:

        [x[0] for x in points]: Esta expresión de lista por comprensión extrae la primera coordenada (la etiqueta) de cada tupla en points y crea una nueva lista con esas etiquetas.
        [x[1] for x in points]: Esta expresión hace lo mismo, pero extrae la segunda coordenada (el valor) de cada tupla.

    plt.xlabel('Categoría'): Establece el título del eje x como "Categoría".
    plt.ylabel('Valor'): Establece el título del eje y como "Valor".
    plt.title('Distribución de valores por categoría'): Establece el título del gráfico.
    plt.show(): Muestra el gráfico en pantalla.
    '''
    plt.show()
