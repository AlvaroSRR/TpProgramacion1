import time

salir = False           #defino variable Boleana para while de menu
while salir==False:     #mientras "salir" sea "False", va a repetir

    print("======================================")
    print("     Bienvenido a Aprender Jugando")
    print("======================================")
    print("1- Luana\n2- Nano\n3- David\n4- Alvaro\n5- Maicol\n6- Camila\n9- Salir")
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
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 2:             #si el contenido es 2
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Nano
                    print("Nano")
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 3:             #si el contenido es 3
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código David
                    print("David")
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta ==9:  #control de opcion ingresada
                        jugar=False

            case 4:             #si el contenido es 4
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Alvaro
                    print("Alvaro")
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta == 9: #control de opcion ingresada
                        jugar = False

            case 5:             #si el contenido es 5
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Maicol
                    print("Maicol")
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta == 9: #control de opcion ingresada
                        jugar = False

            case 6:             #si el contenido es 6
                while jugar:    #mientras "jugar" sea "True", va a repetir
                    #código Camila
                    print("Camila")
                    opcionRespuesta=int(input("9- Volver al menú"))
                    if opcionRespuesta == 9: #control de opcion ingresada
                        jugar = False

print("Gracias por Jugar")
time.sleep(3)       #retraso de 3 segundos