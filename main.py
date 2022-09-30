import action
from board import BoardManager
import pygame
import random

from render import Renderer
from map import maps

# a = player
# @ = player ที่ทับบน goal
# □ = block ที่ไม่อยู่ตรง goal
# ■ = block ที่อยู่ตรง goal
# . = goal

level = 0
sokoban = BoardManager(maps[level])

renderer = Renderer(sokoban).setCaption("Sokoban")

renderer.render()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        validActions = sokoban.getValidActions()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and action.Left in validActions:
                sokoban.push(action.Left)
            if event.key == pygame.K_d and action.Right in validActions:
                sokoban.push(action.Right)
            if event.key == pygame.K_w and action.Up in validActions:
                sokoban.push(action.Up)
            if event.key == pygame.K_s and action.Down in validActions:
                sokoban.push(action.Down)
            if sokoban.isGameOver():
                level += 1
                level = level % len(maps)
                print("You win!")
                font = pygame.font.Font("freesansbold.ttf", 32)
                text = font.render("You win!", True, (255, 255, 255), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (300, 200)
                renderer.screen.blit(text, textRect)
                renderer.render()
                pygame.time.wait(3000)
                # clear screen
                renderer.clear()
                sokoban.genNewBoard(maps[level])

            renderer.render()
            print(sokoban)
