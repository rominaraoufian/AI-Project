from dfs_depth_n import dfs_depth_n
from math import log, floor
from dijkstra_level2 import dij_show_way
from queue import LifoQueue
diamond = []
hole = []
start = tuple()
score=0
size_action=0
diccolornumber = {'y': 0, 'g': 0, 'r': 0, 'b': 0}
actions=LifoQueue()
sizedh=0
prev_action=''
walls =0
def getinfo(gridmap, height, width, character,scoreinitial):
    global diamond
    global hole
    global start
    global score
    global  sizedh
    global walls
    score =scoreinitial
    for i in range(0, height):
        for j in range(0, width):
            if (gridmap[i][j] == 'T'):
                hole.append((i, j, 0))
            if (gridmap[i][j] == '1'):
                diamond.append((i, j, 10))
            if (gridmap[i][j] == '2'):
                diamond.append((i, j, 25))
            if (gridmap[i][j] == '3'):
                diamond.append((i, j, 35))
            if (gridmap[i][j] == '4'):
                diamond.append((i, j, 75))
            if (gridmap[i][j] == ('E'+character)):
                start = (i, j)
            if (gridmap[i][j] == 'W'):
                walls += 1
    sizedh = len(diamond) + len(hole)
    # print(diamond, "diamond")
    # print(hole,"hole")


def startturn(gridmap, height, width, turn, maxturn, timelimit):
    global diamond
    global hole
    global diccolornumber
    global score
    global start #should change in other turns
    global sizedh
    way = LifoQueue()
    depth = floor(log((10**4) * timelimit, max(sizedh,2)))
    # if (((height*width-walls)//height*width)*100) > 2:
    #     depth -= 1
    print(start,"start in startturn")
    print(depth,"depth")
    # print(score,"befordfs")
    #we change maxturn-turn to maxturn-turn+1 because the first turn is 1
    next_move = dfs_depth_n(gridmap, height, width, maxturn-turn+1,depth, start[0], start[1], diamond, hole, score, diccolornumber)
    # print(score,"afterdfsscore")
    print(next_move,"next_move")
    if next_move == ():
        for i in range(maxturn-turn+1):
           way.put('n')
    else:
        if gridmap[next_move[0]][next_move[1]] == '1':
            diccolornumber['y'] += 1
            score += 10
            diamond.remove((next_move[0], next_move[1], 10))
        if gridmap[next_move[0]][next_move[1]] == '2':
            diccolornumber['g'] += 1
            score += 25
            diamond.remove((next_move[0], next_move[1], 25))
        if gridmap[next_move[0]][next_move[1]] == '3':
            diccolornumber['r'] += 1
            score += 35
            diamond.remove((next_move[0], next_move[1], 35))
        if gridmap[next_move[0]][next_move[1]] == '4':
            diccolornumber['b'] += 1
            score += 75
            diamond.remove((next_move[0], next_move[1], 75))

        way = dij_show_way(start[0], start[1], next_move[0], next_move[1], gridmap, height, width, score)
    start = next_move
    # print(score,"scoreafter")
    # while not way.empty():
    #     print(way.get())
    return way


def action_state_func(gridmap, height, width, turn, maxturn, character, maxscore, time):
    global actions
    global size_action
    global score
    global prev_action
    global hole
    global start
    if turn == 1 and actions.empty():
        getinfo(gridmap, height, width, character, maxscore)
        actions = startturn(gridmap, height, width, turn, maxturn, time)
        size_action = actions.qsize()
    if actions.empty():
        score -= size_action
        if prev_action == 't':
            for item_hole in hole:
                if gridmap[item_hole[0]][item_hole[1]] == 'T'+character:
                    start = (item_hole[0],item_hole[1])
                    print(start,"start hole")
        actions = startturn(gridmap, height, width, turn, maxturn, time)
        # print(actions)
        size_action = actions.qsize()

    # while not actions.empty():
    #     print(actions.get())
    # print("weeeeee innnnn")
    prev_action=actions.get()
    print(prev_action,"current_action")
    return prev_action