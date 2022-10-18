#############################################################################################
#Se importan las librerias necesarias, siendo PyGame la principal y la que nos va a permitir#
#desarrollar todo el juego + algunas como refuerzo y facilitar ciertas tareas               #
#############################################################################################

import pygame
from sys import exit
from random import randint


#Se crea una funcion para calcular la puntuacion del jugador
def display_score():
    score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font.render(f'Pt: {score}', False, 'Yellow')
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf,score_rect)


def wave_movement(wave_list):
    if wave_list:
        for wave_rect in wave_list:
            wave_rect.x -= randint(-5,10)
            wave_rect.y -= randint(-5,10)

            screen.blit(enem_surface, wave_rect)

            wave_list = [wave for wave in wave_list if wave.x > -100]

        return wave_list
    else: return []

def Colision(player,waves):
    if waves:
        for wave_rect in waves:
            if player.colliderect(wave_rect): #Condicion de Game Over
                return False
    return True


##################
#Se inicia Pygame#
##################
pygame.init()









#######################
#Renderizado principal#
#######################

#Se renderiza una ventana

screen = pygame.display.set_mode((800,400))
#Variables para las distintas rondas
Wave = 1


#Se le atribuye un nombre a la nueva ventana
pygame.display.set_caption('pyGame test Eduardo Merino Jimenez')
#Variable que servira mas tarde para ajustar los FPS segun necesario
clock = pygame.time.Clock()

#Variable que define a su vez el tipo de fuente (valor1 define la ruta y el tipo de fuente, valor 2 define el tamaño)
font = pygame.font.Font('Fonts/VCR_OSD_MONO.ttf', 25)
font2 = pygame.font.Font('Fonts/VCR_OSD_MONO.ttf', 100)
font3 = pygame.font.Font('Fonts/VCR_OSD_MONO.ttf', 20)

#Game over o no Game over
game_active = False
start_time = 0

###############################################
#Se inicia una superficie sobre la ventana    #
#En este caso la del jugador, terreno y demas.#
###############################################

#Anti-ghosting

#########################################################################################################################
#Explicacion: Cada vez que dibujamos un frame en la ventana, este se dibuja encima del frame existente, creando ghosting#
#########################################################################################################################

NG_surface = pygame.Surface((800,400))
NG_surface.fill('black')

#########################################################################################################################

######################################################################################################
#OPCIONAL: se puede utilizar .convert() para optimizar, aunque es recomendable usar .convert_alpha() #
#La diferencia principal es que .convert() NO respeta los valores Alpha mientras que                 #
#.convert_alpha() si los respeta                                                                     #
######################################################################################################


#Terreno
ground_surface = pygame.Surface((200,200))
ground_surface.fill('Blue')

#Jugador + variables para el movimiento + sistema de colisiones (triangulos)
player_surface = pygame.image.load('Graphics/P1DEBUG.png').convert_alpha()

#Enemigo + variables para el movimiento + sistema de colisiones (triangulos)

enem_surface = pygame.image.load('Graphics/ENEMYDEBUG.png').convert_alpha()
enem_rect = enem_surface.get_rect(midbottom = (80,300))
wave_rect_list = []




#Variables para el movimiento
playerX = 200
playerY = 100

#Obtiene la direccion del mouse
mouse_pos = pygame.mouse.get_pos()


#Rectangulos de colision







#Texto [valor1 indica el texto en pantalla, valor2 Si queremos aplicarle AntiAliasing, valor3 es el color.]

text_surface = font2.render('GAME OVER', False, 'Black' )
text_rect = text_surface.get_rect(center = (400,50))
text1_surface = font3.render('Pulsa R para continuar', False, 'Black' )
text1_rect = text1_surface.get_rect(midbottom = (400,200))
#text2_surface = font.render(f'Ronda: {waveNum}', False, 'Yellow' )
#text2_rect = text2_surface.get_rect(bottomright = (530,200))

#Los valores (h,w) determinan el tamaño de la superficie en caso de no ser una imagen

#Contador para aumentar la cantidad de enemigos y la velocidad
wave = pygame.USEREVENT + 1
pygame.time.set_timer(wave,1500)



#Se crea un loop que mantenga esa ventana abierta + la capacidad de obtener un input del jugador para cerrarla
while True:
   
    #Con este codigo se crea una forma de resetear el juego tras un Game Over, ademas, registra los inputs del usuario
    #Para permitir el movimiento (En debug tambien se da la tecla de movimiento pulsada en ese momento)
    #O bien, pulsando la R indica si el juego esta en un estado de Game Over/Inactivo y resetea el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
             if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            print('D')
             if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            print('S')
             if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            print('A')
             if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            print('W')         
             if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            print(game_active)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                print(game_active)
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
      
    if event.type == wave and game_active:
        wave_rect_list.append(enem_surface.get_rect(midbottom = (randint(-10,850),randint(-10,450))))
        
                
               
    ######################################################################################
    #Se agrega un surface y su posicion en pantalla para mas tarde                       #
    #RECORDATORIO: en PyGame las cordenadas 0,0 representan la esquina superior derecha  #
    #                                                                                    #
    #Los renderizados de cada superficie funcionan como las capas de Photoshop           #
    #Segun el orden en el que se encuentre, se hara visible (o no) ciertos elementos     #
    #En pantalla.                                                                        #
    ######################################################################################


    #Obtiene la direccion del mouse y traslada al jugador dependiendo de este
    mouse_pos = pygame.mouse.get_pos()
    player_rect = player_surface.get_rect(center = (mouse_pos))

    



    


    if game_active:
        #Muestra la ronda y la puntuacion
        display_score()

        #AntiGhosting (Actua como capa de fondo, para prevenir overlap en cada frame)
        screen.blit(NG_surface, (0,0))

        #Jugador (Actuaria como Capa 1) [Triangulado]

        #################################################################################################
        #Esta parte del codigo asegura que el movimiento este sincronizado con el rectangulo de colision#
        #################################################################################################

        if player_rect.right <= 0 : player_rect.left = 800
        screen.blit(player_surface, player_rect)
    
        #Enemigo Capa 2

        #enem_rect.x -= randint(1,10)
        #enem_rect.y -= randint(1,10)
        if enem_rect.bottom <= 0 : enem_rect.top = 400
        

        #IA Enemiga
        wave_rect_list = wave_movement(wave_rect_list)
        

        #Texto Capa 3 [Muestra la puntuacion]
        display_score()

        ####################################################################################
        #Colision entre enemigo y jugador                                                  #
        #Esto devuelve TRUE o FALSE, por lo tanto, si el valor es TRUE se dara un GAME OVER#
        ####################################################################################
        #DEBUG: print(player_rect.colliderect(enem_rect)) para comprobar la colision

        ##########################################################################################
        #Colision. Se crea un rectangulo que definira a su vez la colision y posicion del jugador#
        #.get_rect(midbottom/bottom/top/midtop/left/right/center/ = (x, y))                      #
        ##########################################################################################
        game_active = Colision(player_rect, wave_rect_list)

    else:
        screen.fill('Red')
        screen.blit(text_surface, text_rect)
        screen.blit(text1_surface, text1_rect)
        wave_rect_list.clear()



    #renderizado y actualizacion de frames
    pygame.display.update()
    #Se limita el framerate a 30, para evitar problemas de compatibilidad
    clock.tick(30)


