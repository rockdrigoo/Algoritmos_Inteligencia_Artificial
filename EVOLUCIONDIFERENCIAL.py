#EVOLUCION DIFERENCIAL
#Autor: Rodrigo Antonio Arciniega Mendoza

import random # Libreria necesaria para generar datos aleatorios
import math # Libreria necesaria para funciones trigonometricas
from time import time # Libreria necesaria para poder medir el timpo

"""Este algoritmo realiza 30 corridas de Evolucion Diferencial y entrega 2 listas
   que contienen los mejores costos y los mejores tiempos en cada una de esas
   corridas. Este algoritmo llega a la solucion deseada de una manera muy muy rapida.
   Estuve analizandolo mucho tiempo pensando que tenia mal algo, pues los resultados 
   que obtenia eran muy muy beunos."""
   
MejoresCostos=[] # Listas en donde se guardan los 30 datos obtenidos
MejoresTiempos=[]


def FO(SolActual): # Definimos la Funcion Objetivo
    a=SolActual[0]
    b=SolActual[1]
    cte=418.9829*2
    f=cte-((a*math.sin(math.sqrt(math.fabs(a))))+(b*math.sin(math.sqrt(math.fabs(b)))))
    return f

def GenPob(Poblacion):                  # Funcion que Genera nuestra poblacion aleatoria
    for i in range (0,len(Poblacion)):
        Poblacion[i]=[round(random.uniform(-500,500),4),round(random.uniform(-500,500),4)]
        
def GenCosto(Poblacion,Costos):        #Funcion que genera los costos de nuestros individuos
    for i in range (0,len(Poblacion)):
        Costos[i]=FO(Poblacion[i])
        
def GeneraMutante(Pi,Pj,Pk):   # Generamos nuestra solucion mutante
    mutant=[None]*2            # Creamos un vector con dos entradas que seran modificadas
    F=0.8                               # Establecemos nuestro factor de escala de mutacion
    mutant[0]=Pi[0]+F*(Pj[0]-Pk[0])    # Realizamos la mutacion para la primer coordenada del vector mutante
    mutant[1]=Pi[1]+F*(Pj[1]-Pk[1])    # Realizamos la mutacion para la segunda coordenad del vector mutante
    if mutant[0]>500 or mutant[0]<-500: # Validamos que nuestra solucion vecina este dentro del dominio de la funcion
        if mutant[0]>500:
            mutant[0]=500-(mutant[0]-500)
        else:
            mutant[0]=-500-(mutant[0]+500)
    if mutant[1]>500 or mutant[1]<-500:
        if mutant[1]>500:
            mutant[1]=500-(mutant[1]-500)
        else:
            mutant[1]=-500-(mutant[1]+500)
    return mutant                      # Devolvemos el mutante creado

def GeneraHijo(Pm,Mutante):          # Generamos la cruza entre el vector padre y el mutante previamente obtenido
    hijo1=[None]*2                       # Creamos un vector Hijo que sera resultado de la cruza
    Cr=0.5                              # Establecemos una constante de cruza
    i=random.randint(0,1)
    for j in range(2):                  # Realizamos una serie de volados entre el padre y el mutante para ver como se le heredan caracteristicas al hijo
        r=random.uniform(0,1)
        if r < Cr:
            hijo1[j]=Mutante[j]
        else:
            hijo1[j]=Pm[j]
    hijo1[i]=Mutante[i]                  # Obligamos al hijo a tener caracteristicas del mutante
    return hijo1

for q in range (30):
    tiempo_inicial=time() # Comienzo a medir el tiempo
    Mutante=[None]*2    # Creamos un vector de dos entradas para guardar al mutante que generaremos
    Hijo=[None]*2   # Creamos un vector de dos entradas para guardar al hijo que generaremos
    CostoHijo=[]    # Creamos un vector para guardar el costo de los hijo
    P=[None]*13    # Creamos una lista con el tamaño de nuestra poblacion
    GenPob(P)       # Generamos una poblacion de soluciones aleatorias
    Costo=[None]*13     # Creamos una lista para guardar los costos de las soluciones
    GenCosto(P,Costo)  # Calculamos cada uno de estos costos
    
    """habia colocado un rango de 500 en el primer ciclo for, pero estuve
        analizando el algoritmo, y me di cuenta que los resultados no variavan en nada cuando el 
        tamaño del ciclo se reducia a 70."""
    for n in range(70):
        for m in range(13):
            i=random.randint(0,12)
            j=random.randint(0,12)
            k=random.randint(0,12)
            while (i==j or i==k or i==m or j==k or j==m or m==k):   # Verificamos que no se repitan los padrinos para cada dato
                i=random.randint(0,12)
                j=random.randint(0,12)
                k=random.randint(0,12)   
            Pi=P[i]                    # Generamos al padrino 1
            Pj=P[j]                    # Generamos al padrino 2
            Pk=P[k]                    # Generamos al padrino 3
            Pm=P[m]                    # Generamos al padre
            Mutante=GeneraMutante(Pi, Pj, Pk)       # Generamos un vector mutante con caracteristicas de los padrinos 
            Hijo=GeneraHijo(Pm, Mutante)            # Generamos un vector que es cruza de los padrinos con el mutante
            CostoHijo=FO(Hijo)                      # Calculamos su costo
            if CostoHijo <= Costo[m] :
                Pm[0]=Hijo[0]
                Pm[1]=Hijo[1]
                Costo[m]=CostoHijo

    MejorCosto=Costo[0]
    for s in range(2,13):
        if Costo[s]< MejorCosto:
            MejorCosto=Costo[s] 
    print("La mejor solucion es: ", Hijo)
    print("El mejor costo obtenido es: ", MejorCosto)
    tiempo_final=time() # Dejamos de medir el tiempo
    tiempo_total=tiempo_final-tiempo_inicial # Guardamos el tiempo en una variable
    print('El tiempo de ejecucion del algoritmo es: ', round(tiempo_total,4),"segundos")
    MejoresCostos.append(MejorCosto)       # Guardamos nuestros mejores costos
    MejoresTiempos.append(tiempo_total)     # Guardamos nuestros mejores tiempos
    print('\n')

print('Los 30 mejores Costos son:', MejoresCostos)
print('Los 30 mejores tiempos son: ', MejoresTiempos)

