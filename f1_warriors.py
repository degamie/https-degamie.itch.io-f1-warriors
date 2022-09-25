import pygame, random
from pygame.locals import *

# shape parameters
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
# location parameters
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
# animation parameters
speed = 1

# initiallize the app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)
# set window title
pygame.display.set_caption("f1_warriors")
# set background colour
screen.fill((0, 0, 200))
# apply changes
pygame.display.update()

# load player vehicle
plane = pygame.image.load("plane.png")
# resize image
plane = pygame.transform.scale(plane, (250, 250))
plane = pygame.transform.rotate(plane, 360)
plane_loc = plane.get_rect()
plane_loc.center = right_lane, height * 0.8

# load enemy vehicle
plane2 = pygame.image.load("plane_2.png")
plane2 = pygame.transform.scale(plane2, (250, 250))
plane2 = pygame.transform.rotate(plane2, -180)
plane2_loc = plane2.get_rect()
plane2_loc.center = left_lane, height * 0.2

counter = 0
# game loop
while running:
    counter += 1

    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level! Reached ,congrats", speed)

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
        print("GAME OVER!RESTART THE MATCH LVL..")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            # collapse the app
            running = False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                plane_loc = plane_loc.move([-int(road_w / 2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                plane_loc = plane_loc.move([int(road_w / 2), 0])

    # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
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
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()