import random
import time

print("Bienvenido al juego de adivinanzas, Dont Take The Clues ")
time.sleep(3)
print("El juego consiste en adivinar la palabra, tienes 5 intentos, buena suerte y recuerda Dont Take The Clues")
time.sleep(3)
print("Emepezamos en...")
time.sleep(2)
print("3..")
time.sleep(2)
print("2..")
time.sleep(2)
print("1..")
time.sleep(2)


palabras=["EXTRAORDINARIO", "HEMEROTECA", "EPIDEMIOLOGIA", "PSIQUIATRICO", "CRONOLOGIA", "HIPOPOTOMONSTROSESQUIPEDALIOFOBIA", "ANISOTROPIA"]


palabra=random.choice(palabras)
estado_palabra = []
adivinanzas=["En el lienzo del tiempo se despliega con destellos efímeros, pintando el cielo nocturno con promesas lejanas. Es el eco lumínico de la eternidad, cuya canción se escucha en silencio.",
             "Custodio incansable de los secretos de la tierra, su murmullo incita sueños en los corazones inquietos. Con sus aguas profundas y su danza eterna, guarda misterios que solo el valiente osa descubrir.",
             "Es la fuerza imperceptible que guía el curso de las vidas, invisible a los ojos, pero sentida en el alma. Es el arquitecto del destino, trazando caminos en el vasto mapa del universo.",
             "En la quietud de su refugio, tejió una red de esperanzas y deseos. Con paciencia infinita, observa el mundo pasar, atrapando en su abrazo los sueños fugaces de quienes se atreven a soñar.",
             "Es el escultor del espacio, que con manos invisibles moldea la luz y la sombra. Aunque intangible, su obra es omnipresente, definiendo la existencia con cada gesto imperceptible."
             ]

respuestas_adivinanzas = ["ESTRELLA", "OCEANO", "DESTINO", "NOCHE", "GRAVEDAD"]

for _ in palabra:
    estado_palabra.append("_")

intentos=5



while intentos > 0:
    if "_" not in estado_palabra:
        print(f"Enhorabuena adivinaste la palabra {palabra}")
        break

    letra=input("Ingrese una letra: ").upper()
    if letra in palabra:

        for posicion, letra_palabra in enumerate(palabra):
            if letra_palabra == letra:
                estado_palabra[posicion] = letra
    else:
        print("letra incorrecta")
        intentos -= 1
        while True:
            pista = int(input("Ingrese 1 para obtener una pista sencilla o presione cualquier otro numero para rechazar: "))
            if pista == 1:
                print("Veo que necesitas una ayuda, si resuelves la siguiente adivinanza seras recompensado con una pista de lo contrario el juego continua:")
                time.sleep(3)
                random_adivinanza = random.randint(0, len(adivinanzas) - 1)
                print(adivinanzas[random_adivinanza])

                respuesta=input("Ingrese la respueta: ").upper()
                if respuesta == respuestas_adivinanzas[random_adivinanza]:
                    if palabra == "EXTRAORDINARIO":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el solitario caminante en el sendero de lo cotidiano, que ilumina con su presencia lo mundano, transformando lo ordinario en asombro. Es el artista del universo, cuya obra maestra no se encuentra en lo común, sino en lo singular y excepcional, desafiando siempre los límites de la imaginación. ")
                    elif palabra == "HEMEROTECA":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el guardián de los ecos del pasado, donde las voces del tiempo se archivan y los susurros del ayer encuentran refugio. Este santuario de hojas y tinta preserva las memorias de lo transitorio, convirtiendo cada página en un testamento de la historia humana, esperando ser redescubierta por los curiosos del presente. ")
                    elif palabra == "EPIDEMIOLOGÍA":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el faro en la tormenta, el cartógrafo de lo invisible que traza mapas de la salud y la enfermedad en el vasto océano de la humanidad. Con su mirada perspicaz, descifra patrones ocultos y desvela la danza de los microbios y humanos, tejiendo la red de causas y consecuencias que nos unen en el ciclo interminable de la vida. ")
                    elif palabra == "PSIQUIÁTRICO":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el refugio de las mentes inquietas, el bastión donde los pensamientos errantes encuentran su camino. En sus recintos, las tormentas del alma se enfrentan con la sabiduría serena, y los laberintos internos son desentrañados con delicadeza. Es el lugar donde el silencio se convierte en diálogo y el caos interior se transforma en armonía.")
                    elif palabra == "CRONOLOGÍA":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el hilandero invisible que teje la tela del tiempo, marcando cada punto en el vasto tapiz de la existencia. Con precisión meticulosa, narra la historia del universo desde su nacimiento hasta el presente, ordenando los eventos en un desfile inmutable. En sus manos, los momentos se convierten en eslabones de una cadena eterna, conectando el pasado, el presente y el futuro en una sinfonía temporal.")
                        break
                    elif palabra == "HIPOPOTOMONSTROSESQUIPEDALIOFOBIA":
                        print(
                            "Felicidades esta el la simple pista sobre la palabra a adivinar: Es el monstruo escondido en las sombras del léxico, un titán de sílabas que se erige como un coloso imponente en el paisaje de la lengua. Con cada letra, susurra temores y ansiedades a quienes se acercan, despertando el pavor en aquellos que enfrentan sus largos tentáculos fonéticos. En su corazón, reside el miedo no solo a su propia extensión, sino a la vastedad y complejidad que representa.")
                    elif palabra == "ANISOTROPÍA":
                        print("Felicidades esta el la simple pista sobre la palabra a adivinar: ")
                else:
                    print("Respuesta incorrecta, el juego continua")
                    time.sleep(2)
                    break
            if pista != 1:
                break





    print("Palabra: ",estado_palabra)



if intentos == 0:
    print("Intentos acabados, puedes volver a intentarlo")