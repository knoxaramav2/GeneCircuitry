import pygame
from dims import Point, centerDim

class Camera:

    pos     :       Point
    dim     :       Point
    screen  :       pygame.Surface

    def render(self):
        pygame.display.flip()

    def draw(self):
        pygame.draw.circle(self.screen, (0, 255, 255), centerDim(self.dim), 50)

    def clear(self):
        self.screen.fill((0,0,0))

    def setPos(self, xpos:int, ypos:int):
        self.pos = Point(xpos, ypos)

    def setScale(self, xscale:int, yscale:int):
        self.dim = Point(xscale, yscale)
        self.screen = pygame.display.set_mode(self.dim)

    def __init__(self, width:int=720, height:int=480, xpos:int=0, ypos:int=0):
        self.setPos(xpos, ypos)
        self.setScale(width, height)
        
__cam_inst__:   Camera = None

def getCamera():
    global __cam_inst__
    if __cam_inst__ == None:
        __cam_inst__ = Camera()
    return __cam_inst__
    
