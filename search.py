import time
from board import BoardManager

from collections import deque

# renderer
from render import Renderer
import msvcrt
import pygame

import time


############ test memory
import guppy
from guppy import hpy
import numpy as np


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
    """
########
###   ##
#.a□  ##
### □.##
#.##□ ##
# # . ##
#□ ■□□.#
#   .  #
########
"""
]

class ProblemState:
    def __init__(self, board: BoardManager, action: str = None, prevState = None):
        self.board = board
        self.action = action
        self.prevState = prevState

    def __hash__(self):
        return self.board.__hash__()

    def __eq__(self, other):
        return self.board.__eq__(other.board)

def solution(state: ProblemState):
    result = []
    while state.action:
        result.append(state.action)
        state = state.prevState

    return list(reversed(result))

def bfs(board: BoardManager,renderer : Renderer = None):
    initialState = ProblemState(board)
    queue = deque([initialState])

    if initialState.board.isGameOver():
        return solution(initialState)

    exploredSet = set()

    while len(queue) >0 :
        state = queue.popleft()
        exploredSet.add(state)

        for action in state.board.getValidActions():
            newBoard = state.board.push(action, True)

            #newBoard Renderer
            if renderer : 
                renderer.fromInstance(newBoard).render()
                # wait for input to change render
                # msvcrt.getch()
                # time delay for renderer only
                time.sleep(0.01)
                

            childState = ProblemState(newBoard,action,state)

            if(childState not in exploredSet) and (childState not in queue):
                if childState.board.isGameOver():
                    return solution(childState)
                queue.append(childState)

def dfs(board: BoardManager,renderer : Renderer = None):
    initialState = ProblemState(board)
    visited = deque([initialState])
    if initialState.board.isGameOver():
        return solution(initialState)

    exploredSet = set()

    while len(visited) >0:
        state = visited.pop()
        exploredSet.add(state)

        for action in state.board.getValidActions():
            newBoard = state.board.push(action, True)
                        #newBoard Renderer
            if renderer : 
                renderer.fromInstance(newBoard).render()
                # wait for input to change render
                # msvcrt.getch()
                # time delay for renderer only
                time.sleep(0.01)

            childState = ProblemState(newBoard,action,state)

            if (childState not in exploredSet) and (childState not in visited):
                if childState.board.isGameOver():
                    return solution(childState)
                visited.append(childState)



# source vertex
#       let S be stack
#       S.push( s )            //Inserting s in stack 
#       mark s as visited.
#       while ( S is not empty):
#           //Pop a vertex from stack to visit next
#           v  =  S.top( )
#          S.pop( )
#          //Push all the neighbours of v in stack that are not visited   
#         for all neighbours w of v in Graph G:
#             if w is not visited :
#                      S.push( w )         
#                     mark w as visited

level = 3  
isRender = False
sokoban = BoardManager(data[level])

start = time.time()
heap = hpy()
heap.setref()
heap_status = heap.heap()


solution=bfs(sokoban) #bfs(board: BoardManager,renderer : Renderer = None):

stop = time.time()
print("The time of the run soKoban Engine :", stop - start,' seconds')
heap_status2 = heap.heap()
print("\nMemory Usage After Creation Of soKoban Engine : ", heap_status2.size - heap_status.size, " bytes")
print("number of action : ",len(solution))
print("-----------------------------------------------\n")
print(solution)


sokoban_solution = BoardManager(data[level])
renderer = Renderer(sokoban_solution).setCaption("Sokoban")
renderer.render()

is_buttonclick = False

while True:

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            is_buttonclick = True

        if event.type == pygame.QUIT:
            pygame.quit()
    
    if is_buttonclick == True and len(solution) > 0:
        sokoban_solution.push(solution.pop(0))
        renderer.fromInstance(sokoban_solution).render()
        pygame.time.wait(50)