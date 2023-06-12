import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataFrame,campox, campoy, nombreGrafica):
    colores=["green","violet","black"]
    salarioPromedio=dataFrame.groupby(campox)[campoy].mean()

    plt.bar(salarioPromedio.index,salarioPromedio,color=colores)

    plt.title("promedio salarial")
    plt.xlabel("cargos")
    plt.ylabel("salarios mensual")
    plt.savefig(f'/assets/img/{nombreGrafica}.png')