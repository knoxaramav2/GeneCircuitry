import pygame

class Events:

    __eventBuffer : list[pygame.event.Event]

    def __init__(self):
        pygame.init()
        self.__eventBuffer = []

    def clear(self): 
        
        pygame.event.clear()
    def next(self) -> pygame.event.Event:
        self.__eventBuffer.extend(pygame.event.get())
        if len(self.__eventBuffer) == 0:
            return None
        ret = self.__eventBuffer[0]
        self.__eventBuffer = self.__eventBuffer[1:]

__evnt_inst__ : Events = None
def getEvents():
    global __evnt_inst__
    if __evnt_inst__ == None:
        __evnt_inst__ = Events()
    return __evnt_inst__