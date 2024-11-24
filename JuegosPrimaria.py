import time
import random
from random import randint



salir = False           #defino variable Boleana para while de menu
while salir==False:     #mientras "salir" sea "False", va a repetir

    print("======================================")
    print("    4 en 1     ")
    print("======================================")
    print("1- Luana\n2- Nano\n3- David\n4- Alvaro\n9- Salir")
    numJuego= int(input("Ingresa la opción de juego: "))

    if numJuego == 9:   #control de numero ingresado
        salir = True    #cambia el estado de la variable y finaliza el programa
    else:
        jugar = True    #defino variable boleana para while de juego

        match numJuego: #segun el contenido de la variable elige la opción correspondiente

            case 1:             #si el contenido es 1
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Luana
                    print("Luana")
                    opcionRespuesta=int(input("9- Volver al menú: "))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 2:             #si el contenido es 2
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Nano
                    print("Nano")
                    # Generamos el nombre del jugador y el nombre del robot.
                    nombre_jugador = input("Ingresar nombre del jugador: ").upper()
                    año_nacimiento = int(input("Ingresar año de nacimiento: "))
                    nombre_mecha = str(año_nacimiento)[:2] + nombre_jugador[:2] + str(año_nacimiento)[-2:]

                    # Creamos un diccionario con los datos del jugador y estadisticas
                    personaje = {'nombre': nombre_jugador, 'mecha': nombre_mecha, 'vida': 100, 'ataque': 20, 'defensa': 10}

                    # Matriz de puntaje
                    puntuaciones = []

                    # Arrancamos el juego
                    print(f"\nBienvenido, {nombre_jugador}. Vas a pilotar tu mecha {nombre_mecha}")
                    print("Debes detener a los invasores enemigos.")
                    print("¡ADELANTE!")

                    # Sistema de combate, aca calculamos el daño que hacemos y nos hacen
                    def combate(enemigo, vida_enemigo, ataque_enemigo, defensa_enemigo):
                        daño_total = 0
                        while vida_enemigo > 0 and personaje['vida'] > 0:
                            # Calculamos el daño del jugador
                            daño_jugador = max(0, personaje['ataque'] - defensa_enemigo)
                            vida_enemigo -= daño_jugador
                            daño_total += daño_jugador
                            print(f"Disparas contra el {enemigo} y le causas {daño_jugador} de daño.")
                            if vida_enemigo <= 0:
                                print(f"{enemigo} DERROTADO")
                                break
                            
                            # Calculamos el daño del enemigo
                            daño_enemigo = max(0, ataque_enemigo - personaje['defensa'])
                            personaje['vida'] -= daño_enemigo
                            print(f"El {enemigo} causa {daño_enemigo} de daño a tu armadura. Tu vida es de: {personaje['vida']}")
                            if personaje['vida'] <= 0:
                                print("¡Los escudos colapsan! ¡El enemigo te ha derrotado!")
                                return False
                            
                        # Calculo de puntaje
                        puntuaciones.append([personaje['nombre'], daño_total])
                        return True

                    # Elecciones para el jugador
                    juego = True
                    while juego:
                        print("\nLa ciudad está siendo destruida. ¿Qué vas a hacer?")
                        print("1) Ir al centro de la ciudad")
                        print("2) Ir directo a la nave del enemigo")
                        print("3) Buscar armamento en el arsenal del centro")
                        print("4) Buscar al equipo de reparación")
                        print("5) Cazar a los enemigos que están explorando")
                        print("6) Ver estadísticas del mecha")
                        print("7) Puntuacion")
                        opcion = int(input("Elige una opción (1-7): "))

                        # If para determinar las opciones
                        if opcion == 1:
                            print("\nExploras el centro de la ciudad.")
                            if random.choice([True, False]):
                                print("¡Te encuentras con un grupo de enemigos!")
                                vida_enemigo, ataque_enemigo, defensa_enemigo = 70, 20, 8
                                juego = combate("Soldados Enemigos", vida_enemigo, ataque_enemigo, defensa_enemigo)
                            else:
                                print("No encuentras enemigos pero descubres armamento enemigo abandonado.")
                                print("Encuentras una batería más potente para tus escudos. Tu capacidad de defensa aumenta.")
                                personaje['defensa'] += 5
                        
                        elif opcion == 2:
                            print("\nTe diriges a la nave enemiga.")
                            print("¡Te encuentras de frente con el comandante enemigo!")
                            vida_enemigo, ataque_enemigo, defensa_enemigo = 200, 25, 15
                            juego = combate("Comandante Enemigo", vida_enemigo, ataque_enemigo, defensa_enemigo)
                            if juego:
                                print("¡Derrotaste al comandante enemigo, las tropas hostiles se retiran!")
                                juego = False
                        
                        elif opcion == 3:
                            print("\nBuscas armamento en el arsenal.")
                            if random.choice([True, False]):
                                print("¡Te encuentras con un grupo de enemigos!")
                                vida_enemigo, ataque_enemigo, defensa_enemigo = 70, 20, 8
                                juego = combate("Soldados Enemigos", vida_enemigo, ataque_enemigo, defensa_enemigo)
                                if juego:
                                    print("¡Encuentras un arma de mayor calibre!")
                                    personaje['ataque'] += 10
                            else:
                                print("El arsenal fue saqueado completamente.")

                        elif opcion == 4:
                            print("\nBuscas al equipo de reparación.")
                            if random.choice([True, False]):
                                print("¡Te encuentras con un grupo de enemigos!")
                                vida_enemigo, ataque_enemigo, defensa_enemigo = 100, 20, 10
                                juego = combate("Mecha Enemigo", vida_enemigo, ataque_enemigo, defensa_enemigo)
                                if juego:
                                    print("Encuentras a tu equipo de apoyo y reparan tu armadura balística.")
                                    personaje['vida'] = min(100, personaje['vida'] + 100)
                            else:
                                print("No encuentras a tu equipo de apoyo.")

                        elif opcion == 5:
                            print("\nEmboscas a los exploradores enemigos.")
                            if random.choice([True, False]):
                                print("¡Te enfrentas a un mecha explorador enemigo!")
                                vida_enemigo, ataque_enemigo, defensa_enemigo = 90, 20, 10
                                juego = combate("Mecha Explorador Enemigo", vida_enemigo, ataque_enemigo, defensa_enemigo)
                                if juego:
                                    print("Encuentras información crucial, encuentras el punto débil de su armadura.")
                                    personaje['ataque'] += 5
                            else:
                                print("Los exploradores enemigos te detectan y escapan.")
                        
                        elif opcion == 6:
                            print("\nEstadísticas del mecha:")
                            print(f"Nombre del Mecha: {personaje['mecha']}")
                            print(f"Vida: {personaje['vida']}")
                            print(f"Ataque: {personaje['ataque']}")
                            print(f"Defensa: {personaje['defensa']}")
                        
                        elif opcion == 7: 
                            print("\nPuntuacion del jugador:") 
                            for puntuacion in puntuaciones: 
                                print(f"Nombre: {puntuacion[0]}, Puntos: {puntuacion[1]}")
                        else:
                            print("Opción no válida. Intenta de nuevo.")

                    # Puntuación al final 
                    print("\nPuntuacion final") 
                    total_puntos = sum(puntuacion[1] for puntuacion in puntuaciones)
                    print(f"Jugador: {personaje['nombre']}, Puntos totales: {total_puntos}")

                    print("El juego ha terminado.")
                    opcionRespuesta=int(input("9- Volver al menú: "))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 3:             #si el contenido es 3
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código David
                    print("David")
                    opcionRespuesta=int(input("9- Volver al menú: "))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 4:             #si el contenido es 4
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Alvaro
                    def juegoAlvaro():
                        # Funciones
                        #imprime matrices
                        def imprimirMatriz(matriz):
                            print("   ", "1", "   2", "   3", "   4", "   5")
                            i = 1
                            for fila in matriz:
                                print(i, fila)
                                i += 1
                        #verifica disparo del jugador
                        def disparoJugador(fila, columna, vidaMaquina):
                            match barcosMaquina[fila][columna]:
                                case "B":
                                    print("Barco Hundido")
                                    bombardeoJugador[fila][columna] = "X"
                                    vidaMaquina -= 1
                                    # print para barco hundido
                                    time.sleep(1)
                                case "-":
                                    print("Impacto Fallido")
                                    bombardeoJugador[fila][columna] = "O"
                                    # agregar print para agua
                                    time.sleep(1)
                                # muestra la matriz de los disparos del jugador
                            imprimirMatriz(bombardeoJugador)
                            return vidaMaquina
                        #verifica disparo de la maquina
                        def disparoMaquina(fila, columna, vidaJugador):
                            match barcosJugador[fila][columna]:
                                case "B":
                                    print("Barco Hundido")
                                    bombardeoMaquina[fila][columna] = "X"
                                    vidaJugador -= 1
                                case "-":
                                    print("Impacto Fallido")
                                    bombardeoMaquina[fila][columna] = "O"
                            # muestra la matriz de los disparos de la maquina
                            imprimirMatriz(bombardeoMaquina)
                            return vidaMaquina

                        # funcion para crear matrices
                        def crearMatriz(fila, columna):
                            matrizfun = []
                            for i in range(fila):
                                matrizfun.append(["-"] * columna)
                            return matrizfun
                        """empieza el juego"""
                        jugar = True
                        print("BATALLA NAVAL\n")
                        while jugar:  # mientras "jugar" sea "True", va a repetir
                            # matrices para guardar disparos del jugador y maquina
                            bombardeoMaquina = crearMatriz(5, 5)
                            bombardeoJugador = crearMatriz(5, 5)
                            # Matrices para guardar la posicion de los barcos
                            barcosMaquina = crearMatriz(5, 5)
                            barcosJugador = crearMatriz(5, 5)
                            # Cargo los barcos para la maquina
                            carga = True
                            aux = 0  # contador de barcos
                            while carga:
                                fila = randint(0, 4)
                                columna = randint(0, 4)
                                if barcosMaquina[fila][columna] == "-":
                                    barcosMaquina[fila][columna] = "B"
                                    aux += 1
                                if aux == 5:  # cuando el contador llega a 5 deja de cargar
                                    carga = False
                            # Cargo los barcos del jugador
                            carga = True
                            print("Elija la posicion de sus barcos")
                            i = 0  # variable para contar los barcos y salir del ciclo
                            while carga:
                                print(f"\nBarco nº{i + 1}")
                                fila = int(input("Fila(1-5): ")) - 1
                                if fila >= 0 and fila <= 4:
                                    columna = int(input("Columna(1-5): ")) - 1
                                    if columna >= 0 and columna <= 4:
                                        if barcosJugador[fila][columna] == "-":
                                            barcosJugador[fila][columna] = "B"
                                            i += 1
                                        else:
                                            print("coodenada repetida, ingrese nuevamente la coordenada")
                                        if i == 5:
                                            carga = False
                                    else:
                                        print("coordenada fuera de rango, ingrese nuevamente la coordenada")
                                else:
                                    print("coordenada fuera de rango, ingrese nuevamente la coordenada")

                            # Muestra como queda mi tablero
                            print("\nTU TABLERO")
                            imprimirMatriz(barcosJugador)
                            time.sleep(1)

                            print("\nQUE COMIENCE LA BATALLA")
                            time.sleep(1)
                            #imprimirMatriz(barcosMaquina)  ++++++ Muestra barcos de la maquina
                            # vida de los jugadores
                            vidaMaquina = 5
                            vidaJugador = 5
                            # ciclo para atacar
                            ataque = True
                            while ataque:
                                # pide las coordenas al jugador
                                print("\nATACA JUGADOR")
                                fila = int(input("Fila(1-5): ")) - 1
                                if fila > 4 or fila < 0:
                                    print("Fallo en el sistema, pierdes el turno")
                                else:
                                    columna = int(input("Columna(1-5):")) - 1
                                    if columna > 4 or columna < 0:
                                        print("Proyectil defectuoso, pierdes el turno")
                                    else:
                                        # controla si ya disparo a esas coordenadas
                                        if bombardeoJugador[fila][columna] == "X" or bombardeoJugador[fila][
                                            columna] == "O":
                                            print("Coordenadas Repetida, Disparo Fallado")
                                        else:
                                            # llamo la funcion de disparo y actualizo la vida del jugador
                                            vidaMaquina = disparoJugador(fila, columna, vidaMaquina)

                                # controlo la vida de la maquina , si la vida llega a cero termina el juego
                                if vidaMaquina == 0:
                                    print("\nGANASTE")
                                    ataque = False
                                else:
                                    time.sleep(1)
                                    # elige coordenadas random
                                    print("\nATACA MAQUINA")
                                    fila = randint(0, 4)
                                    columna = randint(0, 4)
                                    # controla si se repiten las coordenadas
                                    if bombardeoMaquina[fila][columna] == "X" or bombardeoMaquina[fila][columna] == "O":
                                        print("Coordenadas Repetida, Disparo Fallado")
                                    else:
                                        vidaJugador = disparoMaquina(fila, columna, vidaJugador)
                                # controlo la vida del jugador
                                if vidaJugador == 0:
                                    print("\nPERDISTE")
                                    ataque = False

                            time.sleep(1)
                            aux = input("\n1 para salir , ENTER para jugar de nuevo")
                            if aux == "1":
                                jugar = False
                        print("Gracias por Jugar")
                        time.sleep(2)
                    juegoAlvaro()
                    jugar = False



print("Gracias por Jugar")
time.sleep(2)       #retraso de 2 segundos