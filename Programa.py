import numpy as np
import math as math


class computacional:
    def __init__(self):
        ...
    
    def mediana(self):
        filas = int(input("Cuantas filas, eje x:  "))
        columnas = int((input("Cuantas columnas, eje y: ")))
        ...
    
    def expancion(self):
        a = int((input("Ingresar a: ")))
        b = int((input("Ingresar b: ")))
        c = int((input("Ingresar c: ")))
        d = int((input("Ingresar d: ")))
        m = (d-c)/(b-a)
        b2 = c-(m*a)
        
        
        T= []     
        for i in range(8):
            T.append(m*i+b2)
            print("T(",i,")","= ",m*i+b2,"\n")
        
    #---------------------------LAPLACIANO----------------------------
    #-- Reemplazarlo con numpy xd
    def laplaciano(self):
        matrizPrincipal = []
        mascara = []
        print("Ingrese los valores de la mascara: \n")
        #AQUI CAMBIAR SI LA MASCARA NO ES DE 3 X 3
        #El aux1 solo sirve para enumerar los valores q vamos poniendo y no confundirnos xd
        aux1= 0
        for i in range(3):
            xd = []
            print("Ingrese el valor",aux1)
            xd.append( int(input()))
            aux1= aux1+1
            print("Ingrese el valor",aux1)
            xd.append( int(input()))
            aux1= aux1+1
            print("Ingrese el valor",aux1)
            xd.append( int(input()))
            aux1= aux1+1
            mascara.append(xd)
        
        print("Su mascara es: \n",mascara)
        
        print(mascara[0][2])
        
        aux1=0
        tamano= int(input("Tamano de la matriz principal: "))
        #AQUI RELLENAREMOS LA MATRIZ PE, 
        print("Ingrese los valores de la Matriz Principal original: \n")
    
        for j1 in range(tamano):
            xd2=[]
            for  j2 in range(tamano):
                print("Ingrese el valor ",aux1)
                xd2.append(int(input()))
                aux1=aux1+1
            
            matrizPrincipal.append(xd2)
            
        print("Su matriz principal es: \n",matrizPrincipal)
        
        valores = []
        aux=0
        for  x in range(tamano):
            for y in range(tamano):
                aux=aux+(matrizPrincipal[x][y]*mascara[1][1])
                print(aux,",")
                if  (x-1>=0) and (y-1>=0):
                    aux = aux + (matrizPrincipal[x-1][y-1]*mascara[0][0])
                    print(aux,",")
                if (y-1>=0):
                    aux=aux + (matrizPrincipal[x][y-1]*mascara[0][1])
                    print(aux,",")
                if (y-1>=0) and (x+1<=tamano-1) : 
                    aux=aux + (matrizPrincipal[x+1][y-1]*mascara[0][2])
                    print(aux,",")
                if  (x-1>=0):
                    aux=aux + (matrizPrincipal[x-1][y]*mascara[1][0])
                    print(aux,",")
                if (x+1)<= (tamano-1):
                    aux=aux + (matrizPrincipal[x+1][y]*mascara[1][2])
                    print(aux,",")
                if (x-1>=0) and (y+1<=tamano-1):
                    aux=aux + (matrizPrincipal[x-1][y+1]*mascara[2][0])
                    print(aux,",")
                if (y+1<=0):
                    aux=aux + (matrizPrincipal[x][y+1]*mascara[2][1])
                    print(aux,",")
                if (x+1<=tamano-1) and (y+1<=tamano-1):
                    aux=aux + (matrizPrincipal[x+1][y+1]*mascara[2][2])
                    print(aux,",")
                print(aux,"\n")
                valores.append(aux)
                aux=0
        print(valores)
