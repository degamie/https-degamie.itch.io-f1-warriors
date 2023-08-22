import pygame, random
from pygame.locals import *
#import pyparsing
from main_menu_game_ui import play

# shape parameters
size = width, height = (800, 720)
road_w = int(width / 1.0)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 4 + road_w / 2
left_lane = width /2 - road_w /4
# animation parameters
speed = 8
# initiallize the app
pygame.init()
running = True
#pygame_font_initialization
pygame.font.init()
# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("f1_warriors")
#logo_display
icon_1_img=pygame.image.load('plane.png')
logo_1=pygame.display.set_icon(icon_1_img)
# set background colour
screen.fill((0, 0, 200))
# apply changes
pygame.display.update()
#sound_game_end
#mixer.music.load("f1_warriors_game_end_!.wav")
#mixer.music.play(-1)
#mixer.music.load("f1_warriors_game_end_4.wav")
#mixer.music.play(-1)
# load player vehicle
plane = pygame.image.load("plane.png")
# resize ima
plane = pygame.transform.scale(plane, (492, 492))
plane = pygame.transform.rotate(plane, 360)
plane_loc = plane.get_rect()
plane_loc.center = right_lane, height * 0.8

# load enemy vehicle
plane2 = pygame.image.load("plane_2.png")
plane2 = pygame.transform.scale(plane2, (492, 492))
plane2 = pygame.transform.rotate(plane2, -180)
plane2_loc = plane2.get_rect()
plane2_loc.center = left_lane, height * .8
counter = 0

def start():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            quit()

            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    run= False

                elif event.KEY == pygame.K_q:
                    pygame.quit()
                    quit()
                    screen.fill("Black")
                    pygame.display.set_caption("PAUSE!")
                    pygame.display.set_caption("play!")
                    pygame.display.update()
                    #font =pygame.font.Font("freesansbold.tff",24)

# game loop
while running:
    counter += 1
    #game_ui_play=play()
    # increase game difficulty overtime
    if counter == 5000:
            speed += 4
            counter = 0
            print("level! Reached ,congrats", speed)

            #font = pygame.font.SysFont('freesansbold.tff',24)

    def show_score(speed,x, y):
        font = pygame.font.SysFont('freesansbold.tff',24)
        score_1 = font.render("level Reached!" + str(speed), True, (255, 250, 205))
        screen.blit(score_1, x, y,speed)
        pygame.display.update()

    # animate enemy vehicle
    plane2_loc[1] += speed
    if plane2_loc[1] > height:
        # randomly select lane
        if random.randint(0, 1) == 0:
            plane2_loc.center = right_lane, -200
        else:
            plane2_loc.center = left_lane, -200

    # end game logic
    if plane_loc[0] == plane2_loc[0] and plane2_loc[1] > plane_loc[1] - 250:
        #sound_play_game_end
        #pygame.mixer_music.load("f1_warriors_game_end_!.wav")
        #pygame.mixer_music.play(-1)
        #pygame.music_mixer.load("f1_warriors_game_end_4.wav")
        #pygame.music_mixer.play(-1)
        print("GAME OVER!RESTART THE LVL..")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
        if event.type== KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                plane_loc = plane_loc.move([-int(road_w / 2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                plane_loc = plane_loc.move([int(road_w / 2), 0])
            #if plane_loc.colliderect(plane2):
                #pygame .draw.rect(screen,(255,10,0),rect,4)

        #def boundaries(plane):
                if plane <= 0:
                    plane = 0
                elif plane <= 736:
                    plane = 736

                elif event.key == pygame.K_c:
                    start()

                    #boundaries(plane)
    # draw road
    road_1=pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2- roadmark_w / 2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # place car images on the screen
    screen.blit(plane, plane_loc)
    screen.blit(plane2, plane2_loc)
    #score_display

    # #screen.blit(play())
    #pygame.Rect(screen, (0,0,0),plane2,4)
    # apply changes
    pygame.display.update()
    pygame.display.update()
# collapse application window
pygame.quit()

