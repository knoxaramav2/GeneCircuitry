from abc import ABC, abstractmethod

from globalState import getGlobalState, GlobalState
from camera import getCamera, Camera
from events import getEvents, Events

class Scene(ABC):
    _name   : str
    _running: bool
    _state  : GlobalState
    _camera : Camera
    _events : Events

    def __init__(self, name:str):
        self._name = name
        self._running = False
        self._state = getGlobalState()
        self._camera = getCamera()
        self._events = getEvents()
        self._events.clear()

    def _loop(self):
        while self._running:
            self.preUpdate()
            self.update()
            self.postUpdate()
            self.preRender()
            self.render()
            self.postRender()

    def start(self):
        self._running = True
        self._loop()

    def stop(self):
        self._running = False

    #@abstractmethod
    def preUpdate(self): pass
    
    #@abstractmethod
    def postUpdate(self): pass

    @abstractmethod
    def update(self): pass

    #@abstractmethod
    def preRender(self):
        self._camera.clear()
        self._camera.draw()

    #@abstractmethod
    def postRender(self): pass

    #@abstractmethod
    def render(self):
        self._camera.render()
    