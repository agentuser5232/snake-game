import pygame
import random
import sys
import json
from pathlib import Path

pygame.init()

WIDTH, HEIGHT = 640, 480
CELL = 20
FPS = 10

BLACK=(25,25,25)
GREEN=(0,200,0)
DARK=(0,120,0)
RED=(220,60,60)
WHITE=(240,240,240)
YELLOW=(240,210,70)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30)
big=pygame.font.SysFont(None,52)

SCORE_FILE=Path("highscore.json")
def load_high():
    if SCORE_FILE.exists():
        try:
            return json.loads(SCORE_FILE.read_text()).get("highscore",0)
        except:
            return 0
    return 0

def save_high(v):
    SCORE_FILE.write_text(json.dumps({"highscore":v}))

high=load_high()

def food_pos(snake):
    while True:
        p=(random.randrange(0,WIDTH,CELL),random.randrange(0,HEIGHT,CELL))
        if p not in snake:
            return p

def draw(txt,f,c,x,y):
    screen.blit(f.render(txt,True,c),(x,y))

def game():
    global high
    snake=[(WIDTH//2,HEIGHT//2)]
    dx,dy=CELL,0
    food=food_pos(snake)
    score=0
    paused=False

    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_p:
                    paused=not paused
                if paused: continue
                if e.key==pygame.K_UP and dy!=CELL: dx,dy=0,-CELL
                elif e.key==pygame.K_DOWN and dy!=-CELL: dx,dy=0,CELL
                elif e.key==pygame.K_LEFT and dx!=CELL: dx,dy=-CELL,0
                elif e.key==pygame.K_RIGHT and dx!=-CELL: dx,dy=CELL,0

        if paused:
            draw("PAUSED",big,YELLOW,240,210)
            pygame.display.flip()
            clock.tick(10)
            continue

        head=(snake[0][0]+dx,snake[0][1]+dy)
        if head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT or head in snake:
            if score>high:
                high=score
                save_high(high)
            return

        snake.insert(0,head)
        if head==food:
            score+=1
            if score%5==0:
                global FPS
                FPS=min(FPS+1,20)
            food=food_pos(snake)
        else:
            snake.pop()

        screen.fill(BLACK)
        for x in range(0,WIDTH,CELL):
            pygame.draw.line(screen,(40,40,40),(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,CELL):
            pygame.draw.line(screen,(40,40,40),(0,y),(WIDTH,y))

        pygame.draw.rect(screen,RED,(*food,CELL,CELL))
        for i,s in enumerate(snake):
            pygame.draw.rect(screen,GREEN if i==0 else DARK,(*s,CELL,CELL))

        draw(f"Score: {score}",font,WHITE,10,10)
        draw(f"High: {high}",font,WHITE,500,10)
        draw("P: Pause",font,WHITE,10,40)
        pygame.display.flip()
        clock.tick(FPS)

while True:
    FPS=10
    screen.fill(BLACK)
    draw("SNAKE GAME",big,GREEN,180,120)
    draw("Press SPACE to Start",font,WHITE,205,210)
    draw("Arrow Keys to Move",font,WHITE,210,250)
    draw("Q to Quit",font,WHITE,260,290)
    pygame.display.flip()

    waiting=True
    while waiting:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_SPACE:
                    waiting=False
                elif e.key==pygame.K_q:
                    pygame.quit();sys.exit()

    game()

    while True:
        screen.fill(BLACK)
        draw("GAME OVER",big,RED,190,140)
        draw(f"High Score: {high}",font,WHITE,235,210)
        draw("R: Restart   Q: Quit",font,WHITE,200,260)
        pygame.display.flip()
        restart=False
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit();sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_r:
                    restart=True
                elif e.key==pygame.K_q:
                    pygame.quit();sys.exit()
        if restart:
            break
        clock.tick(15)
