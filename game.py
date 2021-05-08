from pygame import *
game = True

W = 1366
H = 768
win = display.set_mode((W,H),FULLSCREEN)

class Main(sprite.Sprite):
    def __init__(self,x,y,pic,W,H,speed):
        super().__init__()
        self.pic = image.load(pic)
        self.rect = Rect(x,y,W,H)
    def reset(self):
        win.blit(self.pic,(self.rect.x,self.rect.y))

ball = Main(300,300,'ball.png',40,40,50)

def control():
    global game
    for e in event.get():
        if e.type == 2:
            if e.key == K_ESCAPE:
                game = False
        if e.type == 12:
            game = False



while game:
    control()
    win.fill((255,255,255))
    ball.reset()











    display.update()
