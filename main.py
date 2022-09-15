from action import Action
from board import BoardManager
from action import Action
import textwrap

#8x8
data = textwrap.dedent("""
########
#  •   #
#  □   #
#      #
#  a   #
#      #
#      #
########
""")

sokoban = BoardManager(data)
act = Action(sokoban)
print(sokoban)
act.up()

print(sokoban)