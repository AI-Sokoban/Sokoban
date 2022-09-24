from board import BoardManager
import action
import copy

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
""",
]

level = 0
sokoban = BoardManager(data[level])

# Test case

sokoban.push(action.Up)
print(sokoban)

sokoban2 = copy.deepcopy(sokoban)


visitedState = set()
visitedState.add(sokoban)


print("sokoban", hash(sokoban))
print("sokoban2", hash(sokoban2))
print("sokoban==sokoban2", sokoban == sokoban2)
print("sokoban2 in visitedState", sokoban2 in visitedState)
