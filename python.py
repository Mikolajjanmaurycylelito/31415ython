import pygame
import time
import random

pygame.init()

orange = (255,140,0)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 100, 0)
beige = (255, 228, 196)

dis_width = 500
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Πython Game by Mikołaj Lelito')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 11

font_style = pygame.font.SysFont("bradleyhand", 20)
score_font = pygame.font.SysFont("bradleyhand", 20)
title_font = pygame.font.SysFont("bradleyhand", 35)

def title_card():
    title = title_font.render("Πython Game by Mikołaj Lelito", True, orange)
    dis.blit(title, [dis_width/2 - title.get_width()/2, dis_height/4])
    subtitle = font_style.render("In this slimy game, you play as hungry python hunting for pies.", True, orange)
    dis.blit(subtitle, [dis_width/2 - subtitle.get_width()/2, dis_height/2])
    pygame.display.update()
    time.sleep(5)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(beige)
            message("Game Over! Press C to Play Again or Q to Quit", black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(beige)
        font = pygame.font.SysFont("bradleyhand", snake_block * 2)
        pi_symbol = font.render("π", True, red)
        dis.blit(pi_symbol, (foodx - snake_block / 2, foody - snake_block / 2))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

title_card()
gameLoop()
