from pygame import*
from game import *
print('hello')

class Main(sprite.Sprite):
    def __init__(self,x,y,pic,W,H,speed,face):
        super().__init__()
        self.pic = image.load(pic)
        self.pic = transform.scale(self.pic,(W,H))
        self.rect = Rect(x,y,W,H)
    def reset(self):
        win.blit(self.pic,(self.rect.x,self.rect.y))

class Ball(Main):
    def update():
        if self.face == 'right':
            self.rect.x +=10
            if self.rect.x>=W:
                self.face = 'left'
        if self.face == 'left':
            self.rect.x-=10
            if self.rect.x< 0:
                self.face = 'right'

        if self.face == 'up':
            self.rect.y+=10
            if self.rect.y>=H:
                self.face = 'dawn'
        if self.face == 'dawn':
            self.rect.y-=10
            if self.rect.y < 0:
                self.face = 'up'

        self.reset()