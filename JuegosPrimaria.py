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
                    def busqueda_tesoro(tablero, fila_tesoro, columna_tesoro):
                        intentos = 0
                        encontrado = False
                        #Bucle mientras no se haya encontrado el tesoro
                        while encontrado == False:
                            for i in range(5):
                                for j in range(5):
                                    if tablero[i][j] == "⬜":
                                        print("⬜", end=" ")
                                    elif tablero[i][j] == "❌":
                                        print("❌", end=" ")
                                    elif tablero[i][j] == "💎":
                                        print("💎", end=" ")
                                    else:
                                        print(" ", end=" ")
                                print()

                            #Validación de ingreso de n° de filas
                            fila = -1
                            while not (0 <= fila < 5):
                                fila = int(input("Ingrese el número de fila (1-5): ")) - 1
                                if not (0 <= fila < 5):
                                    print("ERROR! Ingrese un número entre 1 y 5")

                            #Validación de ingreso de n° de columnas
                            columna = -1
                            while not (0 <= columna < 5):
                                columna = int(input("Ingrese el número de columna (1-5): ")) - 1
                                if not (0 <= columna < 5):
                                    print("ERROR! Ingrese un número entre 1 y 5")

                            #Verificamos si se acertó la posición
                            if fila == fila_tesoro and columna == columna_tesoro:
                                tablero[fila][columna] = "💎"
                                print("\n¡Encontraste el tesoro! ¡¡¡GANASTE!!!")
                                #Mostramos el tablero con el tesoro
                                for i in range(5):
                                    for j in range(5):
                                        if tablero[i][j] == "⬜":
                                            print("⬜", end=" ")
                                        elif tablero[i][j] == "❌":
                                            print("❌", end=" ")
                                        elif tablero[i][j] == "💎":
                                            print("💎", end=" ")
                                        else:
                                            print(" ", end=" ")
                                    print()
                                #Finalizamos el juego con tesoro encontrado
                                encontrado = True
                            else:
                                #Marcamos x el lugar como un intento fallido
                                if tablero[fila][columna] != "💎" and tablero[fila][columna] != "❌":
                                    tablero[fila][columna] = "❌"

                                intentos += 1
                                print(f"\nNo está ahí el tesoro. Intento {intentos}/5")

                                #Intentos llega a 5, pierde y termina
                                if intentos >= 5:
                                    print(f"\nPerdiste! El tesoro estaba en la posición ({fila_tesoro + 1}, {columna_tesoro + 1})")
                                    break

                    #Armamos matriz con cuadrados
                    tablero = []
                    for j in range(5):
                        tablero.append(["⬜"] * 5)

                    #Posición del tesoro aleatoriamente
                    fila_tesoro = random.randint(0, 4)
                    columna_tesoro = random.randint(0, 4)

                    print("BÚSQUEDA DEL TESORO\n")
                    print("El tablero tiene un tamaño de 5x5")
                    print("Debe adivinar las coordenadas del tesoro\n")

                    #Llamamos función para iniciar el juego
                    busqueda_tesoro(tablero, fila_tesoro, columna_tesoro)

                    opcionRespuesta=input("9- Volver al menú, ENTER para jugar de nuevo: ")
                    if opcionRespuesta =="9":  #control de opcion ingresada
                        jugar=False

            case 2:             #si el contenido es 2
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Nano
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
                    opcionRespuesta=input("9- Volver al menú, ENTER para jugar de nuevo: ")
                    if opcionRespuesta =="9":  #control de opcion ingresada
                        jugar=False

            case 3:             #si el contenido es 3
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código David
                    def JuegoDavidH():
                        print("Bienvenido al juego de adivinanzas, Dont Take The Clues ")
                        time.sleep(3)
                        print(
                            "El juego consiste en adivinar la palabra, tienes 5 intentos, buena suerte y recuerda Dont Take The Clues")
                        time.sleep(3)
                        print("Empezamos en...")
                        time.sleep(2)
                        print("3..")
                        time.sleep(2)
                        print("2..")
                        time.sleep(2)
                        print("1..")
                        time.sleep(2)

                        palabras = ["EXTRAORDINARIO", "HEMEROTECA", "EPIDEMIOLOGIA", "PSIQUIATRICO", "CRONOLOGIA",
                                    "HIPOPOTOMONSTROSESQUIPEDALIOFOBIA", "ANISOTROPIA"]

                        palabra = random.choice(palabras)
                        estado_palabra = []
                        adivinanzas = [
                            "En el lienzo del tiempo se despliega con destellos efímeros, pintando el cielo nocturno con promesas lejanas. Es el eco lumínico de la eternidad, cuya canción se escucha en silencio.",
                            "Custodio incansable de los secretos de la tierra, su murmullo incita sueños en los corazones inquietos. Con sus aguas profundas y su danza eterna, guarda misterios que solo el valiente osa descubrir.",
                            "Es la fuerza imperceptible que guía el curso de las vidas, invisible a los ojos, pero sentida en el alma. Es el arquitecto del destino, trazando caminos en el vasto mapa del universo.",
                            "En la quietud de su refugio, tejió una red de esperanzas y deseos. Con paciencia infinita, observa el mundo pasar, atrapando en su abrazo los sueños fugaces de quienes se atreven a soñar.",
                            "Es el escultor del espacio, que con manos invisibles moldea la luz y la sombra. Aunque intangible, su obra es omnipresente, definiendo la existencia con cada gesto imperceptible."
                            ]

                        respuestas_adivinanzas = ["ESTRELLA", "OCEANO", "DESTINO", "NOCHE", "GRAVEDAD"]

                        for i in palabra:
                            estado_palabra.append("_")

                        intentos = 5

                        while intentos > 0:
                            if "_" not in estado_palabra:
                                print(f"Enhorabuena adivinaste la palabra {palabra}")
                                break

                            letra = input("Ingrese una letra: ").upper()
                            if letra in palabra:

                                for posicion, letra_palabra in enumerate(palabra):
                                    if letra_palabra == letra:
                                        estado_palabra[posicion] = letra
                            else:
                                print("letra incorrecta")
                                intentos -= 1
                                aux = True  # modi
                                while aux:  # modi
                                    # pista como str
                                    pista = input(
                                        "Ingrese 1 para obtener una pista o presione cualquier otro tecla para rechazar: ")
                                    if pista == "1":  # control como str
                                        print(
                                            "Veo que necesitas una ayuda, si resuelves la siguiente adivinanza seras recompensado con una pista de lo contrario el juego continua:")
                                        time.sleep(3)
                                        random_adivinanza = random.randint(0, len(adivinanzas) - 1)
                                        print(adivinanzas[random_adivinanza])

                                        respuesta = input("Ingrese la respueta: ").upper()
                                        if respuesta == respuestas_adivinanzas[random_adivinanza]:
                                            if palabra == "EXTRAORDINARIO":
                                                print(
                                                    "Felicidades esta es la pista sobre la palabra a adivinar: Es el solitario caminante en el sendero de lo cotidiano, que ilumina con su presencia lo mundano, transformando lo ordinario en asombro. Es el artista del universo, cuya obra maestra no se encuentra en lo común, sino en lo singular y excepcional, desafiando siempre los límites de la imaginación. ")
                                            elif palabra == "HEMEROTECA":
                                                print(
                                                    "Felicidades esta es la pista sobre la palabra a adivinar: Es el guardián de los ecos del pasado, donde las voces del tiempo se archivan y los susurros del ayer encuentran refugio. Este santuario de hojas y tinta preserva las memorias de lo transitorio, convirtiendo cada página en un testamento de la historia humana, esperando ser redescubierta por los curiosos del presente. ")
                                            elif palabra == "EPIDEMIOLOGIA":
                                                print(
                                                    "Felicidades esta es la pista sobre la palabra a adivinar: Es el faro en la tormenta, el cartógrafo de lo invisible que traza mapas de la salud y la enfermedad en el vasto océano de la humanidad. Con su mirada perspicaz, descifra patrones ocultos y desvela la danza de los microbios y humanos, tejiendo la red de causas y consecuencias que nos unen en el ciclo interminable de la vida. ")
                                            elif palabra == "PSIQUIATRICO":
                                                print(
                                                    "Felicidades esta es la pista sobre la palabra a adivinar: Es el refugio de las mentes inquietas, el bastión donde los pensamientos errantes encuentran su camino. En sus recintos, las tormentas del alma se enfrentan con la sabiduría serena, y los laberintos internos son desentrañados con delicadeza. Es el lugar donde el silencio se convierte en diálogo y el caos interior se transforma en armonía.")
                                            elif palabra == "CRONOLOGIA":
                                                print(
                                                    "Felicidades esta es la pista sobre la palabra a adivinar: Es el hilandero invisible que teje la tela del tiempo, marcando cada punto en el vasto tapiz de la existencia. Con precisión meticulosa, narra la historia del universo desde su nacimiento hasta el presente, ordenando los eventos en un desfile inmutable. En sus manos, los momentos se convierten en eslabones de una cadena eterna, conectando el pasado, el presente y el futuro en una sinfonía temporal.")
                                            elif palabra == "HIPOPOTOMONSTROSESQUIPEDALIOFOBIA":
                                                print(
                                                    "Felicidades esta es la sobre la palabra a adivinar: Es el monstruo escondido en las sombras del léxico, un titán de sílabas que se erige como un coloso imponente en el paisaje de la lengua. Con cada letra, susurra temores y ansiedades a quienes se acercan, despertando el pavor en aquellos que enfrentan sus largos tentáculos fonéticos. En su corazón, reside el miedo no solo a su propia extensión, sino a la vastedad y complejidad que representa.")
                                            elif palabra == "ANISOTROPIA":
                                                print("Felicidades esta es la pista sobre la palabra a adivinar: ")
                                        else:
                                            print("Respuesta incorrecta, el juego continua")
                                            time.sleep(2)
                                            # aux = False #cambio variable
                                    # if pista == "1": #controla pista como str
                                    aux = False  # cambio variable

                            print("Palabra: ", estado_palabra)

                        if intentos == 0:
                            print("Intentos acabados, puedes volver a intentarlo")

                    def JuegoDavidE():
                        print("Bienvenido al juego de adivinanzas")
                        time.sleep(3)
                        print("El juego consiste en adivinar la palabra, tienes 5 intentos, buena suerte")
                        time.sleep(3)
                        print("Empezamos en...")
                        time.sleep(2)
                        print("3..")
                        time.sleep(2)
                        print("2..")
                        time.sleep(2)
                        print("1..")
                        time.sleep(2)

                        palabras = ["EXTRAORDINARIO", "HEMEROTECA", "EPIDEMIOLOGIA", "PSIQUIATRICO",
                                    "CRONOLOGIA"]  # Crea una lista con las palabras que tiene que adivinar

                        palabra = random.choice(palabras)  # La palabra va a ser cualquier de la lsita
                        estado_palabra = []  # Lista vacia que va a contener la palabra
                        adivinanzas = [
                            "Brilla en la noche y guía a los viajeros. Es una",
                            "Ocupa gran parte del planeta, azul y profundo. Es el",
                            "Destino inevitable que todos compartimos. Es el",
                            "Es oscura y aparece al final del dia. Es la",
                            "Fuerza que nos mantiene pegados al suelo. Es la"
                        ]  # Adivinanzas que son partes del juego

                        respuestas_adivinanzas = ["ESTRELLA", "OCEANO", "DESTINO", "NOCHE",
                                                  "GRAVEDAD"]  # Respuesta de adivinanzas

                        for i in palabra:
                            estado_palabra.append(
                                "_")  # Agrega un espacio despendiendo la cantidad de posciones que tiene la palabra

                        intentos = 5  # Numero de intentos que tiene el jugador

                        while intentos > 0:  # Verifica intentos y que todos los _ esten ocupados por una letra
                            if "_" not in estado_palabra:
                                print(f"Enhorabuena, adivinaste la palabra {palabra}")
                                break

                            letra = input("Ingrese una letra: ").upper()

                            if letra in palabra:  # Si la letra ingresada esta en la palabra ocupara el espacio
                                for posicion, letra_palabra in enumerate(palabra):
                                    if letra_palabra == letra:
                                        estado_palabra[posicion] = letra
                            else:
                                print("Letra incorrecta")
                                intentos -= 1
                                aux = True  # Variable auxiliar para controlar el bucle
                                while aux:
                                    pista = input(
                                        "Ingrese 1 para obtener una pista sencilla o presione cualquier otro tecla para rechazar: ")
                                    if pista == "1":  # control como str
                                        print(
                                            "Veo que necesitas una ayuda, si resuelves la siguiente adivinanza seras recompensado con una pista de lo contrario el juego continua:")
                                        time.sleep(3)
                                        random_adivinanza = random.randint(0,
                                                                           len(adivinanzas) - 1)  # Elige una adivinanza al azar y al usar el mismo indice que la lista de respuesta verifica
                                        print(adivinanzas[random_adivinanza])

                                        respuesta = input("Ingrese la respueta: ").upper()
                                        if respuesta == respuestas_adivinanzas[random_adivinanza]:
                                            if palabra == "EXTRAORDINARIO":
                                                print(
                                                    "Felicidades esta es la simple pista sobre la palabra a adivinar: Es algo que no es común ni ordinario, sobresale por su calidad. ")
                                            elif palabra == "HEMEROTECA":
                                                print(
                                                    "Felicidades esta es la simple pista sobre la palabra a adivinar: Es un lugar donde se guardan periódicos y revistas antiguos.. ")
                                            elif palabra == "EPIDEMIOLOGIA":
                                                print(
                                                    "Felicidades esta es la simple pista sobre la palabra a adivinar: Es la ciencia que estudia las enfermedades y cómo se propagan en las poblaciones. ")
                                            elif palabra == "PSIQUIATRICO":
                                                print(
                                                    "Felicidades esta es la simple pista sobre la palabra a adivinar: Se refiere a un lugar o tratamiento relacionado con la salud mental..")
                                            elif palabra == "CRONOLOGIA":
                                                print(
                                                    "Felicidades esta el la simple pista sobre la palabra a adivinar: Se refiere a un lugar o tratamiento relacionado con la salud mental..")

                                        else:
                                            print("Respuesta incorrecta, el juego continua")
                                            time.sleep(2)

                                    aux = False  # cambio variable

                            print("Palabra:", estado_palabra)

                        if intentos == 0:
                            print("Intentos acabados, puedes volver a intentarlo")

                    dificultad = input(
                        "Elija dificultad: 1_Modo Facil 2_Modo Hardcore: ")  # Preguntar el modo que desea jugar el usuario
                    if dificultad == "1":
                        JuegoDavidE()
                    else:
                        JuegoDavidH()
                    opcionRespuesta=input("9- Volver al menú, ENTER para jugar de nuevo: ")
                    if opcionRespuesta =="9":  #control de opcion ingresada
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