import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((798, 1188))
x = 42
y = 44
rect(screen, (35, 35, 35), (0, 11.2*y, 19*x, 15.8*y))
rect(screen, (140, 140, 140), (0, 0, 19*x, 11.2*y))
ellipse(screen, (70, 70, 70), (9.6*x, 5.92*y, (20.8-9.6)*x, (7.67-5.92)*y))
rect(screen, (83, 71, 24), (0.9*x, 5.6*y, 10*x, 14*y))
rect(screen, (115, 63, 44), (2*x, 15.6*y, 1.9*x, 2.4*y))
rect(screen, (115, 63, 44), (4.95*x, 15.6*y, 1.9*x, 2.4*y))
rect(screen, (255, 200, 8), (7.85*x, 15.6*y, 1.9*x, 2.4*y))
t = 0
l = 2.25*x
while t <= 3:
    rect(screen, (110, 97, 81), (1.95*x+l*t, 5.6*y, 1.2*x, 5.5*y))
    t += 1
rect(screen, (60, 60, 60), (6.85*x, 3*y, 0.3*x, 2*y))
polygon(screen, (30, 30, 30), [(0, 5.8*y), (1.45*x, 4.8*y), (10.15*x, 4.8*y), (11.6*x, 5.8*y)])
rect(screen, (60, 60, 60), (2.38*x, 3.58*y, 0.35*x, (5.41-3.58)*y))
ellipse(screen, (90, 90, 90), (0.9*x, 2.52*y, (15.8-0.9)*x, (4.33-2.52)*y))
rect(screen, (60, 60, 60), (2.93*x, 2.44*y, (3.62-2.93)*x, (5.51-2.44)*y))
rect(screen, (60, 60, 60), (9.36*x, 3.5*y, (9.71-9.36)*x, (5.51-3.5)*y))
circle(screen, (255, 255, 255), (725, 95), 71)
ellipse(screen, (115, 115, 115), (8.3*x, 1.71*y, (19.15-8.3)*x, (3.48-1.71)*y))
ellipse(screen, (115, 115, 115), (11.3*x, 3.84*y, (19-11.3)*2*x, (5.51-3.84)*y))

b = (0.4*2+1.05)*x
while t <= 9:
    rect(screen, (75, 75, 75), (0.24*x+b*(t-4), 10.07*y, 0.4*x, 1.3*y))
    rect(screen, (75, 75, 75), (1.79*x+b*(t-4), 10.07*y, 0.4*x, 1.3*y))
    t += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()