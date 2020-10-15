import random
import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ nose ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
def borra_pantalla(tiempo,nombre_usuario):
    print("\n¡Tienes",tiempo,"segundos para memorizarla! ¡Tú puedes,",nombre_usuario,"!\n \n")
    time.sleep(tiempo)
    for i in range(30):
        print("Espera....")
        time.sleep(.1)

def guardar_partida (nivel,nombre_usuario,intentos):
    nivel_guardar=open('nivel.txt','w')
    nivel_guardar.write(str(nivel))
    nivel_guardar.close()
    intentos_guardar=open('intentos.txt','w')
    intentos_guardar.write(str(intentos))
    intentos_guardar.close()
    nombre_guardar=open('nombre_usuario.txt','w')
    nombre_guardar.write(str(nombre_usuario))
    nombre_guardar.close()
    print("\n \nJUEGO GUARDADO :D")
    
def seguir_nivel(nombre_usuario,nivel,intentos):
    if nivel==1:
        nivel1(nombre_usuario,intentos)
    elif nivel==2:
        nivel2(nombre_usuario,intentos)
    else:
        nivel3(nombre_usuario,intentos)

def comprobacion_intentos(intentos,nombre_usuario,nivel):
    if intentos == 3:
        print("\n \nLo sentimos,",nombre_usuario," perdiste el juego")
        continuar(intentos,nombre_usuario,nivel)
        

def continuar(intentos,nombre_usuario,nivel):
    print("¿Quieres seguir jugando? SI/NO")
    print("Respuesta: ",end="")
    seguir_jugando=input().upper()
    if seguir_jugando== "SI":
        intentos=0
        seguir_nivel(nombre_usuario,nivel,intentos)
    elif seguir_jugando== "NO":
        print("\n \n¡Gracias por jugar,",nombre_usuario,"nos vemos luego!")
        guardar_partida(nivel,nombre_usuario,intentos)
        
def incorrecto(intentos,nombre_usuario,nivel):
    intentos=intentos+1
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    print("\nEstuviste cerca,",nombre_usuario,"¡Inténtalo de nuevo! :)\n")
    continuar(intentos,nombre_usuario,nivel)
        
    

#~~~~~~~~~~~~~~~~~~~~~ CREACIÓN Y FORMATO DE MATRICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#Crea una matriz de 0 que será llenada posteriormente con números aleatorios
def matriz_ceros(num_ren,num_col): 
    matriz = []
    for renglon in range(num_ren):
        matriz.append([0] * num_col)
    return matriz

#Crea una matriz de números aleatorios.
def matriz_random(num_ren,num_col):
    matriz=matriz_ceros(num_ren,num_col)
    for ren in range(num_ren):
        for col in range(num_col):
            num=random.randint(0,9)
            matriz[ren][col]=num
    return matriz

# Muestra la matri en forma de matriz 
def muestra_matriz(m):
    for ren in range(len(m)):
        for col in range(len(m[0])):
            print(f'{m[ren][col]:3}', end='')
        print()
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESPUESTA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# Pide la respuesta del usuario
def respuesta(matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel):
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    
    matriz_respuesta=[]
    for posicion in range(num_ren):
        numeros=input()
        numeros=numeros.split()
        matriz_respuesta.append(numeros)
    #Se revisa si se ingreso la misma cantidad de columnas que las deseadas.
    for reng in range(num_ren):
        if len(matriz_respuesta[reng]) != num_col:
            incorrecto(intentos,nombre_usuario,nivel)
            
    # Convierte los str a int
    matriz_respuestaNum= matriz_ceros(num_ren,num_col)   
    for m in range(num_ren):
        for n in range(num_col):
            v= int(matriz_respuesta[m][n])
            matriz_respuestaNum[m][n]=v
    #Comprueba si la respuesta es correcta
    comprobacion_respuesta(matriz_respuestaNum,matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel)
    
        
        
        

# Evalúa la respuesta del usuario y la comprueba para ver si está bien o ma
def comprobacion_respuesta(matriz_respuestaNum,matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel):
    correctas=0
    columnas=len(matriz[0])
    renglones=len(matriz)
    for i in range(renglones):
        for e in range(columnas):
            if matriz[i][e] == matriz_respuestaNum[i][e]:
                correctas=correctas+1
                
    if correctas == correctas_x_nivel:
        nivel=nivel+1
        print("*****************************************************************") 
        print("*                                                               *")
        print("  ¡Felicidades,",nombre_usuario," pasaste al siguiente nivel!    ")
        print("*                                                               *")
        print("*****************************************************************\n")
        continuar(intentos,nombre_usuario,nivel)
                
    else:
        incorrecto(intentos,nombre_usuario,nivel)
    
            
            
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NIVELES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

#Nivel 1 del juego con matriz 2x2
def nivel1(nombre_usuario,intentos):
    nivel=1
    tiempo=5
    correctas_x_nivel=4
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    #Se define la dimensión de la matriz del juego.
    num_ren=2
    num_col=2
    print("\nNIVEL 1\n")
    #Se crea una matriz de ceros para guardar los valores.
    matriz=matriz_ceros(num_ren,num_col)
    #Se crean los valores aleatorios dentro la matriz de ceros.
    for ren in range(num_ren):
        for col in range(num_col):
            num=random.randint(1,10)
            matriz[ren][col]=num
    #Muestra la matriz en forma de matriz.        
    muestra_matriz(matriz)
    #"Borra" la pantalla del usuario.
    borra_pantalla(tiempo,nombre_usuario)
    #El usuario da la respuesta al juego:
    print("\n¿Recuerdas la secuencia?\n¡Escríbela!\n")
    respuesta(matriz,nombre_usuario,intentos,num_col,num_ren,tiempo,nivel,correctas_x_nivel)
            
            
        
    
    
