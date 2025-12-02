# Bienvenidos mi nombre es Jeremy Delgado estudiante universitario de UIDE. 
# El presente trabajo a mostrar, es mi proyecto de la materia de logica de programacion, con el profesor Ivan Reyes. 
# Para este proyeto tengo el objetivo, la codificacion de un videojuego.
# El videojuego por el cual me he decidido a codificar es el juego de Piedra, papel o tijera.
# Parte importante de mi proyecto es codificar y comentar mi trabajo. Sin mas que decir comenzamos:

# Aqui estoy creando mi bienvenida, es la presentacion de mi juego#
print('''
         #########################################################  
         #  #     *+*+*+*+*+*+*+ ¡BIENVENIDO! +*+*+*+*+*+*     # #  
         #   #   -----Juego de piedra, papel y tijera-----    #  #  
         #    #    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+    #   #  
         #########################################################  
           ----Elige entre piedra, papel o tijera para jugar----    
          +++++++++++++++++++++++++++++++++++++++++++++++++++++++''')

# Estoy generando una opcion aleatoria para que la computadora pueda elegir entre piedra, papel o tijera.  
import random

# Estoy definiendo una lista con las tres opciones vaidas del juego.
lista = ['piedra', 'papel', 'tijera']

# Aqui estoy creando los contadores de puntos del jugador y la computadora.
puntos_jugador = 0
puntos_computadora = 0

# Aqui estor creando un bucle que repite rondas del juego. Utilizo 'while True' por que no se cuantas rondas habra.
while True:
    
    # Quiero que la computadora eliga aleatoriamente una opcion de la lista.
    computadora = random.choice(lista)
    
    # Inicio la variable 'jugador' con 'None' para indicar que aun no tiene un valor valido.
    # Estoy utilizando 'None' por que me permite controlaar facilmente el ciclo que valida la entrada.
    jugador= None
    
    # Quiero que el ciclo se repita mientras 'jugador' no eliga una de las opciones permitidas.
    # de esta manera me aseguro que solo se pueda continuar si se escribe una de las opciones correctas.
    while jugador not in lista:
        
        # Aquí el jugador elegierá su opcion y quiero que la eleccion del jugador se convierta en minusculas. 
        # Para evitar errores de formato.
        jugador = input('piedra, papel o tijera: ').lower()
        
    # Apartir de aqui ya tengo la elecion del jugador y la computadora.
    # Ahora voy a comparar ambas opciones para determinar el resultado.
    # En caso de empate no habra puntos para ninguno jugador, en caso contrario se sumara un punto al ganador.
    
    # Primero verificare si ambos eligieron las misma opcion.
    # Si el jugador y la computadora son iguales significa que la ronda terminara en empate.  
    if jugador == computadora:
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Empate!')
            
    # Si no hubo empate analizo cada ronda segun lo que haya elegido el jugador.
    
    # Empiezo analizando cuando el jugador escoge 'piedra'       
    elif jugador == 'piedra':
        # Como papel gana a piedra, el jugador pierde la ronda.
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!. Papel gana a Piedra')  
            puntos_computadora += 1 
        # Como piedra gana a tijera, el jugador gana la ronda.       
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!. Piedra gana a Tijera') 
            puntos_jugador += 1
            
    # Ahora analizo si el jugador elige papel.         
    elif jugador == 'papel':
        # Como tijera gana a papel, el jugador pierde. 
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!. Tijera gana a papel')
            puntos_computadora += 1 
        # Como papel gana a piedra, el jugador gana.        
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!. Papel gana a Piedra')
            puntos_jugador += 1
            
    # Ahora analizo si el jugador elige tijera.                 
    elif jugador == 'tijera':
        # Como piedra gana a tijera, el jugador pierde.
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste!. Piedra gana a Tijera')
            puntos_computadora += 1 
            
        # Como tijera gana a papel, el jugador gana.        
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste!. Tijera gana a papel')
            puntos_jugador += 1
            
    # Aqui mostrare el resultado de cada ronda         
    print(f"puntaje de Jeremy:{puntos_jugador}, puntaje de computadora: {puntos_computadora} ")        
            
            
    # Aqui estoy preguntando a el jugador quiere seguir jugando y que lo que escriba se convierta en minusculas    
    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (si/no): ').lower()
 
    # Aqui estoy verificando que si la respuesta del jugador no es si o se escribe algo distinto.
    # El juego entiende que ya no quieres seguir jugando y se usa break para salir del ciclo principal.
    if jugar_de_nuevo != 'si':
        break
    
# Al final del juego muestro el ganador final con los puntos obtenidos por cada ronda.
print("==========================================================                  ")
print("************###########################******************                   ")
print("            RESULTADO FINAL DEL JUEGO                                       ")
print(f"          Jugador {puntos_jugador}        Computadora {puntos_computadora} ")

# Aquí comparo los puntajes finales para decidir quién ganó el juego.
# Esta parte es importante porque resume el resultado final después de todas las rondas.
if puntos_jugador > puntos_computadora:
    print("¡Felicidades! ¡Ganaste el juego!")
elif puntos_computadora > puntos_jugador:
    print("La computadora ganó el juego. ¡Suerte la próxima!")
else:
    print("¡El juego terminó en empate!")
print('Gracias por jugar. ¡ADIOS!')
print("           #############################                                    ")
print("*************                           ******************                  ")
print("==========================================================                  ")
