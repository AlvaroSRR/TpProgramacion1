import time
from random import randint
#def juegoAlvaro(): #Agregar tab
# Funciones
def imprimirMatriz(matriz):
    print("   ","1","   2","   3","   4","   5")
    i=1
    for fila in matriz:
        print(i,fila)
        i +=1
def disparoJugador(fila, columna,vidaMaquina):
    match barcosMaquina[fila][columna]:
        case "B":
            print("Barco Hundido")
            bombardeoJugador[fila][columna] = "X"
            vidaMaquina -=1
            #print para barco hundido
            time.sleep(2)
        case "-":
            print("Impacto Fallido")
            bombardeoJugador[fila][columna] = "O"
            #agregar print para agua
            time.sleep(2)
        #muestra la matriz de los disparos del jugador
    imprimirMatriz(bombardeoJugador)
    return vidaMaquina

def disparoMaquina(fila, columna,vidaJugador):
    match barcosJugador[fila][columna]:
        case "B":
            print("Barco Hundido")
            bombardeoMaquina[fila][columna] = "X"
            vidaJugador -=1
        case "-":
            print("Impacto Fallido")
            bombardeoMaquina[fila][columna] = "O"
    #muestra la matriz de los disparos de la maquina
    imprimirMatriz(bombardeoMaquina)
    return vidaMaquina
#funcion para crear matrices
def crearMatriz(fila,columna):
    matrizfun = []
    for i in range(fila):
        matrizfun.append(["-"]*columna)
    return matrizfun

jugar=True
print("BATALLA NAVAL")
while jugar:  # mientras "jugar" sea "True", va a repetir
    #matrices para guardar disparos del jugador y maquina
    bombardeoMaquina = crearMatriz(5,5)
    bombardeoJugador = crearMatriz(5,5)
    # Matrices para guardar la posicion de los barcos
    barcosMaquina = crearMatriz(5,5)
    barcosJugador = crearMatriz(5,5)
    #Cargo los barcos para la maquina
    carga = True
    aux = 0 #contador de barcos
    while carga:
        fila = randint(0,4)
        columna = randint(0,4)
        if barcosMaquina[fila][columna]=="-":
            barcosMaquina[fila][columna]="B"
            aux +=1
        if aux == 5: #cuando el contador llega a 5 deja de cargar
            carga =False
    #Cargo los barcos del jugador
    carga = True
    print("Elija la posicion de sus barcos")
    i = 0   #variable para contar los barcos y salir del ciclo
    while carga:
        print(f"Barco nº{i+1}")
        fila=int(input("Fila(1-5): "))-1
        if fila >=0 and fila <=4:
            columna=int(input("Columna(1-5): "))-1
            if columna >=0 and columna <= 4:
                if barcosJugador[fila][columna]=="-":
                    barcosJugador[fila][columna]="B"
                    i+=1
                else:
                    print("coodenada repetida, ingrese nuevamente la coordenada")
                if i ==5:
                    carga=False
            else:
                print("coordenada fuera de rango, ingrese nuevamente la coordenada")
        else:
            print("coordenada fuera de rango, ingrese nuevamente la coordenada")

    #Muestra como queda mi tablero
    print("TU TABLERO")
    imprimirMatriz(barcosJugador)

    #Muestro barcos de la maquina, para test
    for linea in barcosMaquina:
        print(linea)

    time.sleep(2)
    print("")
    print("QUE COMIENCE LA BATALLA")
    print("")
    time.sleep(2)

    #vida de los jugadores
    vidaMaquina = 5
    vidaJugador = 5
    #ciclo para atacar
    ataque=True
    while ataque:
        #pide las coordenas al jugador
        print("Ingrese coordenada")
        fila= int(input("Fila(1-5): "))-1
        if fila >4 or fila < 0:
            print("Fallo en el sistema, pierdes el turno")
        else:
            columna= int(input("Columna(1-5):"))-1
            if columna >4 or columna <0:
                print("Proyectil defectuoso, pierdes el turno")
            else:
                #controla si ya disparo a esas coordenadas
                if bombardeoJugador[fila][columna] == "X" or bombardeoJugador[fila][columna] == "O":
                    print("Coordenadas Repetida, Disparo Fallado")
                else:
                    #llamo la funcion de disparo y actualizo la vida del jugador
                    vidaMaquina = disparoJugador(fila,columna,vidaMaquina)

        #controlo la vida de la maquina , si la vida llega a cero termina el juego
        if vidaMaquina ==0:
            print("GANASTE")
            ataque=False
        else:
            time.sleep(2)
            #elige coordenadas random
            print("Ataca la maquina")
            fila = randint(0,4)
            columna = randint(0,4)
            #controla si se repiten las coordenadas
            if bombardeoMaquina[fila][columna] == "X" or bombardeoMaquina[fila][columna] == "O":
                print("Coordenadas Repetida, Disparo Fallado")
            else:
                vidaJugador= disparoMaquina(fila, columna,vidaJugador)
        #controlo la vida del jugador
        if vidaJugador ==0:
            print("Perdiste")
            ataque=False
    time.sleep(2)
    print("")
    aux = input("1 para salir , ENTER para jugar de nuevo")
    if aux == "1":
        jugar = False
print("salio")
time.sleep(5)

#juegoAlvaro() #llama funcion