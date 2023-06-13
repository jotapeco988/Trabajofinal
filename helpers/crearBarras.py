import matplotlib.pyplot as plt
ruta_absoluta = 'C:/Users/duque/OneDrive/Escritorio/nuevos/python/Trabajofinal/assets/img'

def graficarnose(dataFrame,campox, campoy, nombreGrafica):
    colores=["green","violet","black"]
    nose=dataFrame.groupby(campox)[campoy].mean()



    plt.bar(nose.index,nose,color=colores)

    plt.title("nose que estoy graficando")
    plt.xlabel("nombre")
    plt.ylabel("arboles")
    plt.savefig(f'{ruta_absoluta}/{nombreGrafica}.png')