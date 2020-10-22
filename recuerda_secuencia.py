# JUEGO: Recuerda la secuencia
# 20/10/2020
# Serete Jardón A01235434   IBQ
# Paola De La Rosa A01233794 ICT
# Versión de Python: 3.7.7

import random
import time
import turtle
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# "Borra" la pantalla del usuario para que no vea la matriz a memorizar
def borra_pantalla(tiempo,nombre_usuario):
    print("\n¡Tienes",tiempo,"segundos para memorizarla! ¡Tú puedes,",nombre_usuario,"!\n \n")
    print("Espera...")
    time.sleep(tiempo)
    for i in range(30):
        print("Espera....")
        time.sleep(.1)

#Guarda la partida cuando el usuario ya no quiere jugar
def guardar_partida (nivel,nombre_usuario,intentos):
    nivel_guardar = open('nivel.txt','w')
    nivel_guardar.write(str(nivel))
    nivel_guardar.close()
    intentos_guardar = open('intentos.txt','w')
    intentos_guardar.write(str(intentos))
    intentos_guardar.close()
    nombre_guardar = open('nombre_usuario.txt','w')
    nombre_guardar.write(str(nombre_usuario))
    nombre_guardar.close()
    print("\n \nJUEGO GUARDADO :D")
    exit()
    
# Se lleva al nivel en el que el usuario se quedó
def seguir_nivel(nombre_usuario,nivel,intentos):
    if nivel == 1:
        nivel1(nombre_usuario,intentos)
        
    elif nivel == 2:
        nivel2(nombre_usuario,intentos)
    else:
        nivel3(nombre_usuario,intentos)
        
# Se comprueba si hay 3 intentos, de ser así se le indica al usuario que ha perdido el juego y le pregunta si quiere
#seguir jugando
def comprobacion_intentos(intentos,nombre_usuario,nivel):
    if intentos == 3:
        print("\n \nLo sentimos,",nombre_usuario," perdiste el juego")
        intentos = 1
        nivel = 1
        continuar(intentos,nombre_usuario,nivel)
        
#Le pregunta al jugador si quiere seguir jugando, de se así se le lleva al nivel en el
# que estaba y si no quiere manda a llamar a la funcion guardar juego
def continuar(intentos,nombre_usuario,nivel):
    print("\n¿Quieres seguir jugando? SI/NO")
    print("Respuesta: ",end="")
    seguir_jugando=input().upper()
    while (seguir_jugando != "SI") and (seguir_jugando != "NO"):
        print("\n¿Quieres seguir jugando? SI/NO")
        print("Respuesta: ",end="")
        seguir_jugando=input().upper()
        
        
    if seguir_jugando == "SI":
        seguir_nivel(nombre_usuario,nivel,intentos)
    elif seguir_jugando == "NO":
        print("\n \n¡Gracias por jugar,",nombre_usuario,"nos vemos luego!")
        guardar_partida(nivel,nombre_usuario,intentos)

#Le indica al usuario que su respuesta es incorrecta y luego manda a llamar a la funcion continuar
def incorrecto(intentos,nombre_usuario,nivel):
    intentos = intentos+1
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    print("\nEstuviste cerca,",nombre_usuario,"¡Inténtalo de nuevo! :)\n")
    print("Tus intentos hasta ahora son: ",intentos)
    continuar(intentos,nombre_usuario,nivel)
    
