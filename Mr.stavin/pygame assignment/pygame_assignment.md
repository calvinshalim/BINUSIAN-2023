# Pygame for Mr. Stavin

1.Pygame is one of pyhthon modules designed for writing video games and can be with the pyhton programming language. yes you can modify it.

2.Rectangle is a background in pygame windows that is a shape of rectangle and it is the bounding box of an object.
```
    import pygame, sys
    from pygame.locals import
    def main():
        pygame.init()
    
        DISPLAY=pygame.display.set_mode((500,400),0,32)
        WHITE=(255,255,255)
        BLUE=(0,0,255)
    
        DISPLAY.fill(WHITE)
    
        pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))
    
        while True:
            for event in pygame.event.get():
                 if event.type==QUIT:
                     pygame.quit()
                     sys.exit()
            pygame.display.update()
main()
```

3.Yes you can. This is how you play a music in pygame.
```
   pygame.init()
   pygame.mixer.music.load('music.wav')
   pygame.mixer.music.play(-1) #(-1) if you want to play it continuously
```
4.This is how you set a timer in pygame
```
    pygame.init()
    start_ticks=pygame.time.get_ticks()
    while mainloop:
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if seconds>10:
        break
    print (seconds)
```

5.Sprites is a two dimensional image that is part of the larger graphical scene which is usually an object in the scene.
   Groups are used to store sprites.
   You used this when you want to add something like an enemy or anoter object that u want to interact with.
```
pygame init()
class Bullet(Sprite):
     def __init__(self,ai_settings,screen,ship):
         super(Bullet,self).__init__()
         self.screen = screen
         
         self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                                 ai_settings.bullet_height)
         self.rect.centerx = ship.rect.centerx
         self.rect.top = ship.rect.top
         self.y = float(self.rect.y)
         
         self.color = ai_settings.bullet_color
         self.speed_factor = ai_settings.bullet_speed_factor
         
     def update(self):
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y
        
     def draw_bullet(self):
         pygame.draw.rect(self.screen, self.color, self.rect)
```         

6.Collision detection is when two or more objects in the screen touched with each other.
   It is important because it can help determine whether two rectangles are overlapping each other or not. 
```
    function collisionDetection() {
    for(var c=0; c<brickColumnCount; c++) {
        for(var r=0; r<brickRowCount; r++) {
            var b = bricks[c][r];
            // calculations
        }
    }
}
```

7.Use pygame.image.load() to load.
   Blit is a function to draw one image onto another or copy data image to surface and we call it blitting.
```
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)
```

8.Use for loop to update and draw them all at almost the same time.
```
    pygame.init()
    screen = pygame.display.set_mode(1200,800)
    image = pygame.image.load("image.jpg")
    for sprite in sprites_lists:
    sprite.update()
    screen.blit(sprite.image,sprite.image.get_rect())
```
10.Game physics is a introduction of the laws of physics into a game, particularly in 3D computer graphics. It is important because it makes the effects in the game appear more realistic to the user. 

11.This is how you display a text in pygame.
```
   import pygame
   pygame.init()
   X = 400 
   Y = 400
   display_surface = pygame.display.set_mode((X, Y ))
   font = pygame.font.SysFont("arial", 34)
   text = font.render("Calvin", True, (0,255,0),(0,0,128)) 
   textRect = text.get_rect()  
   textRect.center = (X // 2, Y // 2) 
```

12.This is how you move a sprite or image in pygame.
```
    class Bird(object):
        def __init__(self):
            self.image = pygame.image.load(img_path)
            self.x = 0
            self.y = 0
    
        def handle_keys(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                self.y += 1
            elif key[pygame.K_UP]:
                self.y -= 1 
            if key[pygame.K_RIGHT]:
                self.x += 1
            elif key[pygame.K_LEFT]:
                self.x -= 1
    
        def blitme(self, surface):
            surface.blit(self.image, (self.x, self.y))
    
    
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    
    bird = Bird()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
    
        bird.handle_keys()
        
        screen.fill((255,255,255))
        bird.blitme(screen)
        pygame.display.update() 

```
13.This is how you fill a background color of a surface. i am changing the background to blue
```
    import pygame
    from pygame.locals import *
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,255))
        pygame.display.update()
```
14.This is how to randomize your sprite.
```
    import random
    def move(self):
        self.rect.move_ip(random.randint(0, 999), random.randint(0, 999))
```

15.Y, I redownloaded it twice just to make sure I do not have the wrong .txt file lol