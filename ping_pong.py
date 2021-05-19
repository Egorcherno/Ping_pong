from pygame import *
game = True


W = 1366
H = 768
H_W = H/2

font.init()
shift = font.SysFont('Arial',150)
lose = shift.render('You lose',False,(255,0,0))

fo = image.load("fon.jpg")
fo = transform.scale(fo,(W,H))


WIN = shift.render('You Win',False,(0,255,0))



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
        global gamemode
        if self.face == 'right':
            self.rect.x +=1
            if self.rect.x> W:
                gamemode = 'Lose'               
        if self.face == 'left':
            self.rect.x-=1
            if self.rect.x < 0:
                gamemode = 'Lose'

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
        if self.rect.y>H-40:
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


class Hero1(Main):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -=  self.speed
        if keys[K_DOWN]:
            self.rect.y +=  self.speed


        if self.rect.y<0:
            self.rect.y+=self.speed
        if self.rect.y>H-40:
            self.rect.y -= self.speed

        if sprite.collide_rect(self,Ball):
            if Ball.face == 'right':
                Ball.face = 'left'                
            elif Ball.face == 'left':
                Ball.face = 'right'

            if Ball.face1 == 'up':
                Ball.face1 = 'dawn'
            if Ball.face1 == 'dawn':
                Ball.face1 = 'up'

        self.reset()
        
#for one player
class BALL_for_one(Main):
    
    def ch_s(self):
        self.speed += 1

    def update(self):
        global gamemode
        if self.face == 'right':
            self.rect.x +=1
            if self.rect.x> W:
                self.face = 'left'
                self.speed +=2         
        if self.face == 'left':
            self.rect.x-=1
            if self.rect.x < 0:
                gamemode = 'Lose'

        if self.face1 == 'up':
            self.rect.y+=3
            if self.rect.y>=H:
                self.face1 = 'dawn'
        if self.face1 == 'dawn':
            self.rect.y-=3
            if self.rect.y < 0:
                self.face1 = 'up'
        
        self.reset()
        
class Hero_for_one(Main):
    def update(self):
        
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -=  self.speed
        if keys[K_s]:
            self.rect.y +=  self.speed


        if self.rect.y<0:
            self.rect.y+=5
        if self.rect.y>H-40:
            self.rect.y -= 5
        self.reset()
        
        if sprite.collide_rect(self,B_F_O):
            if B_F_O.face == 'right':
                B_F_O.rect.x +=10
                if B_F_O.rect.x>=W:
                    B_F_O.face = 'left'                
            if B_F_O.face == 'left':
                B_F_O.rect.x-=10
                if B_F_O.rect.x< 0:
                    B_F_O.face = 'right'

            if B_F_O.face1 == 'up':
                B_F_O.rect.y+=3
                if B_F_O.rect.y>=H:
                    B_F_O.face1 = 'dawn'
            if B_F_O.face1 == 'dawn':
                B_F_O.rect.y-=3
                if B_F_O.rect.y < 0:
                    B_F_O.face1 = 'up'
    def shoot(self):
        global F,ef,o1
        p = Pulya(self.rect.x,self.rect.y,'bullet.png','up','1')
        pulys.add(p)         



Ball = BALL(300,H_W,'ball.png',20,20,20,'left','up')
Racket = Hero(0,H_W,"racket.png",25,100,5,'left','up')
Racket2 = Hero1(W-25,H_W,"racket2.png",25,100,5,'left','up')

B_F_O = BALL_for_one(300,H_W,'ball.png',20,20,20,'left','up')
R_F_O = Hero_for_one(0,H_W,"racket.png",25,100,5,'left','up')

def control():
    global game,gamemode
    for e in event.get():
        if e.type == 2:
            if e.key == K_ESCAPE:
                game = False
        if e.type == 12:
            game = False
        if e.type == KEYUP:
            if e.key == K_SPACE:
                gamemode = 'Play_one'
                B_F_O.rect.x = 300
                B_F_O.rect.y = H_W
            if e.key == K_KP_ENTER:
                gamemode = 'Start'
                Ball.rect.x = 300
                Ball.rect.y = H_W
                print(e)



gamemode = 'START'

while game:
    control()
    win.fill((255,255,255))
    if gamemode == 'START':
        win.blit(fo,(0,0))
    if gamemode == 'Start':
        
        Ball.update()
        Racket.update()
        Racket2.update()  

    if gamemode == 'Play_one':
        R_F_O.update()
        B_F_O.update()


    if gamemode == 'Lose':
        win.blit(lose,(150,501))

    
    display.update()