# Si el usuario gana el juego le da una felicitaión al usuario.    
def ganar():
    
    import turtle
    
    
    
    turtle.setup(1400, 750)
    t = turtle.Turtle()
    t.speed(10)
    turtle.bgcolor("#000000")
    turtle.title("¡Felicidades!")
    t.shape("turtle")
    t.color("green", "green")
    t.pensize(5)
    t.pencolor("yellow")
    
    #G
    t.forward(-500)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.forward(-100)
    t.left(90)
    t.forward(-200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(-50)

    #A
    t.forward(50)
    t.left(90)
    t.forward(-100)
    t.right(90)
    t.forward(50)
    t.left(80)
    t.forward(200)
    t.left(180)
    t.forward(100)
    t.left(100)
    t.forward(55)
    t.forward(-55)
    t.left(80)
    t.forward(100)
    t.right(150)
    t.forward(210)
    t.left(70)
    t.forward(50)

    #N
    t.forward(200)
    t.forward(-200)
    t.left(90)
    t.forward(200)
    t.left(30)
    t.forward(-230)
    t.right(30)
    t.forward(200)
    t.forward(-200)
    t.right(90)
    t.forward(500)
    t.forward(-450)

    #A
    t.left(80)
    t.forward(200)
    t.left(180)
    t.forward(100)
    t.left(100)
    t.forward(55)
    t.forward(-55)
    t.left(80)
    t.forward(100)
    t.right(150)
    t.forward(210)
    t.left(70)
    t.forward(50)

    #S
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(-100)
    t.right(90)
    t.forward(100)

    #T
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.forward(-100)
    t.forward(50)
    t.right(90)
    t.forward(-200)
    t.right(90)
    t.forward(100)

    #E
    t.forward(100)
    t.forward(-100)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.forward(-100)
    t.left(90)
    t.forward(-100)
    t.right(90)
    t.forward(50)
    t.forward(-50)
    t.left(90)
    t.forward(-100)
    t.right(90)
    t.forward(100)

    t.left(180)
    t.forward(500)
    t.left(90)
    t.forward(180)
    t.right(124)

    for i in range(35):
        t.forward(i * 10)
        t.right(144)
    time.sleep(4)
    turtle.bye()
    turtle.Terminator

    
    
    
        
    

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
            matriz[ren][col] = num
    return matriz

# Muestra la matriz en forma de matriz 
def muestra_matriz(m):
    for ren in range(len(m)):
        for col in range(len(m[0])):
          print(f'{m[ren][col]:3}', end='')
        print()
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RESPUESTA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# Pide la respuesta del usuario
def respuesta(matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel):
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    
    matriz_respuesta = []
    for posicion in range(num_ren):
        numeros = input()
        numeros = numeros.split()
        for elemento in range(len(numeros)):
            if numeros[elemento] == "-":
                numeros[elemento] = ord("-")
        matriz_respuesta.append(numeros)
    #Se revisa si se ingreso la misma cantidad de columnas que las deseadas.
    if len(matriz_respuesta) != len(matriz):
        incorrecto(intentos,nombre_usuario,nivel)
           
    # Convierte los str a int
    else:
        matriz_respuestaNum= matriz_ceros(num_ren,num_col)   
        for m in range(num_ren):
            for n in range(num_col):
                v=int(matriz_respuesta[m][n])
                matriz_respuestaNum[m][n] = v
        #Comprueba si la respuesta es correcta
        comprobacion_respuesta(matriz_respuestaNum,matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel)
    
        
        
        

# Evalúa la respuesta del usuario y la comprueba para ver si está bien o mal.
def comprobacion_respuesta(matriz_respuestaNum,matriz,nombre_usuario,intentos,num_ren,num_col,tiempo,nivel,correctas_x_nivel):
    correctas = 0
    columnas = len(matriz[0])
    renglones = len(matriz)
    for i in range(renglones):
        for e in range(columnas):
            if matriz[i][e] == matriz_respuestaNum[i][e]:
                correctas = correctas+1
                
    if correctas == correctas_x_nivel:
        if nivel != 3:
            nivel = nivel+1
            intentos = 1
            print("*****************************************************************") 
            print("*                                                               *")
            print("  ¡Felicidades,",nombre_usuario," pasaste al siguiente nivel!    ")
            print("*                                                               *")
            print("*****************************************************************\n")
            continuar(intentos,nombre_usuario,nivel)
        else:
            print("***********************************************")
            print(" !Has terminado el juego,",nombre_usuario,"!"   )
            print("***********************************************")
            print("Se abrirá una ventana, presionala para abrila")
            nivel=1
            ganar()
            continuar(intentos,nombre_usuario,nivel)
            
            
            
    else:
        incorrecto(intentos,nombre_usuario,nivel)
    
            
            
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ NIVELES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

#Nivel 1 del juego con matriz 2x2
def nivel1(nombre_usuario,intentos):
    nivel = 1
    tiempo = 5
    correctas_x_nivel = 4
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    #Se define la dimensión de la matriz del juego.
    num_ren = 2
    num_col = 2
    print("\nNIVEL 1\n")
    #Se crea una matriz de ceros para guardar los valores.
    matriz=matriz_ceros(num_ren,num_col)
    #Se crean los valores aleatorios dentro la matriz de ceros.
    for ren in range(num_ren):
        for col in range(num_col):
            num = random.randint(1,10)
            matriz[ren][col] = num
    #Muestra la matriz en forma de matriz.        
    muestra_matriz(matriz)
    #"Borra" la pantalla del usuario.
    borra_pantalla(tiempo,nombre_usuario)
    #El usuario da la respuesta al juego:
    print("\n¿Recuerdas la secuencia?\n¡Escríbela!\n")
    respuesta(matriz,nombre_usuario,intentos,num_col,num_ren,tiempo,nivel,correctas_x_nivel)
            
            
        
    
 # Nivel 2 con matriz 3x3.   
def nivel2(nombre_usuario,intentos):
    nivel = 2
    tiempo = 10
    correctas_x_nivel = 9
    comprobacion_intentos(intentos,nombre_usuario,nivel)
    #Se define la dimensión de la matriz del juego.
    num_ren = 3
    num_col = 3
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
    
# Nivel 3 con matriz 5x5 con espacios y números aleatorios. 
def nivel3(nombre_usuario,intentos):
    nivel = 3
    tiempo = 15
    correctas_x_nivel = 25
    #Se define la dimensión de la matriz del juego.
    num_ren = 5
    num_col = 5
    print("\nNIVEL 3\n")
    #Se crea una matriz de números aleatorios.
    matriz=matriz_random(num_ren,num_col)
    # Asigna aleatoriamente "-".
    for ren in range(num_ren+1):
        for col in range(num_col+1):
            num="  -"
            reng=random.randint(0,4)
            colu=random.randint(0,4)
            matriz[reng][colu]=num
    #Muestra la matriz en forma de matriz.
    muestra_matriz(matriz)
    for ren in range(num_ren):
        for col in range(num_col):
            if matriz[ren][col] == "  -":
                matriz[ren][col] = ord("-")
    #"Borra" la pantalla del usuario.
    borra_pantalla(tiempo,nombre_usuario)
    #El usuario da la respuesta al juego:
    print("\n¿Recuerdas la secuencia?\n¡Escríbela!\n")
    respuesta(matriz,nombre_usuario,intentos,num_col,num_ren,tiempo,nivel,correctas_x_nivel)
    



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENÚ PRINCIPAL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
## Función main con el menú principal.
def main():
    nivel_anterior = open("nivel.txt","r")
    nivel=nivel_anterior.read()
    nivel_anterior.close()
    usuario=open("nombre_usuario.txt","r")
    nombre_usuario = usuario.read()
    usuario.close()
    intentos_anterior = open("intentos.txt","r")
    intentos =intentos_anterior.read()
    intentos_anterior.close()
    
    while nivel == "" or nivel != "":
        
         if nivel == "":
            intentos = 1
            print("\n******************************************") 
            print("*                                        *")
            print("*  ¡Bienvenido a Recuerda la secuencia!  *")
            print("*                                        *")
            print("******************************************")
            print("\n¿Cómo te llamas? ",end="")
            nombre_usuario = input()
            print("\nMuy bien,",nombre_usuario," en este juego podrás\
 ejercitar tu memoria de forma fácil y divertida\nSolo tienes que recordar\
 la secuencia de los números que se te mostrarán en pantalla.")
            print("\nInstrucciones:\n* Cuando se te pida la respuesta deberás\
 teclear los números renglón por renglón de forma lineal y separados por espacios.\
\n* Deberás esperar a que el juego te indique o pregunte lo que quieres hacer, de\
 lo contrario no deberás presionar ningúna tecla.\n* Perderás cuanto tu número de\
 intentos sea 3 y volverás a comenzar el juego.")
            print("\n¡Vamos a jugar,",nombre_usuario,"!\n \nEspera...")
            time.sleep(20)
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
            opcion = int(input())
            while (opcion != 2)and(opcion!=1):
                print("\nIngrese el número de la opción que deseé")
                print ("Elige una opción:\n1) Iniciar nueva partida\n2) Continuar partida")
                print("Opción: ",end="")
                opcion=int(input())
            if opcion == 1:
                reiniciar = open('nivel.txt','w')
                reiniciar.write("")
                reiniciar.close()
                re=open("nivel.txt","r")
                nivel=re.read()
                re.close()
                
                
                reiniciar_nombre = open('nombre_usuario.txt','w')
                reiniciar_nombre.write("")
                reiniciar_nombre.close()
                re_nombre=open("nombre_usuario.txt","r")
                nombre_usuario = re_nombre.read()
                re_nombre.close()
                
                reiniciar_intentos = open('intentos.txt','w')
                reiniciar_intentos.write(str(1))
                reiniciar_intentos.close()
                re_intentos = open("intentos.txt","r")
                intentos=re_intentos.read()
                re_intentos.close()
                
            elif opcion == 2:
                print("\n¡Hola,",nombre_usuario,"!\nAnteriormente te quedaste en el nivel",nivel)
                print("Tus intentos hasta ahora son: ",intentos)
                time.sleep(3)
                nivel = int(nivel)
                intentos = int(intentos)
                
                seguir_nivel(nombre_usuario,nivel,intentos)
                break
            
        
        
    
main()  