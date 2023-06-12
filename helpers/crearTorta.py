import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioSalariosPorEdad(dataFrame, rangos,columnadeinteres,columnaapromediar,nombreGrafica):
    plt.figure()

    dataFrame['rangosEdad']=pd.cut(dataFrame[columnadeinteres],nins=rangos)

    salarioporrango=dataFrame.groupby('rangosEdad')['salario'].sum()

    salario=salarioporrango.values
    rangosEdad = salarioporrango.index

    plt.pie(salario, labels=rangosEdad, autopct="%1,1f%%")
    plt.title('salarios por rango de edad')
    plt.savefig(f'/assets/img/{nombreGrafica}.png')