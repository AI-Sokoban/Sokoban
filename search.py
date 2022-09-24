import time
import os
from datetime import datetime
from board import BoardManager
from collections import deque
from map import maps

# renderer
from render import Renderer
import msvcrt
import pygame

import time


# test memory
import guppy
from guppy import hpy
import numpy as np


class ProblemState:
    def __init__(self, board: BoardManager, action: str = None, prevState=None):
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


def bfs(board: BoardManager, renderer: Renderer = None):
    detail = {"alg": "bfs", "nodeGenerated": 1}

    initialState = ProblemState(board)
    queue = deque([initialState])

    if initialState.board.isGameOver():
        return solution(initialState), detail

    exploredSet = set()

    while len(queue) > 0:
        state = queue.popleft()
        exploredSet.add(state)
        detail["nodeGenerated"] += 1

        for action in state.board.getValidActions():
            newBoard = state.board.push(action, True)

            # newBoard Renderer
            if renderer:
                renderer.fromInstance(newBoard).render()
                # wait for input to change render
                # msvcrt.getch()
                # time delay for renderer only
                time.sleep(0.01)

            childState = ProblemState(newBoard, action, state)

            if (childState not in exploredSet) and (childState not in queue):
                if childState.board.isGameOver():
                    return solution(childState), detail
                queue.append(childState)


def dfs(board: BoardManager, renderer: Renderer = None):
    detail = {"alg": "dfs", "nodeGenerated": 1}

    initialState = ProblemState(board)
    visited = deque([initialState])
    if initialState.board.isGameOver():
        return solution(initialState), detail

    exploredSet = set()

    while len(visited) > 0:
        state = visited.pop()
        exploredSet.add(state)
        detail["nodeGenerated"] += 1

        for action in state.board.getValidActions():
            newBoard = state.board.push(action, True)
            # newBoard Renderer
            if renderer:
                renderer.fromInstance(newBoard).render()
                # wait for input to change render
                # msvcrt.getch()
                # time delay for renderer only
                time.sleep(0.01)

            childState = ProblemState(newBoard, action, state)

            if (childState not in exploredSet) and (childState not in visited):
                if childState.board.isGameOver():
                    return solution(childState), detail
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

level = 0
isRender = False
sokoban = BoardManager(maps[level])

start = time.time()
heap = hpy()
heap.setref()
heap_status = heap.heap()


# bfs(board: BoardManager,renderer : Renderer = None):
solution, detail = bfs(sokoban)

stop = time.time()
heap_status2 = heap.heap()

timeUsage = stop - start
memoryUsage = heap_status2.size - heap_status.size


# write solution detail to file
resultDir = "results"
filename = f"solution-{detail['alg']}-l{level}.txt"
relPath = os.path.join(resultDir, filename)
with open(relPath, "w") as f:
    now = datetime.now()
    nowStrft = now.strftime("%d/%m/%Y, %H:%M:%S")
    f.write(f"Finished at: {nowStrft}\n")

    f.write(f"Node generated: {detail['nodeGenerated']}\n")

    mapObj = [i.__str__() for i in solution]
    actionString = " ".join(mapObj)
    f.write(actionString + "\n")

    f.write(f"Number of action: {len(solution)}\n")

    f.write(f"Time usage: {timeUsage} seconds\n")

    f.write(f"Memory usage: {memoryUsage} bytes\n")

    f.write("\n")

print("K Engine Activate!!!")
print("The time of the run soKoban Engine :", timeUsage, " seconds")
print("Node generated: ", detail["nodeGenerated"])
print(
    "\nMemory Usage After Creation Of soKoban Engine : ",
    heap_status2.size - heap_status.size,
    " bytes",
)
print("number of action : ", len(solution))
print("-----------------------------------------------\n")
print(solution)


sokoban_solution = BoardManager(maps[level])
renderer = Renderer(sokoban_solution).setCaption("Sokoban")
renderer.render()

is_buttonclick = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_buttonclick = True

        if event.type == pygame.QUIT:
            pygame.quit()

    if is_buttonclick == True and len(solution) > 0:
        sokoban_solution.push(solution.pop(0))
        renderer.fromInstance(sokoban_solution).render()
        pygame.time.wait(50)
