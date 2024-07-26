import matplotlib.pyplot as plt
'''
def generateBarChart(labels, values, colors=None, hatch=None):
    """
    Genera un gráfico de barras con los valores y etiquetas proporcionados.

    Args:
        labels (list): Etiquetas para las barras.
        values (list): Valores para las barras.
        colors (list, optional): Colores para las barras. Defaults to None.
        hatch (list, optional): Patrones de sombreado para las barras. Defaults to None.
    """
    fig, ax = plt.subplots()
    if colors is not None:
        for i, (label, value, color) in enumerate(zip(labels, values, colors)):
            ax.bar(label, value, color=color, hatch=hatch[i] if hatch else None)
    else:
        ax.bar(labels, values)
    plt.show()

def generatePieChart(labels, values, colors=None, autopct=None):
    """
    Genera un gráfico de sectores con los valores y etiquetas proporcionados.

    Args:
        labels (list): Etiquetas para los sectores.
        values (list): Valores para los sectores.
        colors (list, optional): Colores para los sectores. Defaults to None.
        autopct (str, optional): Formato para mostrar el porcentaje en cada sector. Defaults to None.
    """
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors, autopct=autopct)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    colors = ['#ff0000', '#00ff00', '#0000ff']  # Rojo, verde y azul
    hatch = ['/', '\\', '|']  # Patrones de sombreado

    # generateBarChart(labels, values, colors, hatch)
    generatePieChart(labels, values, colors, autopct='%1.1f%%')
'''

def generateBarChart(labels,values):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generatePieChart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()



if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,40,800]
    #generateBarChart(labels,values)
    generatePieChart(labels,values)
    generateBarChart(labels=labels, values=values)
