from pygame import *
game = True

W = 1366
H = 768
win = display.set_mode((W,H),FULLSCREEN)



def control():
    global game
    for e in event.get():
        if e.type == 2:
            if e.key == K_ESCAPE:
                game = False

while game:
    control()
    win.fill((255,255,255))












    display.update()