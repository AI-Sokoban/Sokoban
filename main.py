import action
from board import BoardManager
import pygame
import random

from render import Renderer
# a = player
# @ = player ที่ทับบน goal
# □ = block ที่ไม่อยู่ตรง goal
# ■ = block ที่อยู่ตรง goal
# . = goal

# 8x8
data = [
    """
########
#      #
##a   ##
##.□■  #
##  #  #
#      #
#      #
########
""",
    """
########
#      #
##  a ##
##.□□  #
##  #  #
#      #
#   .  #
########
""",
    """
##########
#        #
##  a   ##
##.  □   #
##  #    #
#    □   #
#   .    #
##########
"""
]

level = 0
sokoban = BoardManager(data[level])

renderer = Renderer(sokoban).setCaption("Sokoban")

renderer.render()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        validActions = sokoban.getValidActions()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and action.Left in validActions:
                sokoban.push(action.Left)
            if event.key == pygame.K_RIGHT and action.Right in validActions:
                sokoban.push(action.Right)
            if event.key == pygame.K_UP and action.Up in validActions:
                sokoban.push(action.Up)
            if event.key == pygame.K_DOWN and action.Down in validActions:
                sokoban.push(action.Down)
            if sokoban.isGameOver():
                level += 1
                level = level % len(data)
                print("You win!")
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(
                    'You win!', True, (255, 255, 255), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (300, 200)
                renderer.screen.blit(text, textRect)
                renderer.render()
                pygame.time.wait(3000)
                # clear screen
                renderer.clear()
                sokoban.genNewBoard(data[level])
                
            renderer.render()
            print(sokoban)

