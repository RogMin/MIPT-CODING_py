import pygame
from pygame.draw import *
import random
import pandas as pd
import os

max_ball_amount = 3
balls = []
colors = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "GREEN": (0, 255, 0),
    "MAGENTA": (255, 0, 255),
    "CYAN": (0, 255, 255),
}
score = 0


def init_game(FPS=144):
    """ Start game """
    df = pd.DataFrame({"Player name": [], "Score": []})
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    game_tick(screen, FPS, df)


def get_random_color():
    return random.choice(list(colors.values()))


def create_ball():
    """ Creates new ball, return ref to ball """
    if len(balls) < max_ball_amount:
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        r = random.randint(30, 50)
        return balls.append([(x, y), r, [get_random_color()],0,0])


def move_balls(x_speed = 5, y_speed = 5):
    """ Move and bounce """
    for b in balls:
        if b[3] == 0 or b[4] == 0:
            b[3] = random.randint(-x_speed, x_speed)
            b[4] = random.randint(-y_speed, y_speed)
        if b[0][1] - b[1] <= 0 or b[0][1] + b[1] >= 900: # collision process with wall
            b[4] = -b[4]
        if b[0][0] - b[1] <= 0 or b[0][0] + b[1] >= 1200:
            b[3] = -b[3]
        for c in balls: # collision process with balls
            if (c != b and ((c[0][0]-b[0][0])**2) + ((c[0][1]-b[0][1])**2)) <= (b[1] + c[1])**2:
                c[3] = -((b[1] * b[3]) / c[1])
                b[3] = -((c[1] * c[3]) / b[1])
                c[4] = -((b[1] * b[4]) / c[1])
                b[4] = -((c[1] * c[4]) / b[1])
        b[0] = (b[0][0] + b[3], b[0][1] + b[4])


def draw_balls(screen):
    """ Render balls in display """
    if len(balls) > 0:
        for b in balls:
            color = (b[2][0])
            xy = (b[0][0], b[0][1])
            r = b[1]
            circle(screen, color, xy, r)


def get_leader_table(df):
    """ Generate fake leaders data frame """
    def get_random_name():
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                      'y', 'z']
        res = []
        for i in range(random.randint(2, 3)):
            res.append(vowels[random.randint(1, len(vowels)-1)])
            res.append(consonants[random.randint(1, len(consonants)-1)])
        res[0].upper()
        return (''.join(res).capitalize())
    for i in range(10):
        df.loc[len(df.index)] = [get_random_name(), random.randint(0,34)]
    return df


def game_tick(screen, FPS,df):
    """ Game cycle """
    global score
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                df = get_leader_table(df)
                df.loc[len(df.index)] = [os.getlogin(),score]
                print(df.sort_values(by='Score'))
                df.to_csv('results.csv', index=False)
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
              i = score
              score += click(event.pos[0], event.pos[1], screen)
              if score != i:
                  print("Score: ", score)
        clock.tick(FPS)
        create_ball()
        draw_balls(screen)
        move_balls()
        pygame.display.update()
        screen.fill((0, 0, 0))


def click(pos_x, pos_y, screen):
    """ Process button click
        pos_x: int, x-coordinate of cursor
        pos_y: int, y-coordinate of cursor
    """
    for b in balls:
        if ((pos_x - b[0][0]) ** 2 + (pos_y - b[0][1]) ** 2) <= b[1] ** 2:
            balls.remove(b)
            return 1
    return 0


init_game()
pygame.quit()