# ----------------------ecualizacion-----------
    def ecualizacion():
        cantidadEscalas = int(input("Ingresa la cantidad de escalas de grises: "))
        primerArreglo=[]
        
        for i in range(cantidadEscalas):
            aux = int(input("Ingresa la cantidad de pixeles en la posicion: " + str(i) + " -> "))
            primerArreglo.append(aux)
        #print (primerArreglo)
        
        cantidadPixeles = 0
        for i in range(cantidadEscalas):
            cantidadPixeles =  cantidadPixeles + primerArreglo[i]
        
        arregloPorcentajes1= []
        for i in range(cantidadEscalas):
            arregloPorcentajes1.append(primerArreglo[i]/cantidadPixeles)

        #print (arregloPorcentajes1)
        ### ESTAS SON VARIABLES PARA LAS OPERACIONES
        a = cantidadEscalas-1
        b = 0
        arreglo3 = []
        for  i in range(cantidadEscalas):
            b = b + arregloPorcentajes1[i]
            arreglo3.append(a*b)

        #print(arreglo3)
        arreglo4 = []
        for  i in range(cantidadEscalas):
            arreglo4.append(round(arreglo3[i]))
        print(arreglo3)
        
        ##PINTAMOS BONITO XD
        print("///////////////////////////////////////////////////////////////////////////////////////")
        
        for  i in range(cantidadEscalas):
            print(str(arreglo3[i])+ " -> "+ str(arreglo4[i])+" -> "+str(arregloPorcentajes1[i])+" -> "+ str(arregloPorcentajes1[i]*cantidadPixeles) +"\n")
        
        
#------------------MATRIZ CAMINOS--------------
    def MatrizCaminos(self):
        fil = int(input("Ingrese la cantidad de filas: "))
        col = int(input("Ingrese la cantidad de columnas: "))
        dimenciones = (fil,col)
        
        MatrizOriginal = np.zeros(dimenciones)
        
        for i in range(fil):
            for j in range(col):
                num =  int(input("Ingrese el numero en la posicion: "+ str(i)+"," + str(j)+ " : "))
                MatrizOriginal[i,j] = num
        print("Su matriz original es : ")
        print(MatrizOriginal)
        print("--------------------------------")
        for supa in range(fil*col):
            for i in range(fil):
                for j in range(col):

                    if MatrizOriginal[i,j] == 1 : 
                        
                        for k in range(col):
                            if MatrizOriginal[j,k] == 1:
                                MatrizOriginal[i,k]=1
                                continue
        print("La matriz de caminos es: ")
        print(MatrizOriginal)
#----------------Algoritmo djkastra----------------
    def djkastra(self):
        fil = int(input("Ingrese la cantidad de filas: "))
        col = int(input("Ingrese la cantidad de columnas: "))
        dimenciones = (fil,col)
        
        MatrizOriginal = np.zeros(dimenciones)
        
        for i in range(fil):
            for j in range(col):
                num =  int(input("Ingrese el numero en la posicion: "+ str(i)+"," + str(j)+ " : "))
                MatrizOriginal[i,j] = num
        print("Su matriz original es : ")
        print(MatrizOriginal)
        print("--------------------------------")
        for supa in range(fil*col):
            for i in range(fil):
                for j in range(col):

                    if MatrizOriginal[i,j] == 1 : 
                        
                        for k in range(col):
                            if MatrizOriginal[j,k] == 1:
                                MatrizOriginal[i,k]=1
                                continue
        for i in range(fil):
            MatrizOriginal[i,i]= 1
            
        contadorUnos = 0
        conjuntoDeUnos=[]
        for i in range(fil):
            contadorUnos = 0
            for j in range(col):
                if MatrizOriginal[i,j]== 1:
                    contadorUnos = contadorUnos+1
            conjuntoDeUnos.append([contadorUnos,i])
        #print(conjuntoDeUnos)
        temp = []
        
        for i in range(len(conjuntoDeUnos)):
            least = i
            for j in range(i+1,len(conjuntoDeUnos)):
                if conjuntoDeUnos[i][0]<conjuntoDeUnos[j][0]:
                    temp = conjuntoDeUnos[i]
                    conjuntoDeUnos[i] = conjuntoDeUnos[j]
                    conjuntoDeUnos[j] = temp

        #print(conjuntoDeUnos)
        
        reemplazo = []
        for i in range(len(conjuntoDeUnos)):
            reemplazo.append(conjuntoDeUnos[i][1])
        
        MatrizOriginal=MatrizOriginal[reemplazo,:]
        MatrizOriginal=MatrizOriginal[:,reemplazo]
        
        print(MatrizOriginal)
        print("En el orden: ")
        print(reemplazo)
        



