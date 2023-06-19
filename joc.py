import pygame
import time
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
color_fondo = (0, 0, 0)
color_cabeza = (0, 255, 0)
color_cuerpo = (0, 200, 0)
color_comida = (255, 0, 0)

# Tamaño de la ventana del juego
ancho_ventana = 800
alto_ventana = 600

# Tamaño del bloque
tamano_bloque = 20

# Velocidad del juego (menor valor = mayor velocidad)
velocidad = 15

# Creación de la ventana del juego
ventana_juego = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Snake Game")

# Reloj del juego
reloj = pygame.time.Clock()

# Fuente para el marcador
fuente_marcador = pygame.font.SysFont(None, 40)


def mostrar_marcador(puntuacion):
    marcador = fuente_marcador.render("Puntuación: " + str(puntuacion), True, (255, 255, 255))
    ventana_juego.blit(marcador, (10, 10))


def dibujar_serpiente(tamano_bloque, lista_serpiente):
    for segmento in lista_serpiente:
        pygame.draw.rect(ventana_juego, color_cuerpo, [segmento[0], segmento[1], tamano_bloque, tamano_bloque])


def jugar_snake():
    # Posición inicial de la serpiente
    x_cabeza = ancho_ventana / 2
    y_cabeza = alto_ventana / 2

    # Cambio inicial de posición
    cambio_x = 0
    cambio_y = 0

    # Lista que representa la serpiente
    lista_serpiente = []
    longitud_serpiente = 1

    # Posición y movimiento aleatorio de la comida
    x_comida = round(random.randrange(0, ancho_ventana - tamano_bloque) / 20.0) * 20.0
    y_comida = round(random.randrange(0, alto_ventana - tamano_bloque) / 20.0) * 20.0

    # Variable para controlar si el juego ha terminado
    fin_juego = False

    # Variable para controlar la puntuación
    puntuacion = 0

    while not fin_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    cambio_x = -tamano_bloque
                    cambio_y = 0
                elif evento.key == pygame.K_RIGHT:
                    cambio_x = tamano_bloque
                    cambio_y = 0
                elif evento.key == pygame.K_UP:
                    cambio_y = -tamano_bloque
                    cambio_x = 0
                elif evento.key == pygame.K_DOWN:
                    cambio_y = tamano_bloque
                    cambio_x = 0

        if x_cabeza >= ancho_ventana or x_cabeza < 0 or y_cabeza >= alto_ventana or y_cabeza < 0:
            fin_juego = True

        x_cabeza += cambio_x
        y_cabeza += cambio_y

        ventana_juego.fill(color_fondo)
        pygame.draw.rect(ventana_juego, color_comida, [x_comida, y_comida, tamano_bloque, tamano_bloque])

        cabeza_serpiente = []
        cabeza_serpiente.append(x_cabeza)
        cabeza_serpiente.append(y_cabeza)
        lista_serpiente.append(cabeza_serpiente)

        if len(lista_serpiente) > longitud_serpiente:
            del lista_serpiente[0]

        for segmento in lista_serpiente[:-1]:
            if segmento == cabeza_serpiente:
                fin_juego = True

        dibujar_serpiente(tamano_bloque, lista_serpiente)
        mostrar_marcador(puntuacion)

        pygame.display.update()

        if x_cabeza == x_comida and y_cabeza == y_comida:
            x_comida = round(random.randrange(0, ancho_ventana - tamano_bloque) / 20.0) * 20.0
            y_comida = round(random.randrange(0, alto_ventana - tamano_bloque) / 20.0) * 20.0
            longitud_serpiente += 1
            puntuacion += 1

        reloj.tick(velocidad)

    pygame.quit()


# Ejecución del juego
jugar_snake()
