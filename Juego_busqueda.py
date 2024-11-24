import random

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