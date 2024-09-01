

class GlobalState:
    __running:      bool
    
    def __init__(self):
        self.__running = True

    def running(self): return self.__running
    def exit(self): self.__running = False

__gs_inst__ : GlobalState = None
def getGlobalState():
    global __gs_inst__
    if __gs_inst__ == None:
        __gs_inst__ = GlobalState()
    return __gs_inst__