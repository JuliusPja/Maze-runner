from abc import ABC, abstractmethod

class GameEntity(ABC):
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    @abstractmethod
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Player(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 'P')
        self.dx = 0
        self.dy = 0

    def move(self, dx, dy):  
        self.x += dx
        self.y += dy    

class Wall(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, '#')


class Exit(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 'E')

