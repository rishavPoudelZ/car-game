import pygame, sys, random
def audio(audio_path,loop) :
    # Starting the mixer
    pygame.mixer.init()
    # Loading the song
    pygame.mixer.music.load(audio_path)
    #Setting the volume
    pygame.mixer.music.set_volume(0.7)
    # Start playing the song
    pygame.mixer.music.play(loop,0.0,0)   


#class def    
class Player(pygame.sprite.Sprite):
    def __init__(self,picture_path,x,y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center=[x,y]

#Class def for falling objects
class obj(pygame.sprite.Sprite):
    def __init__(self,picture_path,axis_x,axis_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center=[axis_x,axis_y]
    def update(self,axis_x,axis_y):
       self.rect.center=[axis_x,axis_y]
                   
        
#declaring all varaibles
x=350
y=650
obj_x=random.randrange(150,550)
obj_x1=random.randrange(150,550)
obj_x2=random.randrange(150,550)
obj_x3=random.randrange(150,550)
obj_x4=random.randrange(150,550)
obj_y=-15
obj_y1=-350
obj_y2=-550
obj_y3=-90
obj_y4=-200
count=0
velocity=3.8
sound=True
with open('assests/Score.txt', 'r') as f:
    highScore = f.readline()
    f.close()
if highScore=="null":
    highScore==0
    


#General setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width=700
screen_height=700
screen=pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("assests/bg1.png")
portal=pygame.image.load("assests/portal.png")


#making a sprite
player1 = Player("assests/mainCar.png",x,y)
cone = obj("assests/cone.png", obj_x, obj_y)
people= obj("assests/people.png",obj_x1, obj_y1)
car2= obj("assests/car2.png",obj_x2, obj_y2)
car3= obj("assests/car4.png",obj_x3, obj_y3)
stop= obj("assests/stop.png",obj_x4, obj_y4)

#Grouping a sprite
player_group = pygame.sprite.Group()
player_group.add(player1)

#AddingToGroup
obj_group = pygame.sprite.Group()
obj_group.add(cone)
obj_group.add(people)
obj_group.add(car2)
obj_group.add(car3)
obj_group.add(stop)
audio("assests/GameSound.mp3",-1)


#Running Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #collision
    if pygame.sprite.spritecollideany(player1, obj_group):
        while sound==True:
            audio("assests/gameover.mp3",0)
            sound=False
            if sound==False:
                break

        #GameOverImage    
        lost = pygame.image.load("assests/lost.png")
        screen.blit(lost,(170,250))
        #RESTART prompt
        pygame.font.init() 
        restart_font = pygame.font.SysFont('Comic Sans MS', 30)
        restart_surface = restart_font.render('Press Space Bar To Restart', False, (0, 0, 0))
        screen.blit(restart_surface, (170,190))
        #HighScore
        pygame.font.init() 
        score_font= pygame.font.SysFont('Comic Sans MS', 30)
        highScore_font = score_font.render('HighScore :'+str(highScore), False, (0, 0, 0))
        screen.blit(highScore_font, (170,130))

        input = pygame.key.get_pressed()
        #Restart the game
        if input[pygame.K_SPACE]:
            audio("assests/GameSound.mp3",-1)
            if pygame.sprite.spritecollideany(player1, obj_group):
                velocity=3.5
                count=0
                x=350 
                y=650
                obj_x=random.randrange(150,550)
                obj_x1=random.randrange(150,550)
                obj_x2=random.randrange(150,550)
                obj_x3=random.randrange(150,550)
                obj_x4=random.randrange(150,550)
                obj_y=-15
                obj_y1=-350
                obj_y2=-550
                obj_y3=-90
                obj_y4=-200
                sound=True
                with open('assests/Score.txt', 'r') as f:
                    highScore = f.readline()
                    f.close()
    #If game just began then this will be run first
    else :       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
          y +=3
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
         y -=3
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
         x +=velocity
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
         x -=velocity               

   #Bound rules for sprite 
        if  x >= 550:
            x = 350
        elif x <= 150:
            x=350
        if y > 650:
            y = 650
        elif y < 50:
            y=50

   #making obj fall randomly and with increasing score the speed increases
        if count<25 :    
             obj_y  += 7
             obj_y1 += 7
             obj_y2 += 7
             obj_y3 += 7
             obj_y4 += 7
        elif count>24 and count<50 :  
             obj_y  += 8
             obj_y1 += 8
             obj_y2 += 8
             obj_y3 += 8
             obj_y4 += 8
        elif count>=50 and count<75 :
             obj_y  += 10
             obj_y1 += 10
             obj_y2 += 10
             obj_y3 += 10
             obj_y4 += 10
        elif count>=75 and count<100 :
             obj_y  += 11
             obj_y1 += 11
             obj_y2 += 11
             obj_y3 += 11
             obj_y4 += 11
        elif count>=100 :
             obj_y  += 13
             obj_y1 += 13
             obj_y2 += 13
             obj_y3 += 13
             obj_y4 += 13

    #resetting the object position
        if obj_y > 650  :
            
            count +=1
            obj_x=random.randrange(150,550)
            obj_y=-15

        if obj_y1 > 650  :
            
            count +=1
            obj_x1=random.randrange(150,550)
            obj_y1=random.randrange(-25,-15)

        if obj_y2 > 650 :
            
            count +=1
            obj_x2=random.randrange(150,550)
            obj_y2=random.randrange(-25,-15)

        if obj_y3 > 650  :
            
            count +=1
            obj_x3=random.randrange(150,550)
            obj_y3=random.randrange(-25,-15)

        if obj_y4 > 650  :
            
            count +=1
            obj_x4=random.randrange(150,550)
            obj_y4=random.randrange(-25,-15)

    #score
    pygame.font.init() 
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('Score :'+str(count), False, (0, 0, 0))
    score=count
    

    
    if count>int(highScore):
        with open('assests/Score.txt', 'w') as f:
            f.write('%d' % count)
            f.close()

            
        

    pygame.display.flip()
    screen.blit(background,(0,0))
    screen.blit(text_surface, (0,0))
    screen.blit(portal, (90,610))
    screen.blit(portal, (560,610))
    


    
    player_group.draw(screen)
    player_group.update()  
    obj_group.draw(screen)
    cone.update(obj_x, obj_y)
    people.update(obj_x1, obj_y1)
    car2.update(obj_x2, obj_y2)
    car3.update(obj_x3, obj_y3)
    stop.update(obj_x4, obj_y4)

    clock.tick(60)                                          
