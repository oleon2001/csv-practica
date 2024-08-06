import matplotlib.pyplot as plt
import seaborn as sns

def generateBarChart(labels,values):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generatePieChart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()

def generateScatter(labels,values):
    fig, ax = plt.subplots()
    plt.scatter(labels,values)
    plt.show()


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,40,800]
    #generateBarChart(labels,values)
    generatePieChart(labels,values)

