from pygame import *
from ball import*
game = True

W = 1366
H = 768
H_W = H/2

win = display.set_mode((W,H),FULLSCREEN)

class Main(sprite.Sprite):
    def __init__(self,x,y,pic,W,H,speed,face,face1):
        super().__init__()
        self.pic = image.load(pic)
        self.pic = transform.scale(self.pic,(W,H))
        self.rect = Rect(x,y,W,H)
        self.face = face
        self.face1 = face1
        self.speed = speed

    def reset(self):
        win.blit(self.pic,(self.rect.x,self.rect.y))

class BALL(Main):
    
    def ch_s(self):
        self.speed += 1

    def update(self):
        if self.face == 'right':
            self.rect.x +=5
            if self.rect.x>=W:
                self.face = 'left'                
        if self.face == 'left':
            self.rect.x-=5
            if self.rect.x< 0:
                self.face = 'right'

        if self.face1 == 'up':
            self.rect.y+=3
            if self.rect.y>=H:
                self.face1 = 'dawn'
        if self.face1 == 'dawn':
            self.rect.y-=3
            if self.rect.y < 0:
                self.face1 = 'up'
        self.reset()
        

class Hero(Main):
    def update(self):
        
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -=  self.speed
        if keys[K_s]:
            self.rect.y +=  self.speed


        if self.rect.y<0:
            self.rect.y+=5
        if self.rect.y>H-30:
            self.rect.y -= 5
        self.reset()
        
        if sprite.collide_rect(self,Ball):
            if Ball.face == 'right':
                Ball.rect.x +=10
                if Ball.rect.x>=W:
                    Ball.face = 'left'                
            if Ball.face == 'left':
                Ball.rect.x-=10
                if Ball.rect.x< 0:
                    Ball.face = 'right'

            if Ball.face1 == 'up':
                Ball.rect.y+=3
                if Ball.rect.y>=H:
                    Ball.face1 = 'dawn'
            if Ball.face1 == 'dawn':
                Ball.rect.y-=3
                if Ball.rect.y < 0:
                    Ball.face1 = 'up'
    def shoot(self):
        global F,ef,o1
        p = Pulya(self.rect.x,self.rect.y,'bullet.png','up','1')
        pulys.add(p)
        
Ball = BALL(300,300,'ball.png',20,20,20,'left','up')
Racket = Hero(0,H_W,"racket.png",25,100,5,'left','up')


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
    Ball.update()
    Racket.update()










    display.update()
