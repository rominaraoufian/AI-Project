from dfs_depth_n import dfs_depth_n
from math import log, floor
from dijkstra_level2 import dij_show_way
from queue import LifoQueue
diamond = []
hole = []
start = tuple()
diccolornumber = {'y': 0, 'g': 0, 'r': 0, 'b': 0}

def getinfo(map, height, width, turn, maxturn, character):
    global diamond
    global hole
    global start
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
            if (map[i][j] == character):
                start = (i, j)


def startturn(map, height, width, turn ,maxturn, score, timelimit):
    global diamond
    global hole
    global diccolornumber
    global start #should change in other turns
    sizedh = len(diamond) + len(hole)
    depth = floor(log((10**6) * timelimit, sizedh))
    next_move = dfs_depth_n(map,height. width, maxturn-turn, depth, start[0], start[1], diamond, hole, score, diccolornumber)
    if map[next_move[0]][next_move[1]] == '1':
        diccolornumber['y'] += 1
        diamond.remove((next_move[0], next_move[1], 10))
    if map[next_move[0]][next_move[1]] == '2':
        diccolornumber['g'] += 1
        diamond.remove((next_move[0], next_move[1], 25))
    if map[next_move[0]][next_move[1]] == '3':
        diccolornumber['r'] += 1
        diamond.remove((next_move[0], next_move[1], 35))
    if map[next_move[0]][next_move[1]] == '4':
        diccolornumber['b'] += 1
        diamond.remove((next_move[0], next_move[1], 75))

    way = dij_show_way(start[0], start[1], next_move[0], next_move[1], map, height, width)
    start = next_move
    return way
