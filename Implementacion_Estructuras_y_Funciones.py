# Bienvenidos, mi nombre es Jeremy Delgado, estudiante universitario de la UIDE.
# Este es mi proyecto final de lógica de programación con el profesor Iván Reyes.
# Para este trabajo elegí desarrollar el videojuego clásico: Piedra, papel o tijera.
# En esta nueva versión del código, busco mejorar la organización, la eficiencia
# y la legibilidad en comparación con la primera versión. A continuación explico
# paso a paso cómo funciona esta versión optimizada.

# Aquí muestro la pantalla de bienvenida, que es la presentación inicial del juego.
print('''
         #########################################################  
         #  #     *+*+*+*+*+*+*+ ¡BIENVENIDO! +*+*+*+*+*+*     # #  
         #   #   -----Juego de piedra, papel y tijera-----    #  #  
         #    #    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+    #   #  
         #########################################################  
           ----Elige entre piedra, papel o tijera para jugar----    
          +++++++++++++++++++++++++++++++++++++++++++++++++++++++''')

# Importo el módulo random para que la computadora pueda elegir opciones al azar.
import random

# Aquí defino una tupla con las opciones válidas del juego.
# Utilizo una tupla porque no necesito modificar sus valores.
opciones = ("piedra", "papel", "tijera")

# --------------------------- FUNCIÓN 1 --------------------------- #
# Esta función obtiene la jugada del usuario.
def obtener_jugada_usuario(opciones):
    # Inicio la variable jugador sin valor válido.
    jugador = None

    # Mantengo un ciclo hasta que el usuario escriba una opción correcta.
    while jugador not in opciones:
        # Aquí el usuario escribe su elección.
        # strip() quita espacios, lower() convierte a minúsculas.
        jugador = input("piedra, papel o tijera: ").strip().lower()

    # Retorno la jugada válida del jugador.
    return jugador

# --------------------------- FUNCIÓN 2 --------------------------- #
# Esta función obtiene la jugada de la computadora de manera aleatoria.
def obtener_jugada_computadora(opciones):
    # random.choice elige una opción al azar dentro de la tupla.
    return random.choice(opciones)

# --------------------------- FUNCIÓN 3 --------------------------- #
# Esta función determina quién gana la ronda.
def determinar_ganador(jugador, computadora):

    # Primero verifico si hay empate.
    if jugador == computadora:
        return "empate"

    # Aquí utilizo un diccionario para simplificar las reglas del juego.
    # Cada opción gana a la opción asignada.
    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }

    # Si la regla indica que el jugador vence a la computadora, gana el jugador.
    if reglas[jugador] == computadora:
        return "jugador"
    else:
        # Caso contrario, la computadora gana la ronda.
        return "computadora"

# --------------------------- FUNCIÓN PRINCIPAL --------------------------- #
# Esta función controla todo el flujo del juego: rondas, puntajes y repetición.
def main():

    # Aquí inicializo los contadores de puntos.
    puntos_jugador = 0
    puntos_computadora = 0

    # Ciclo principal del juego que se repite hasta que el usuario quiera salir.
    while True:

        # Obtengo la jugada aleatoria de la computadora.
        computadora = obtener_jugada_computadora(opciones)

        # Obtengo la jugada válida ingresada por el usuario.
        jugador = obtener_jugada_usuario(opciones)

        # Muestro las elecciones de ambos jugadores.
        print("Computadora:", computadora)
        print("Jugador:", jugador)

        # Determino el resultado utilizando la función que creé antes.
        resultado = determinar_ganador(jugador, computadora)

        # Según el resultado, muestro el mensaje correspondiente y actualizo puntajes.
        if resultado == "empate":
            print("¡Empate!")
        elif resultado == "jugador":
            print("¡Ganaste!")
            puntos_jugador += 1
        else:
            print("Perdiste...")
            puntos_computadora += 1

        # Aquí muestro el puntaje actualizado después de cada ronda.
        print(f"puntaje de Jeremy: {puntos_jugador}, puntaje de computadora: {puntos_computadora}")

        # Pregunto al jugador si quiere continuar.
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()

        # Si no responde "si", el ciclo se detiene y el juego termina.
        if jugar_de_nuevo != "si":
            break

    # --------------------- RESULTADO FINAL --------------------- #
    print("==========================================================")
    print("************###########################******************")
    print("            RESULTADO FINAL DEL JUEGO")
    print(f"          Jugador {puntos_jugador}        Computadora {puntos_computadora} ")

    # Aquí determino quién ganó según el puntaje acumulado.
    if puntos_jugador > puntos_computadora:
        print("¡Felicidades! ¡Ganaste el juego!")
    elif puntos_computadora > puntos_jugador:
        print("La computadora ganó el juego. ¡Suerte la próxima!")
    else:
        print("¡El juego terminó en empate!")

    # Mensaje de despedida.
    print("Gracias por jugar. ¡ADIOS!")
    print("#############################")
    print("*************                           ******************")
    print("==========================================================")

# Llamo a la función principal para iniciar el juego.
main()
