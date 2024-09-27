from pygame import *
import pygame
import sys
from random import randint
init()

class GameSprite(sprite.Sprite):
    def __init__(self, w, h, picture, x, y):
        super().__init__()
        self.image = image.load(picture)
        self.image = transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Miska(GameSprite):
    def __init__(self, w, h, picture, x, y, speed):
        super().__init__(w, h, picture, x, y)
        self.speed = speed
    def update(self):
        keys = key.get_pressed()
        if keys[K_d]:
            self.rect.x = self.rect.x + self.speed
        if keys[K_a]:
            self.rect.x = self.rect.x - self.speed

class Area():
    def __init__(self, x, y, width, height, color, colorframe):
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = pygame.Rect(x-6, y-6, width, height)
        self.color = color
        self.color_frame = colorframe
    def draw_rect(self, window):
        pygame.draw.rect(window, self.color_frame, self.frame)
        pygame.draw.rect(window, self.color, self.rect)

class Label(Area):
    def create_text(self, text, size):
        font = pygame.font.Font(None, size)
        self.first = font.render(text, True, (62, 100, 100))
    def writing_text(self, y):
        window.blit(self.first, (self.rect.x+10, y))

class Apple(GameSprite):
    def __init__(self, w, h, picture, x, y, speed):
        super().__init__(w, h, picture, x, y)
        self.speed = speed
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 720:
            self.kill()
            apples.add(Apple(100, 100, 'apple.png', randint(200, 1080), -200, 5))
            misochka.score = 0
            scores1.create_text(str(misochka.score), 50)
        if sprite.collide_rect(self, misochka):
            self.kill()
            apples.add(Apple(100, 100, 'apple.png', randint(200, 1080), -200, 5))
            misochka.score += 1
            scores1.create_text(str(misochka.score), 50)
            print('Кол-во собранных яблок:', misochka.score)

w = 1280
h = 720
window = display.set_mode((w, h))
images = image.load('i.png') #загрузка картинки
images = transform.scale(images, (w, h)) #изменение размеров картинки
spritik = GameSprite(randint(200, 1500), 500, 'heh.jpg', 100, 10) #создаётся обьект GameSprite
misochka = Miska(250, 125, 'i1.png', 360, 600, 20)
misochka.score = 0
scores = Label(1050, 100, 0, 0, (68, 249, 225), (68, 249, 225))
scores1 = Label(1050, 1000, 0, 0, (68, 249, 225), (68, 249, 225))
scores.create_text('Очки:', 50)
scores1.create_text(str(misochka.score), 50)
apple2 = Apple(100, 100, 'apple.png', randint(200, 1080), -900, 5) #создаётся обьект класса Apple
apple3 = Apple(100, 100, 'apple.png', randint(200, 1080), -700, 5) #создаётся обьект класса Apple
apple4 = Apple(100, 100, 'apple.png', randint(200, 1080), -500, 5) #создаётся обьект класса Apple
apple5 = Apple(100, 100, 'apple.png', randint(200, 1080), -300, 5) #создаётся обьект класса Apple
apple6 = Apple(100, 100, 'apple.png', randint(200, 1080), -100, 5) #создаётся обьект класса Apple
apples = sprite.Group(apple2, apple3, apple4, apple5, apple6) #создаётся группа с яблоками
while True: #цикл бесконечный
    for e in event.get(): #цикл который перебирает все события
        if e.type == QUIT: #если тип события = закрытия игры
            sys.exit()
    window.blit(images, (0, 0)) #отображает задние фон
    spritik.reset() #отображает обьект spritik
    misochka.reset() #отображает обьект миски
    misochka.update() #делает так чтобы миска двигался в лево и право
    apples.draw(window) #отображает яблоки
    apples.update() #делает так чтобы яблоки двигались внизззззззззззззззззззззззззззз
    scores.writing_text(50)
    scores.draw_rect(window)
    scores1.writing_text(100)
    scores1.draw_rect(window)
    display.update() #обновляет экранчик