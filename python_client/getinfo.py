from dfs_depth_n import dfs_depth_n
from math import log, floor
from dijkstra_level2 import dij_show_way
from queue import LifoQueue
diamond = []
hole = []
start = tuple()
score=0
diccolornumber = {'y': 0, 'g': 0, 'r': 0, 'b': 0}
actions=LifoQueue()
def getinfo(map, height, width, character,scoreinitial):
    global diamond
    global hole
    global start
    global score
    score =scoreinitial
    for i in range(0, height):
        for j in range(0, width):
            if (map[i][j] == 'T'):
                hole.append((i, j, 0))
            if (map[i][j] == '1'):
                diamond.append((i, j, 10))
            if (map[i][j] == '2'):
                diamond.append((i, j, 25))
            if (map[i][j] == '3'):
                diamond.append((i, j, 35))
            if (map[i][j] == '4'):
                diamond.append((i, j, 75))
            if (map[i][j] == ('E'+character)):
                start = (i, j)



def startturn(map, height, width, turn ,maxturn, timelimit):
    global diamond
    global hole
    global diccolornumber
    global score
    global start #should change in other turns
    sizedh = len(diamond) + len(hole)
    depth = floor(log((10**6) * timelimit, sizedh))
    print(start,"start")

    #we change maxturn-turn to maxturn-turn+1 because the first turn is 1
    next_move = dfs_depth_n(map, height, width, maxturn-turn+1, depth, start[0], start[1], diamond, hole, score, diccolornumber)
    print(next_move,"next_move")
    if map[next_move[0]][next_move[1]] == '1':
        diccolornumber['y'] += 1
        score += 10
        diamond.remove((next_move[0], next_move[1], 10))
    if map[next_move[0]][next_move[1]] == '2':
        diccolornumber['g'] += 1
        score += 25
        diamond.remove((next_move[0], next_move[1], 25))
    if map[next_move[0]][next_move[1]] == '3':
        diccolornumber['r'] += 1
        score += 35
        diamond.remove((next_move[0], next_move[1], 35))
    if map[next_move[0]][next_move[1]] == '4':
        diccolornumber['b'] += 1
        score += 75
        diamond.remove((next_move[0], next_move[1], 75))

    way = dij_show_way(start[0], start[1], next_move[0], next_move[1], map, height, width)
    start = next_move
    while not way.empty():
        print(way.get())
    return way


def action_state_func(map,height,width,turn,maxturn,character,score,time):
    global actions

    if turn == 1 and actions.empty():
        getinfo(map, height, width, character, score)
        actions = startturn(map, height, width, turn, maxturn,time)
    if actions.empty():
        actions = startturn(map, height, width, turn, maxturn,time)

    while not actions.empty():
        print(actions.get())

    return actions.get()