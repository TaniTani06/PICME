#import math
from mpmath import *
import pygame
from pygame import mixer
pygame.init()

width = 1280
height = 720

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50,50,50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
yellow = (255, 255, 0)


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Bagadugunbaradugunbau')
label_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 24)


play3 = False
tocar = [0, 0, 0, 0] #lista para computar qual padrão de toques será usado
falso = [0, 0, 0, 0] #lista para comparar com o tocar sendo todo igual a 0
fps = 64
timer = pygame.time.Clock()
beats = 16
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)]for _ in  range(instruments)]
active_list = [1 for _ in range(instruments)]
bpm = 768
playing = True
active_length = 0
active_beat = 1
beat_changed = True

#load in sounds
agogo = mixer.Sound('sounds\AGOGO6.wav')
le = mixer.Sound('sounds\le4.wav')
rumpi = mixer.Sound('sounds\\rumpi.wav')
rum = mixer.Sound('sounds\\rum.wav')
rum_pau = mixer.Sound('sounds\RumOpenPau4.wav')
tom = mixer.Sound('sounds\\tom.wav')
pygame.mixer.set_num_channels(instruments*3)

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                agogo.play()
            if i == 1:
                le.play()
            if i == 2:
                rumpi.play()
            if i == 3:
                rum.play()

def draw_grid(clicks, beat, actives):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 220, height - 238], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, height - 242, width, 240], 5)
    boxes = []
    colors = [gray, white, gray]

    agogo_text = label_font.render('Gã', True, colors[actives[0]])
    screen.blit(agogo_text, (25,30))

    le_text = label_font.render('Lé', True, colors[actives[1]])
    screen.blit(le_text, (25,105))

    rumpi_text = label_font.render('Rumpi', True, colors[actives[2]])
    screen.blit(rumpi_text, (25,185))

    rum_text = label_font.render('Rum', True, colors[actives[3]])
    screen.blit(rum_text, (25,265))
    '''
    clap_text = label_font.render('Clap', True, colors[actives[4]])
    screen.blit(clap_text, (25,345))

    floor_text = label_font.render('Floor Tom', True, colors[actives[5]])
    screen.blit(floor_text, (30,425))
    '''
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i*80) + 80), (218, (i*80) + 80), 5)
    

    for i in range(beats):
        for j in range(instruments):
            if clicked[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = dark_gray
            rect = pygame.draw.rect(screen, color, [i*((width-217)//beats) + 220, (j*80) + 5,
                ((width-217)//beats) - 3, ((height-240)//instruments) - 10], 0, 3)

            pygame.draw.rect(screen, gold, [i*((width-217)//beats) + 220, (j*80),
                ((width-217)//beats), ((height-240)//instruments)], 5, 5)
            
            pygame.draw.rect(screen, black, [i*((width-217)//beats) + 220, (j*80),
                ((width-217)//beats), ((height-240)//instruments)], 2, 5)
            boxes.append((rect, (i, j)))


    active = pygame.draw.rect(screen, blue, [beat*((width-217)//beats) + 220, 0, (width-217)//beats, instruments*80], 5, 3)

    return boxes



'''
#usando fibonacci como f(x)
def next_seq(seq):
    new_seq = ''
    for i in range(len(seq)):
        if seq[i] == 'L':
            new_seq = new_seq + 'LS'
        if seq[i] == 'S':
            new_seq = new_seq + 'L'
    seq = new_seq
    return seq
  

def f(x):
    seq = 'L'
    while x>len(seq):
        seq = next_seq(seq)
    
    #print (seq)
    return (seq[x-1])
'''

'''
def f(x):
    mp.dps = x
    a = int(x*((mpf(2)**mpf(0.5))/mpf(4.5)))
    b = int((x-1)*((mpf(2)**mpf(0.5))/mpf(4.5)))

    return a-b
'''

def f(x):
    mp.dps = x
    a = int(x*((mpf(2)**mpf(0.5))/mpf(4.5)))
    b = int((x-1)*((mpf(2)**mpf(0.5))/mpf(4.5)))

    return a-b

def g(x):
    mp.dps = x
    a = int(x*((mpf(2)**mpf(0.5))/mpf(3.5)))
    b = int((x-1)*((mpf(2)**mpf(0.5))/mpf(3.5)))

    return a-b

x = 0

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_list)
    
    #Lower menu
    play_pause = pygame.draw.rect(screen, gray, [50, height - 170, 220, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, height - 150))
    if playing:
        play_text2 = medium_font.render('Playing', True, dark_gray)
    else:
        play_text2 = medium_font.render('Paused', True, dark_gray)
    screen.blit(play_text2, (70, height - 120))



    #instruments rects
    instrument_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i*80), (220,80))
        instrument_rects.append(rect)

    if beat_changed:
        play_notes()
        beat_changed = False

    #x aumenta 6 a cada quadrinho

    #96 -> 1x /loop (16 retângulos), 24 -> 4x /loop, 12 -> 8x /loop, 6 -> 16x /loop (em todo retângulo)
    #if (x%6 == 0):
    
    if tocar[0] != 0 and x%6 == 0:
        if active_list[3] == 1:
            tocar[0] += 1
    if tocar[0] > 2:                #intervalo mínimo entre dois "toques" consecutivos
                tocar[0] = 0

    #Se nenhum toque estiver selecionado, em todo quadrinho se roda a função para escolher um dos toques
    if (tocar == falso) and x%6 == 0:
        if (f(x/6) == 1 and g(x/6) == 1):
            tocar[0] = 1
        elif (f(x/6) == 1 and g(x/6) == 0):
            tocar[1] = 1
        elif (f(x/6) == 0 and g(x/6) == 1):
            tocar[2] = 1
        else:
            tocar[3] = 1
        
    #print(tocar)

    #                    chamado de quatro
    if tocar[1] != 0:
        if active_list[3] == 1:
            if tocar[1] == 1 and x%48 == 0:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[1] += 1
            if tocar[1] == 2 and x%48 == 12:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[1] += 1
            if tocar[1] == 3 and x%48 == 0:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[1] += 1
            if tocar[1] == 4 and x%48 == 24:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[1] += 1
    if tocar[1] > 4:
                tocar[1] = 0
                tocar[0] = 1

    if tocar[3] != 0:
        if active_list[3] == 1:
            if tocar[3] == 1 and x%48 == 0:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[3] += 1
            if tocar[3] == 2 and x%48 == 12:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[3] += 1
            if tocar[3] == 3 and x%48 == 36:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[3] += 1
            if tocar[3] == 4 and x%48 == 0:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[3] += 1
            if tocar[3] == 5 and x%48 == 24:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[3] += 1
            if tocar[3] == 6 and x%48 == 36:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[3] += 1
            if tocar[3] == 7 and x%48 == 12:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum.play()
                tocar[3] += 1
            if tocar[3] == 8 and x%48 == 36:
                pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
                rum_pau.play()
                tocar[3] += 1
    if tocar[3] > 8:
                tocar[3] = 0
                tocar[0] = 1

    if tocar[2] != 0 and x%6 == 0:
        if active_list[3] == 1:
            #pygame.draw.rect(screen, yellow, [0, 240, 218, 80], 0, 5)
            #rum.play()
            tocar[2] += 1
    if tocar[2] > 4:
                tocar[2] = 0
                tocar[0] = 1
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1

    beat_length = fps*60 // bpm     #fps*60 //bpm
    
    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True
        x += 1
        
    pygame.display.flip()
pygame.quit()