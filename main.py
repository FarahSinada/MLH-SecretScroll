import pygame
import math

pygame.init()

displayWidth = 800
displayHeight = 700

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('SECRET SCROLL')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
finished = False
safeImg = pygame.image.load('rsz_level1_safe.png')
boxImg = pygame.image.load('rsz level2_leds.png')
scrollImg = pygame.image.load('rszscroll with lightning.png')
safeKnob = pygame.image.load('safe_knob.png')
openScroll = pygame.image.load('rsz_open scroll.png')



def knob(x, y):
    gameDisplay.blit(safeKnob, (x, y))

x = 400
y = 330

# def rotate(x,y,mouse_pos, image):
#     run, rise = (mouse_pos[0], mouse_pos[1])
#     # convert angle to degrees
#     angle = math.degrees(math.atan2(rise, run))
#     rotImage = pygame.transform.rotate(image, -angle)
#     # get rect area of surface; will be centred at given x,y
#     rect = rotImage.get_rect(center=(x, y))
#     return rotImage, rect

# def message_display(text):
#     Message = pygame.font.SysFont("Marlett", 35)
#     MessageRender = N.render(text, True, (0, 0, 0))
#     return MessageRender


# def unlock_safe():
#     level2State = False
#     count = 0
#     # northClick = mouse[0] in range(x+60, x+70) and mouse[1] in range(y, y+20)
# #     unlock sequence
#     # standing on a hill I look west, then east and finally south
#     if westClick:
#         count = 1
#         print(count)
#     if count == 1 and eastClick:
#         count = 2
#         print(count)
#     if count == 2 and southClick:
#         count = 3
#         print(count)
#     if count == 3:
#         print("you did right")
#     return level2State, print(level2State)

def LEDs(x, y, width, height, colour):
    pygame.draw.rect(gameDisplay, colour, [x, y, width, height])

tx, ty = 250,250

# game loop
gameDisplay.blit(safeImg, (0, 0))
level2 = False
level1 = True
foundScroll = False
count2 = []
boxSequence = [4, 2, 1, 3]

while not finished:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            finished = True
        print(event)

        if not level2 and level1:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                northClick = mouse[0] in range(x + 60, x + 70) and mouse[1] in range(y, y + 20)
                eastClick = mouse[0] in range(x+110, x+130) and mouse[1] in range(y+60, y+80)
                westClick = mouse[0] in range(x+10, x+30) and mouse[1] in range(y+60, y+80)
                southClick = mouse[0] in range(x+60, x+80) and mouse[1] in range(y+110, y+130)

                if northClick:
                    # print("you pressed north")
                    knob(x, y)
                elif eastClick:
                    # print("you pressed east")
                    pygame.transform.rotate(safeKnob, 45)
                elif westClick:
                    # print("you pressed west")
                    pygame.transform.rotate(safeKnob, 90)
                elif southClick:
                    # print("you pressed south")
                    pygame.transform.rotate(safeKnob, -45)

                # unlock_safe()
                if westClick:
                    count = 1
                    print(count)
                if count == 1 and eastClick:
                    count = 2
                    print(count)
                if count == 2 and southClick:
                    count = 3
                    print(count)
                if count == 3:
                    level2 = True
                    level1 = False
                    print("you did right")

        elif level2:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                LED1click = mouse[0] in range(170, 250) and mouse[1] in range(350, 430)
                LED2click = mouse[0] in range(280, 360) and mouse[1] in range(350, 430)
                LED3click = mouse[0] in range(390, 470) and mouse[1] in range(350, 430)
                LED4click = mouse[0] in range(505, 580) and mouse[1] in range(350, 430)

                if LED1click:
                    count2.append(1)
                    print('LED1 click')
                    print(count2)
                elif LED2click:
                    count2.append(2)
                    print('LED2 click')
                    print(count2)
                elif LED3click:
                    count2.append(3)
                    print('LED3 click')
                    print(count2)
                elif LED4click:
                    count2.append(4)
                    print('LED4 click')
                    print(count2)

                if boxSequence == count2:
                    print('You got the code!')
                    level1 = False
                    level2 = False
                    foundScroll = True

    if level1:
        knob(x, y)

        N = pygame.font.SysFont("Marlett", 35)
        Npos = N.render("N", True, (0, 0, 0))
        gameDisplay.blit(Npos, (x + 60, y))

        E = pygame.font.SysFont("Marlett", 35)
        Epos = N.render("E", True, (0, 0, 0))
        gameDisplay.blit(Epos, (x + 110, y + 60))

        W = pygame.font.SysFont("Marlett", 35)
        Wpos = N.render("W", True, (0, 0, 0))
        gameDisplay.blit(Wpos, (x + 10, y + 60))

        S = pygame.font.SysFont("Marlett", 35)
        Spos = N.render("S", True, (0, 0, 0))
        gameDisplay.blit(Spos, (x + 60, y + 110))

        riddle = pygame.font.SysFont("Marlett", 40)
        riddleRender = riddle.render("Standing on a hill I look West, then East and finally South", True, (255, 10, 0))
        gameDisplay.blit(riddleRender, (10, 110))

    elif level2:
        gameDisplay.blit(boxImg, (0, 0))
        riddle2 = pygame.font.SysFont("Marlett", 80)
        riddle2Render = riddle2.render("4213", True, (150, 150, 150))
        gameDisplay.blit(riddle2Render, (250, 110))
        LEDs(170, 350, 80, 80, (255, 10, 0))
        LEDs(280, 350, 80, 80, (255, 10, 0))
        LEDs(390, 350, 80, 80, (255, 10, 0))
        LEDs(505, 350, 80, 80, (255, 10, 0))

    elif foundScroll:
        gameDisplay.blit(openScroll, (0, 0))
        endMessage = pygame.font.SysFont("Marlett", 25)
        endMessageRender = endMessage.render("I KNOW WHAT YOU DID LAST SUMMER", True, (250, 0, 10))
        gameDisplay.blit(endMessageRender, (250, 300))


    # display.update only affects part of the screen, .flip updates entire surface
    pygame.display.update()
    # 60 fps
    clock.tick(60)

pygame.quit()
quit()
