import pygame
from board import BoardManager
from tile import *

wall = pygame.image.load('assets/images/wall.png')
box = pygame.image.load('assets/images/box.png')
box_on_target = pygame.image.load('assets/images/box_on_target.png')
player = pygame.image.load('assets/images/player.png')
space = pygame.image.load('assets/images/space.png')
target = pygame.image.load('assets/images/target.png')


DEFAULT_RENDER_MAP = {
    WALL: wall, 
    EMPTY: space, 
    BOX: box,
    GOAL: target, 
    PLAYER: player, 
    BOX_ON_GOAL: box_on_target, 
    PLAYER_ON_GOAL: player
}

DEFAULT_BOX_SIZE = wall.get_width()
DEFAULT_SCREEN_SIZE = (600, 400)

class Renderer:
    def __init__(self, board: BoardManager):
        pygame.init()
        self.board = board
        self.renderMap = DEFAULT_RENDER_MAP
        self.renderBoxSize = DEFAULT_BOX_SIZE
        self.screen = None
        
        self.setDisplaySize(DEFAULT_SCREEN_SIZE)


    def setDisplaySize(self, size: tuple[int, int]):
        self.screen = pygame.display.set_mode(size)
        
        return self

    def setCaption(self, name: str):
        pygame.display.set_caption(name)

        return self

    def setRenderMap(self, renderMap: dict[str, pygame.Surface]):
        self.renderMap = renderMap

        return self

    def setRenderBoxSize(self, size):
        self.renderBoxSize = size

        return self

    def fromInstance(self, board: BoardManager):
        self.board = board

        return self

    def clear(self):
        self.screen.fill((0, 0, 0))

    def render(self):
        toRender = self.board.board_lst
        for i in range(len(toRender)):
            for c in range(len(toRender[i])):
                self.screen.blit(self.renderMap[toRender[i][c]], (c*self.renderBoxSize, i*self.renderBoxSize))

        pygame.display.update()
