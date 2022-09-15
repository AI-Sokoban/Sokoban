from turtle import down
from action import Action
from board import BoardManager
from action import Action
import textwrap
import os

# a = player
# @ = player ที่ทับบน goal
# □ = block ที่ไม่อยู่ตรง goal
# ■ = block ที่อยู่ตรง goal
# . = goal

#8x8
data = ("""
########
#      #
##a   ##
##.□■  #
##  #  #
#      #
#      #
########
""")

sokoban = BoardManager(data)
act = Action(sokoban)



while True:
    print(sokoban)
    inp = input()
    
    if inp == "w":
        act.up()
    
    if inp == "s":
        act.down()

    if inp == "a":
        act.left()

    if inp == "d":
        act.right()

    if inp == "x":
        break
    os.system('cls')

    #act