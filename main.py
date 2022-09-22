import pygame
import os
from pygame.locals import *
import keyboard
import random
from debug import debug
import pdb

#shape parameters
size=width,height=(400,800)
road_w=int(width/1.6)
roadmark_w=int(width/80)
#locations parameters
right_lane = width/2-road_w/4
left_lane = width / 2 + road_w / 4
#animation parameters
speed=1

#intiiasing the window
pygame.init()
running = True

#seting the window
screen = pygame.display.set_mode(size)
pygame.display.set_caption("f1_warriors")
#height=int(height/2)

#setting the bg color
screen.fill((0, 0, 200))
#apply changes
pygame.display.update()

plane = pygame.image.load('plane.png')
plane_loc = plane.get_rect()
plane_loc.center = right_lane, height*0.86

plane_2 = pygame.image.load('plane_2.png').convert()
plane_loc_2 = plane_2.get_rect()
plane_loc_2.center = left_lane, height*0.2

pygame.draw.rect(
    screen, (50, 50, 50),
    (width / 2 - road_w / 2, 0, road_w, height))

pygame.draw.rect(
    screen,
    (255, 255, 0),
    (width / 2 - roadmark_w / 2, 0, roadmark_w, height))

pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))

pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

pygame.display.update()
pygame.display.flip()
pygame.display.update()

counter= 0
#game loop
running = True

while running:
    input()
    #screen.fill((0, 0, 200))
    plane_loc_2[1] += 1
    if plane_loc_2[1]> height:
        plane_loc_2[1]=-200

    for event in pygame.event.get():
        if event.type == QUIT():
            #input()
            running = False
            #sys.exit()
            #pygame.quit()


        if event.type == (keyboard.Add_hotkey('a',print,args=('left key'))):
                plane_loc = plane_loc.move([-int(road_w/2),0])
        if event.type in (keyboard.Add_hotkey('d',print,args=('right key'))):
                plane_loc = plane_loc.move([int(road_w / 2), 0])

                if event.type == KEYDOWN:
                    # move user car to the left
                    if event.key in [K_a, K_LEFT]:
                        car_loc = car_loc.move([-int(road_w / 2), 0])
                    # move user car to the right
                    if event.key in [K_d, K_RIGHT]:
                        car_loc = car_loc.move([int(road_w / 2), 0])

                if random.randint(0,1):
                    plane_loc_2=right_lane,-200
                else:
                    plane_loc_2=left_lane,-200
                if plane_loc[0] == plane_loc_2[0] and plane_loc_2 >plane_loc[1] -250:
                    print('GAME OVER')

                screen = pygame.display.set_mode(size)
                screen.fill((0, 0, 200))

                pygame.draw.rect(
                    screen, (50, 50, 50),
                    (width / 2 - road_w / 2, 0, road_w, height))

                pygame.draw.rect(
                    screen,
                    (255, 255, 0),
                    (width / 2 - roadmark_w / 2, 0, roadmark_w, height))

                pygame.draw.rect(
                    screen,
                    (255, 255, 255),
                    (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))

                pygame.draw.rect(
                    screen,
                    (255, 255, 255),
                    (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))


debug(pygame.mouse.get_pos())
debug(pygame.mouse.get_pressed(),40)
debug(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0])

keyboard.wait('esc')
#screen.blit (plane,plane_loc)
screen.blit(plane,(15,20))
#screen.blit (plane_2,plane_loc_2)
screen.blit(plane_2,(10,10))
pygame.display.update()
pygame.display.update()


