import os
clear = lambda: os.system("cls")
clear()

archivo = open("score.txt","a")

pusuario = 0
comodines = 2

correcto = "\033[92m"  # Verde
incorrecto = "\033[91m"  # Rojo
reset = "\033[0m"  # Resetear color

print("**************************************************")
print("*                                                *")
print("*              JUEGO DE PREGUNTAS                *")
print("*                                                *")
print("**************************************************")
print("")
nombre = input("Nombre: ").lower().capitalize()
print("")

print("El juego consiste en responder 10 preguntas:")
print("- 1 fácil (1 punto),")
print("- 4 normales (2 puntos cada una),")
print("- 4 difíciles (3 puntos cada una),")
print("- 1 última pregunta de dificultad extrema (5 puntos).")
print("")
input("Presiona enter para continuar: ")
print("")
print("También tendrás 2 comodines para utilizar, que consisten en eliminar opciones, pero al usarlos se resta 1 punto.")
print("Si usas un comodín en la última pregunta, se restarán 3 puntos.")
print("")
input("Presiona enter para continuar: ")
print("")
print("")
print("Bien, estamos listos para empezar.")
print("")
print("El tema es la serie de television Breaking Bad.")
print("")

tema = "Breaking Bad"
while tema == "Breaking Bad":
    # Pregunta 1 (Fácil)
    print(reset+"-----------------------------------")
    print("Pregunta 1 (Fácil): ¿Cuál es el nombre del protagonista?")
    print("1) Walter White")
    print("2) Jesse Pinkman")
    print("3) Saul Goodman")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")
    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 3) Saul Goodman.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 2 or respuesta < 1:
                print("Ahora que se elimino una opcion.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
    
    if respuesta == 1:
        clear()
        print(correcto + "¡Correcto! Walter White es el protagonista de Breaking Bad.")
        pusuario += 1
    else:
        clear()
        print(incorrecto + "Incorrecto. El protagonista de Breaking Bad es Walter White.")
    # Pregunta 2 (Normal)
    print(reset+"-----------------------------------")
    print("Pregunta 2 (Normal): ¿Quién es el cuñado de Walter White?")
    print("1) Saul Goodman")
    print("2) Hank Schrader")
    print("3) Jesse Pinkman")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 1) Saul Goodman.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 2:
        clear()
        print(correcto + "¡Correcto! El cuñado de Walter White es Hank Schrader.")
        pusuario += 2
    else:
        clear()
        print(incorrecto + "Incorrecto. El cuñado de Walter White es Hank Schrader.")
    # Pregunta 3 (Normal)
    print(reset+"-----------------------------------")
    print("Pregunta 3 (Normal): ¿Qué tipo de cáncer padece Walter White?")
    print("1) Cáncer de pulmón")
    print("2) Cáncer de próstata")
    print("3) Cáncer de hígado")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 2) Cáncer de próstata.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 1:
        clear()
        print(correcto + "¡Correcto! Walter White padece cáncer de pulmón.")
        pusuario += 2
    else:
        clear()
        print(incorrecto + "Incorrecto. Walter White padece cáncer de pulmón.")
    # Pregunta 4 (Normal)
    print(reset+"-----------------------------------")
    print("Pregunta 4 (Normal): ¿Qué personaje de Breaking Bad sufre de parálisis cerebral?")
    print("1) Jane Margolis")
    print("2) Gustavo Fring")
    print("3) Hector Salamanca")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 1) Jane Margolis.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 3:
        clear()
        print(correcto + "¡Correcto! Hector Salamanca sufre de parálisis cerebral.")
        pusuario += 2
    else:
        clear()
        print(incorrecto + "Incorrecto. Hector Salamanca sufre de parálisis cerebral.")
    # Pregunta 5 (Normal)
    print(reset+"-----------------------------------")
    print("Pregunta 5 (Normal): ¿Quién fue la primera persona que asesinó Walter White en Breaking Bad?")
    print("1) Emilio Koyama")
    print("2) Krazy-8")
    print("3) Gustavo Fring")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 2) Krazy-8.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 1:
        clear()
        print(correcto + "¡Correcto! Emilio Koyama fue la primera persona que asesinó Walter White en Breaking Bad.")
        pusuario += 2
    else:
        clear()
        print(incorrecto + "Incorrecto. Emilio Koyama fue la primera persona que asesinó Walter White en Breaking Bad.")
    # Pregunta 6 (Difícil)
    print(reset+"-----------------------------------")
    print("Pregunta 6 (Difícil): ¿Cómo se llama el único episodio de la serie en tener una calificación perfecta de 10/10?")
    print("1) Felina")
    print("2) Face Off")
    print("3) Ozymandias")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 2) Face Off.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 3:
        clear()
        print(correcto + "¡Correcto! El único episodio en tener una calificación perfecta de 10/10 es 'Ozymandias'.")
        pusuario += 3
    else:
        clear()
        print(incorrecto + "Incorrecto. El único episodio en tener una calificación perfecta de 10/10 es 'Ozymandias'.")
    # Pregunta 7 (Difícil)
    print(reset+"-----------------------------------")
    print("Pregunta 7 (Difícil): ¿Qué tipo de negocio utiliza Walter White para lavar dinero?")
    print("1) Un lavadero de autos")
    print("2) Una tienda de cómics")
    print("3) Una galería de arte")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 2) Una tienda de cómics.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 1:
        clear()
        print(correcto + "¡Correcto! Walter White utiliza un lavadero de autos para lavar dinero.")
        pusuario += 3
    else:
        clear()
        print(incorrecto + "Incorrecto. Walter White utiliza un lavadero de autos para lavar dinero.")
    # Pregunta 8 (Difícil)
    print(reset+"-----------------------------------")
    print("Pregunta 8 (Difícil): ¿De qué manera terminó la historia de Breaking Bad?")
    print("1) Walter White muere de una herida de bala")
    print("2) Walter White es arrestado por la DEA")
    print("3) Walter White muere en un enfrentamiento con la policía")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 2) Walter White es arrestado por la DEA.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 1:
        clear()
        print(correcto + "¡Correcto! La serie termina con la muerte de Walter White debido a una herida de bala.")
        pusuario += 3
    else:
        clear()
        print(incorrecto + "Incorrecto. La serie termina con la muerte de Walter White debido a una herida de bala.")
    # Pregunta 9 (Difícil)
    print(reset+"-----------------------------------")
    print("Pregunta 9 (Difícil): ¿Cuántas temporadas tiene la serie Breaking Bad?")
    print("1) 4 temporadas")
    print("2) 5 temporadas")
    print("3) 6 temporadas")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 1
            print("Se ha eliminado la opción 1) 4 temporadas.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 3 or respuesta < 1 or respuesta == 2:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 3 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 2:
        clear()
        print(correcto + "¡Correcto! La serie Breaking Bad tiene 5 temporadas.")
        pusuario += 3
    else:
        clear()
        print(incorrecto + "Incorrecto. La serie Breaking Bad tiene 5 temporadas.")
    # Pregunta 10 (Dificultad extrema)
    print(reset+"-----------------------------------")
    print("Pregunta 10 (Dificultad extrema): ¿En qué año se estrenó el primer episodio de Breaking Bad?")
    print("1) 2006")
    print("2) 2007")
    print("3) 2008")
    print("4) 2009")
    print("5) 2010")
    print("0) Comodín (quedan", comodines, "comodines)")
    print("-----------------------------------")
    respuesta = int(input("Ingresa el número de tu respuesta: "))
    print("")
    while respuesta > 3 or respuesta < 0:
        print("Respuesta inválida. Por favor ingresa un número dentro de las opciones.")
        respuesta = int(input("Ingresa el número de tu respuesta: "))
        print("")

    if respuesta == 0:
        if comodines > 0:
            print("Has usado un comodín para eliminar una opción incorrecta.")
            comodines -= 1
            pusuario -= 3
            print("Se ha eliminado la opción 4) 2009.")
            print("Ahora quedan", comodines, "comodines.")
            while respuesta > 5 or respuesta < 1 or respuesta == 4:
                print("Ahora que se eliminó una opción.")
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")
        else:
            print("Ya has utilizado todos tus comodines.")
            while respuesta > 5 or respuesta < 1:
                respuesta = int(input("Ingresa el número de tu respuesta: "))
            print("")

    if respuesta == 3:
        clear()
        print(correcto + "¡Correcto! El primer episodio de Breaking Bad se estrenó en 2008.")
        pusuario += 5
    else:
        clear()
        print(incorrecto + "Incorrecto. El primer episodio de Breaking Bad se estrenó en 2008.")
    tema="."

print("")
print("")
print(reset+"Puntuación final:", pusuario,"/ 26")
if pusuario < 10:
    print("Aún tienes mucho por descubrir sobre Breaking Bad. Tu puntuación es baja.")
else:
    if pusuario < 20:
        print("¡Bien hecho! Obtuviste una puntuación decente.")
    else:
        if pusuario <= 26:
            print("¡Excelente trabajo! Tu puntuación muestra un gran conocimiento sobre Breaking Bad.")
        else:
            print("¡Felicidades! Eres un experto en Breaking Bad.")
print("")

archivo.write('Usuario: ' + nombre + '\n')
archivo.write('Tema: Breaking Bad ' + '\n')
archivo.write('Puntaje del usuario: ' + "%d" %  pusuario + " de 26" '\n')
archivo.write('----------------'+ '\n')

archivo.close()
