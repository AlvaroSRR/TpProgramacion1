import time
import random

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
                    opcionRespuesta=input(f"Salir- Volver al menú: ")
                    if opcionRespuesta == 9: #control de opcion ingresada
                        jugar = False


print("Gracias por Jugar")
time.sleep(3)       #retraso de 3 segundos