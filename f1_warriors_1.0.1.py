import operator
import pygame,random,PIL
from pygame.locals import *

#build_debug_mobile
#import com.microsoft.appcenter.AppCenter;
#import com.microsoft.appcenter.analytics.Analytics;
#import com.microsoft.appcenter.crashes.Crashes;

# shape parameters
size = width, height = (800, 720)
playerX=width
PlayerY=height
playerX_change = 0
x=35
y=35
road_w = int(width / 1.0)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 4 + road_w / 2
left_lane = width / 2 - road_w / 4
# animation parameters
speed = 10
# initiallize the app
pygame.init()
running = True
#pygame_font_initialization
pygame.font.init()
# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("f1_warriors")

icon_1_img = pygame.image.load('plane_2_2.png')
logo_1 = pygame.display.set_icon(icon_1_img)
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
plane = pygame.image.load("plane_1.png")
#plane_X=492
#plane_Y=492
#plane=370
#plane=int(plane)
# resize ima
#plane = pygame.image.load("plane_.png")
# resize ima
plane = pygame.transform.scale(plane, (492, 492))
plane = pygame.transform.rotate(plane, 360)
plane_loc = plane.get_rect()
#plane_loc_1 = plane.get_rect()
plane_loc.center = right_lane, height * 0.8
#plane_loc_1.center = left_lane, height * 0.16
# load enemy vehicle
plane2 = pygame.image.load("plane_2.png")
#plane2_X=492
#plane2_Y=492
plane2 = pygame.transform.scale(plane2, (492, 492))
plane2 = pygame.transform.rotate(plane2, -180)
plane2_loc = plane2.get_rect()
plane2_loc.center = left_lane, height * .8
#planeX_2=492
counter = 0
plane_change=0
#playerX=plane
#playerX = 0

#def plane(x,y):
   #screen.blit(plane,(x,y))

#def plane2(x,y):
    #screen.blit(plane2,(x,y))

#global game_end_1
#global game_end_display_1


def start():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                pygame.quit()
            quit()

            if event.key == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    run = False

                elif event.KEY == pygame.K_q:
                    pygame.quit()
                    quit()
                    screen.fill("Black")
                    pygame.display.set_caption("PAUSE!")
                    pygame.display.set_caption("play!")
                    pygame.display.update()
                    #font =pygame.font.Font("freesansbold.tff",24)

#def set_background():
    #global  background
    #screen.fill(0,0,0)
    #screen.blit((background),(0,0))

def show_score(speed,x,y):
        font = pygame.font.SysFont('freesansbold.tff',30)
        score_1 = font.render("Level Reached: " + str(speed), True, (200,0, 205))
        print("level! Reached ,congrats", speed)
        screen.blit(score_1,(x, y))
        pygame.display.update()

#def boundaries(planeX_1):
        #planeX_1 = 492
        #planeX_1+= plane_change
        #if planeX_1 < 0:
            #planeX_1= 0
        #elif planeX_1< 736:
            #planeX_1= 736

        #elif event.key == pygame.K_c:
        #start()



# game loop
while running:
    #planeX_1=plane
    #plane2X_1=plane2
    counter += 1
    #game_ui_play=play()
    # increase game difficulty overtime
    if counter == 5000:
        speed += 4
        counter = 0


#def game_over():
    if plane_loc[0] == plane2_loc[0] and plane2_loc[1] > plane_loc[1] - 250:
        font = pygame.font.SysFont('freesansbold.tff',24)
        font = pygame.font.SysFont('freesansbold.tff', 60)
        x = 50
        y = 50
        #for game_end in 5:
        game_end = font.render("GAME OVER! RESTART THE LeveL.. ", True, (200, 0, 205))
        screen.blit(game_end, (x, y))
        pygame.display.update()
        print("GAME OVER! RESTART THE LVL..")
        #print("The Plane is out of runway")
        break

    # animate enemy vehicle
    plane2_loc[1] += speed
    if plane2_loc[1] > height:
        # randomly select lane
        if random.randint(0, 1) == 0:
            plane2_loc.center = right_lane, -200
        else:
            plane2_loc.center = left_lane, -200


    #def Game_over(speed,x=0,y=0):
        #if plane_loc[0] == plane2_loc[0] and plane2_loc[1] > plane_loc[1] - 250:
                #gamee_end=print("GAME OVER!RESTART THE LVL..")
                #font = pygame.font.SysFont('freesansbold.tff',24)
                #game_end_1= font.render("GAME OVER!RESTART THE LVL.. " + str(speed), True, (200, 0, 205))
                #game_end_1_display=screen.blit(game_end_1,(x, y))
                #break
               #pygame.display.update()
                #x = 0
                #y = 0


    #Game_over(speed,x,y)



    # event listeners

    # event listeners

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
                #plane_loc=plane_loc.move(speed)
                    #running = False
                    #screen.blit(plane_loc)
                    # break
                    #plane_change = 5
                    #print("The Plane is out of runway")
            # move user car to the right

                #screen.blit(plane_loc)



            #if event.key in [K_a, K_LEFT]:
                    #plane_loc_2
                    # plane_loc_1= plane_loc_1.move([-int((road_w)/2), 0])
                    #plane_loc= plane_loc.move([-int((road_w-left_lane)/1.5), 0])
                    #running=False
                    #plane_change=-5
                    #print("The Plane is out of runway")
                    # plane_loc_1= plane_loc.move([-int((road_w)/2), 0])





            #right_mov(plane_loc)
            #left_mov(plane_loc)

            #font = pygame.font.SysFont('freesansbold.tff', 24)
            #game_end_1 = font.render("GAME OVER!RESTART THE LVL.. " + str(speed), True, (200, 0, 205))
            #game_end_1_display = screen.blit(game_end_1, (x, y))
            #print(game_end_1_display)
    #break
                #running= False
                #font = pygame.font.SysFont('freesansbold.tff', 60)
                #game_end = font.render("The Plane is out of runway", True, (200, 0, 205))
                #screen.blit(game_end, (x, y))
                #pygame.display.update()
                #print("The Plane is out of runway")



                # move user car to the left



                #if event.key in [K_a,K_l]:
                #plane_loc = plane_loc.move([-int((road_w)/2), 0])

                #plane_change = 5

            #event.key in [K_SPACE,]:
                #playerX=planeX_1
            #if plane_loc.colliderect(plane2):
                #pygame .draw.rect(screen,(255,10,0),rect,4)


            #boundaries(planeX_1)
            #start()
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
    screen.blit(plane,plane_loc)
    screen.blit(plane2,plane2_loc)
    #screen.blit(source, dest, area = None, special_flags = 0)
    #score_display
    show_score(speed,x,y)
    #plane(x,y)
    #plane2(x,y)
    #set_background()

    #screen.blit(play())
    #pygame.Rect(screen, (0,0,0),plane2,4)
    # apply changes
    pygame.display.update()
    pygame.display.update()

    #m = MainApp()
    #if __name__=='__main__':
        #m.run()
# collapse application window
pygame.quit()