def nivel2(nombre_usuario,intentos):
    nivel=2
    tiempo=10
    correctas_x_nivel=9
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    #Se define la dimensión de la matriz del juego.
    num_ren=3
    num_col=3
    print("\nNIVEL 2\n")
    #Se crea una matriz de ceros para guardar los valores.
    matriz=matriz_ceros(num_ren,num_col)
    #Se crean los valores aleatorios dentro la matriz de ceros.
    for ren in range(num_ren):
        for col in range(num_col):
            num=random.randint(1,10)
            matriz[ren][col]=num
    #Muestra la matriz en forma de matriz.        
    muestra_matriz(matriz)
    #"Borra" la pantalla del usuario.
    borra_pantalla(tiempo,nombre_usuario)
    #El usuario da la respuesta al juego:
    print("\n¿Recuerdas la secuencia?\n¡Escríbela!\n")
    respuesta(matriz,nombre_usuario,intentos,num_col,num_ren,tiempo,nivel,correctas_x_nivel)
    
    
def nivel3(nombre_usuario,intentos):
    print("\nNIVEL 3 EN PROCESO")
#     nivel=3
#     tiempo=15
#     correctas_x_nivel=25
#     comprobacion_intentos(intentos,nombre_usuario,nivel)
#     #Se define la dimensión de la matriz del juego.
#     num_ren=4
#     num_col=4
#     print("NIVEL 3\n")
#     #Se crea una matriz de números aleatorios.
#     matriz=matriz_random(num_ren,num_col)
#     # Asigna aleatoriamente "-".
#     # Asigna aleatoriamente "-".
#     for ren in range(num_ren+1):
#         for col in range(num_col+1):
#             num=" -"
#             reng=random.randint(0,3)
#             colu=random.randint(0,3)
#             matriz[reng][colu]=num
#     
#     #Muestra la matriz en forma de matriz.        
#     muestra_matriz(matriz)
#     #"Borra" la pantalla del usuario.
#     borra_pantalla(tiempo,nombre_usuario)
#     #El usuario da la respuesta al juego:
#     print("\n¿Recuerdas la secuencia?\n¡Escríbela!\n")
#     respuesta(matriz,nombre_usuario,intentos,num_col,num_ren,tiempo,nivel,correctas_x_nivel)
# 



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENÚ PRINCIPAL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
def main():
    nivel_anterior=open("nivel.txt","r")
    nivel=nivel_anterior.read()
    nivel_anterior.close()
    usuario=open("nombre_usuario.txt","r")
    nombre_usuario=usuario.read()
    usuario.close()
    intentos_anterior=open("intentos.txt","r")
    intentos=intentos_anterior.read()
    intentos_anterior.close()
    
    while nivel == "" or nivel !="":
        
         if nivel == "":
            intentos=0
            print("******************************************") 
            print("*                                        *")
            print("*  ¡Bienvenido a Recuerda la secuencia!  *")
            print("*                                        *")
            print("******************************************")
            print("\n¿Cómo te llamas? ",end="")
            nombre_usuario=input()
            print("\nMuy bien,",nombre_usuario," en este juego podrás ejercitar tu memoria de forma fácil y divertida\nSolo tienes que recordar la secuencia de los números que se te mostrarán en pantalla.\nCuando se te pida la respuesta deberás teclear los números renglón por renglón de forma lineal y separados por espacios.")
            print("\n \n¡Vamos a jugar,",nombre_usuario,"!\n")
            time.sleep(10)
            nivel1(nombre_usuario,intentos)
            break
        
         else:
            print("*************************************************************") 
            print("*                                                           *")
            print("          ¡Bienvenido de vuelta,",nombre_usuario,"!          ")
            print("*                                                           *")
            print("*************************************************************")
                
            print ("\nElige una opción:\n1) Iniciar nueva partida\n2) Continuar partida")
            print("Opción: ",end="")
            opcion=int(input())
            while (opcion != 2)and(opcion!=1):
                print("Ingrese el número de la opción que deseé")
                print ("Elige una opción:\n1) Iniciar nueva partida\n2) Continuar partida")
                print("Opción: ",end="")
                opcion=int(input())
            if opcion == 1:
                reiniciar=open('nivel.txt','w')
                reiniciar.write("")
                reiniciar.close()
                re=open("nivel.txt","r")
                nivel=re.read()
                re.close()
                
                
                reiniciar_nombre=open('nombre_usuario.txt','w')
                reiniciar_nombre.write("")
                reiniciar_nombre.close()
                re_nombre=open("nombre_usuario.txt","r")
                nombre_usuario=re_nombre.read()
                re_nombre.close()
                
                reiniciar_intentos=open('intentos.txt','w')
                reiniciar_intentos.write(str(0))
                reiniciar_intentos.close()
                re_intentos=open("intentos.txt","r")
                intentos=re_intentos.read()
                re_intentos.close()
                
            elif opcion == 2:
                print("¡Hola,",nombre_usuario,"!\nAnteriormente te quedaste en el nivel",nivel)
                print("Tus intentos hasta ahora son: ",intentos)
                time.sleep(3)
                nivel=int(nivel)
                intentos=int(intentos)
                
                seguir_nivel(nombre_usuario,nivel,intentos)
                break
            
        
        
    
main()  