import pygame
from pygame import mixer
pygame.init()

width = 1280
height = 720

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Bagadugunbaradugunbau')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 220, height - 238], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, height - 242, width, 240], 5)
    boxes = []
    colors = [gray, white, gray]

    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (25,30))

    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (25,105))

    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (25,185))

    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (25,265))

    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (25,345))

    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (30,425))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i*80) + 80), (218, (i*80) + 80), 5)


    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [i*((width-217)//beats) + 220, (j*80),
            ((width-217)//beats), ((height-240)//instruments)], 5, 5)


    

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    pygame.display.flip()
pygame.quit()