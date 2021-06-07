import math
import numpy as np
from Programa import computacional


programa = computacional()

while True:
    print("---------------------------------------------------------------------------")
    print("Que ejercicio deseas realizar? : \n 1.-Mediana \n 2.-Expancion  \n 3.-Laplaciano \n 4.-Ecualizacon \n 5.-Matriz de caminos \n 6.-Componentes Conexas \n 7.-Salir")
    opcion = int(input())
    if opcion == 1:
        programa.mediana()
    elif opcion == 2:
        programa.expancion()
    elif opcion == 3:
        programa.laplaciano()
    elif opcion == 4:
        programa.ecualizacion()
    elif opcion == 5:
        programa.MatrizCaminos()
    elif opcion == 6:
        programa.conexa()
    elif opcion == 7 :
        break
    else: 
        print("Elige bien pe tmre xd")

