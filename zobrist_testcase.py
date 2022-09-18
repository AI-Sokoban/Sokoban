from board import BoardManager
import action

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

# Test case

sokoban.push(action.Up)
print(sokoban)

sokoban2 = BoardManager(data[level])
sokoban2.push(action.Up)

visitedState = set()
visitedState.add(sokoban)



t1 = sokoban in visitedState
t2 = sokoban2 in visitedState
print(t1)
print(t2)