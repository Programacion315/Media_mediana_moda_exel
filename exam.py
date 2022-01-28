# Módulo de estadística descriptiva
# Media, Moda, Mediana, Rango, Maximo valor, Mínimo valor, Desviación estandar, varianza  
import pandas as pd
import numpy as np
import csv


da = pd.read_csv("datos.csv")
print(da)
matriz = pd.read_csv("datos.csv",  sep=';',  comment='#').values


i = 1 #columna que queremos obtener
columna = [fila[i] for fila in matriz]

print(columna)


# Módulo de estadística descriptiva
# Media, Moda, Mediana, Rango, Maximo valor, Mínimo valor, Desviación estandar, varianza  

def media(listaDatos):
    sumatoriaDatos = 0
    numeroDatos = 0
    for iterDatos in listaDatos:
        sumatoriaDatos = sumatoriaDatos + iterDatos
        numeroDatos = numeroDatos + 1
    promedio = sumatoriaDatos / numeroDatos
    return promedio

def media1(listaDatos):
    return sum(listaDatos)/len(listaDatos)

def moda(listaDatos):
    dictModa = {}
    modas = {}
    for iterDatos in listaDatos:
        frecuencia = listaDatos.count(iterDatos)
        dictModa[iterDatos] = frecuencia
    
    listValores = dictModa.values()
    maxValor = max(listValores)
    if maxValor > 1 :
        for clave, valor in dictModa.items():
            if valor == maxValor:
                modas[clave] = valor
            
        return modas
    else:
        return []
    
def mediana(listaDatos):
    #  3, 5, 7, 8, 8, 10     longitud = 6      6/2 = 3 y 3-1 = 2   6/2 = 3
    # mediana es 7.5
    # 1, 6, 8, 10, 12, 23, 25  rango = 25 - 1 = 24
    # mediana es 7
    listaDatos.sort()
    if len(listaDatos) % 2 == 0: # Si la cantidad de datos es par
        median = (listaDatos[int(len(listaDatos)/2 - 1)] + listaDatos[int(len(listaDatos)/ 2)]) / 2
    else: # la cantidad de datos es impar
        median = listaDatos[int(len(listaDatos)/ 2)]
    return median 
       
def rango(listaDatos):
    return max(listaDatos) - min(listaDatos)

def maximo(listaDatos):    
    return max(listaDatos) 

def minimo(listaDatos):    
    return min(listaDatos) 

def desvEstandar(listaDatos):
    pass

def varianza(listaDatos):
    pass
    
def main():
    datos = [fila[i] for fila in matriz]
    seguir = True
    while seguir == True:
        dato = int(input("Ingrese el dato "))
        datos.append(dato)
        control = input("Desea continuar (S/N) ")
        if control.upper() == "N":
            seguir = False
            
               
    resultado = media(datos) 
    print("El promedio de los datos con la función media es: ", resultado)       
    print("El promedio de los datos con la función media1 es: ", media1(datos)) 
    resultadoModa = moda(datos)
    if len(resultadoModa) == 0:
        print("No hay moda")
    else:
        print("La moda es: ", list(resultadoModa.keys()))
        
    print("La mediana es: ", mediana(datos))    
    print("La rango es: ", rango(datos))   
    print("El máximo valor es: ", maximo(datos))   
    print("El mínimo valor es: ", minimo(datos))       

    with open("datosNuevos.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(str(mediana(datos)))
        writer.writerow(str(rango(datos)))
        writer.writerow(str(minimo(datos)))
        writer.writerow(str(maximo(datos)))
## _name_

main()


