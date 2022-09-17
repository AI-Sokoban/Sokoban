import action
from board import BoardManager
import pygame
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


def drawBoard():
    board = sokoban.getBoardList()
    for i in range(0, len(board)):
        for c in range(0, len(board[i])):
            screen.blit(images[board[i][c]], (c*box_size, i*box_size))
    pygame.display.update()


level = 0
sokoban = BoardManager(data[level])


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sokoban")
wall = pygame.image.load('assets/images/wall.png')
box = pygame.image.load('assets/images/box.png')
box_on_target = pygame.image.load('assets/images/box_on_target.png')
player = pygame.image.load('assets/images/player.png')
space = pygame.image.load('assets/images/space.png')
target = pygame.image.load('assets/images/target.png')

images = {'#': wall, ' ': space, '□': box,
          '.': target, 'a': player, '■': box_on_target, '@': player}
box_size = wall.get_width()

drawBoard()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
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
            drawBoard()
            if sokoban.isGameOver():
                level += 1
                level = level % len(data)
                print("You win!")
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(
                    'You win!', True, (255, 255, 255), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (300, 200)
                screen.blit(text, textRect)
                pygame.display.update()
                pygame.time.wait(3000)
                # clear screen
                screen.fill((0, 0, 0))
                sokoban.genNewBoard(data[level])
                drawBoard()
