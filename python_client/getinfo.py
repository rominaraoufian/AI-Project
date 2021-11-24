from dfs_depth_n import dfs_depth_n
from math import log, floor
from dijkstra_level2 import dij_show_way,dij_show_action
from queue import LifoQueue
from minmax_alpha_beta import minmax
from minimax_alpha_beta1 import minmax1
from TrapOrNot import trapornot

#change diamondlist to dictionary, should other functions
diamond = {}
hole = {}
start_agent = tuple()
score = 0
size_action = 0
diccolornumber_agent = {'y': 0, 'g': 0, 'r': 0, 'b': 0}
diccolornumber_enemy = {'y': 0, 'g': 0, 'r': 0, 'b': 0}
actions = LifoQueue()
sizedh = 0
sizedh_minmax=0
prev_action = ''
walls = 0
score_agent = 0
score_enemy = 0
start_enemy = tuple()
agent_id = 0
enemy_id = 0
enemy_trap = []
agent_trap = []
transposition = {}
transposition_size = 0
max_depth=0


def getinfo(gridmap, height, width, character,scoreinitial):
    global diamond
    global hole
    global start_agent
    global score
    global sizedh
    global walls
    score = scoreinitial

    for i in range(0, height):
        for j in range(0, width):
            if gridmap[i][j]=='W':
                walls += 1
            if gridmap[i][j] == 'T':
                hole.append((i, j, 0))
            if gridmap[i][j] == '1':
                diamond.append((i, j, 10))
            if gridmap[i][j] == '2':
                diamond.append((i, j, 25))
            if gridmap[i][j] == '3':
                diamond.append((i, j, 35))
            if gridmap[i][j] == '4':
                diamond.append((i, j, 75))
            if gridmap[i][j] == ('E'+character):
                start_agent = (i, j)
            if (gridmap[i][j] == 'W'):
                walls += 1
    sizedh = len(diamond) + len(hole)
    # print(diamond, "diamond")
    # print(hole,"hole")


def startturn(gridmap, height, width, turn, maxturn, timelimit,character):
    global diamond
    global hole
    global diccolornumber
    global score
    global start_agent #should change in other turns
    global sizedh
    global walls
    way = LifoQueue()


    depth = floor(log((10 ** 4) * timelimit, max(sizedh, 2)))

    if (walls // (height + width)) * 100 < 5 and len(hole) == 0:
        depth -= 1

    # print(start,"start in startturn")

    # print(depth,"depth")
    # print(score,"befordfs")
    #we change maxturn-turn to maxturn-turn+1 because the first turn is 1
    next_move = dfs_depth_n(gridmap, height, width, maxturn - turn + 1, depth, start_agent[0], start_agent[1], diamond, hole, score, diccolornumber)
    # print(score,"afterdfsscore")
    # print(next_move, "next_move")
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

        # print(start," start")
        # print(next_move, "next_move")
        way = dij_show_way(start_agent[0], start_agent[1], next_move[0], next_move[1], gridmap, height, width, score,character)
    start_agent = next_move
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
    global start_agent
    if turn == 1 and actions.empty():
        getinfo(gridmap, height, width, character, maxscore)
        actions = startturn(gridmap, height, width, turn, maxturn, time,character)
        size_action = actions.qsize()
    if actions.empty():
        score -= size_action
        if prev_action == 't':
            for item_hole in hole:
                if gridmap[item_hole[0]][item_hole[1]] == 'T'+character:
                    start_agent = (item_hole[0], item_hole[1])
                    # print(start,"start hole")
        actions = startturn(gridmap, height, width, turn, maxturn, time,character)
        # print(actions)
        size_action = actions.qsize()

    # while not actions.empty():
    #     print(actions.get())
    # print("weeeeee innnnn")
    prev_action = actions.get()
    # print(prev_action,"current_action")
    return prev_action

def getinfophase2(gridmap, height, width, turn, maxturn, character,scoreinitial, scores, trapcount,timelimit):
    global diamond
    global hole
    global start_agent
    global score_agent
    global score_enemy
    global sizedh_minmax
    global walls
    global start_enemy
    global enemy_list
    global transposition
    global transposition_size
    global max_depth
    score_agent = scoreinitial
    score_enemy = scoreinitial

    if character == 'A':
        character_enemy = 'B'
        agent_id = 0
        enemy_id = 1
        score_agent = scores[0]
        score_enemy = scores[1]
    else:
        character_enemy = 'A'
        agent_id = 1
        enemy_id = 0
        score_enemy = scores[0]
        score_agent = scores[1]

    if turn == 1:
        for i in range(0, height):
            for j in range(0, width):
                s = str(gridmap[i][j])
                if gridmap[i][j] == 'W':
                    walls += 1
                if gridmap[i][j] == 'T':
                    hole[(i, j, 0)] = True
                if gridmap[i][j] == '1':
                    diamond[(i, j, 10)] = True
                if gridmap[i][j] == '2':
                    diamond[(i, j, 25)] = True
                if gridmap[i][j] == '3':
                    diamond[(i, j, 35)] = True
                if gridmap[i][j] == '4':
                    diamond[(i, j, 75)] = True
                if s.find(character) != -1:
                    start_agent = (i, j)
                if s.find(character_enemy) != -1:
                    start_enemy = (i, j)


        transposition_size = height * width - (walls+len(diamond)+len(hole))

        sizedh_minmax = len(diamond) + len(hole)
    if turn != 1:
        previous_enemy_place = start_enemy
        prevous_enemy_score = score_enemy
        for i in range(0, height):
            for j in range(0, width):
                s = str(gridmap[i][j])
                if s.find(character) != -1:
                    start_agent = (i, j)
                if s.find(character_enemy) != -1:
                    start_enemy = (i, j)


        if start_enemy == previous_enemy_place and (start_enemy not in enemy_trap):
            enemy_trap.append(start_enemy)


        # score_enemy -= 1
        # score_agent -= 1
        # if start_agent == previous_enemy_place:
        #     if prevous_enemy_score > score_agent:
        #         score_agent -= 19
        #     elif prevous_enemy_score < score_agent:
        #         score_enemy -= 19
        #     elif score_agent == prevous_enemy_score:
        #         score_enemy -= 19
        # if start_enemy == start_agent:
        #     if score_enemy > score_agent:
        #         score_agent -= 19
        #     elif score_agent > score_enemy:
        #         score_enemy -= 19
        #     elif score_agent == score_agent:
        #         score_agent -= 19
        # fortrap = str(gridmap[start_enemy[i]][start_enemy[j]])
        # if fortrap.find(character.lower()):
        #     score_enemy -= 39
        if (start_enemy[0],start_enemy[1],10) in diamond:
            if diccolornumber_enemy['y'] < 15:
                diccolornumber_enemy['y'] += 1
                del diamond[ (start_enemy[0],start_enemy[1],10)]

        if (start_enemy[0],start_enemy[1],25) in diamond:
            if diccolornumber_enemy['g'] < 8 and score_enemy-25 > 14:
                diccolornumber_enemy['g'] += 1
                del diamond [(start_enemy[0],start_enemy[1],25)]

        if (start_enemy[0],start_enemy[1],35) in diamond:
            if diccolornumber_enemy['r'] < 5 and score_enemy - 35 > 49:
                diccolornumber_enemy['r'] += 1
                del diamond[(start_enemy[0],start_enemy[1],35)]
        if (start_enemy[0], start_enemy[1], 75) in diamond:
            if diccolornumber_enemy['b'] < 4 and score_enemy - 75 > 139:
                diccolornumber_enemy['b'] += 1
                del diamond[(start_enemy[0], start_enemy[1], 75)]

        if (start_agent[0], start_agent[1], 10) in diamond:
            if diccolornumber_agent['y'] < 15:
                diccolornumber_agent['y'] += 1
                del diamond[(start_agent[0], start_agent[1], 10)]

        if (start_agent[0], start_agent[1], 25) in diamond:
            if diccolornumber_agent['g'] < 8 and score_agent - 25 > 14:
                diccolornumber_agent['g'] += 1
                del diamond[(start_agent[0], start_agent[1], 25)]

        if (start_agent[0], start_agent[1], 35) in diamond:
            if diccolornumber_agent['r'] < 5 and score_agent - 35 > 49:
                diccolornumber_agent['r'] += 1
                del diamond[(start_agent[0], start_agent[1], 35)]

        if (start_agent[0], start_agent[1], 75) in diamond:
            if diccolornumber_agent['b'] < 4 and score_agent - 75 > 139:
               diccolornumber_agent['b'] += 1
               del diamond[(start_agent[0], start_agent[1], 75)]



    agent_trap=[]

    # print(character_enemy,"character enemy")
    # print(character,"character")
    depth_minmax = floor(log((10 ** 4) * timelimit, max(sizedh_minmax, 2)))

    if (walls // (height + width)) * 100 < 5 and len(hole) == 0:

        depth_minmax -= 1

    depth_minmax = max(max_depth, depth_minmax)
    if depth_minmax % 2:
        depth_minmax = max(depth_minmax-1, 2)
    # print("-"*15)
    # print(maxturn-turn+1)
    # print("-" * 15)
    next_move,max_depth = minmax(gridmap, height, width, maxturn-turn+1, maxturn-turn+1, diamond, hole, start_agent[0], start_agent[1], start_enemy[0], start_enemy[1], trapcount, depth_minmax, score_agent, score_enemy, diccolornumber_agent,diccolornumber_enemy,transposition, enemy_trap, agent_trap,transposition_size,max_depth,character,character_enemy)
    # print(next_move,"next_moove")
    if not next_move == ():
       next_action = dij_show_action(start_agent[0], start_agent[1], next_move[0], next_move[1], gridmap, height, width,score_agent,enemy_trap,character,diccolornumber_agent)
       return next_action
    else:
        return 'n'



def getinfophase2_1(gridmap, height, width, turn, maxturn, character,scoreinitial, scores, trapcount,timelimit):
    global diamond
    global hole
    global start_agent
    global score_agent
    global score_enemy
    global sizedh_minmax
    global walls
    global start_enemy
    global enemy_list
    global transposition
    global transposition_size
    global max_depth
    global agent_trap
    score_agent = scoreinitial
    score_enemy = scoreinitial

    if character == 'A':
        character_enemy = 'B'
        agent_id = 0
        enemy_id = 1
        score_agent = scores[0]
        score_enemy = scores[1]
    else:
        character_enemy = 'A'
        agent_id = 1
        enemy_id = 0
        score_enemy = scores[0]
        score_agent = scores[1]

    if turn == 1:
        for i in range(0, height):
            for j in range(0, width):
                s = str(gridmap[i][j])
                if gridmap[i][j] == 'W':
                    walls += 1
                if gridmap[i][j] == 'T':
                    hole[(i, j, 0)] = True
                if gridmap[i][j] == '1':
                    diamond[(i, j, 10)] = True
                if gridmap[i][j] == '2':
                    diamond[(i, j, 25)] = True
                if gridmap[i][j] == '3':
                    diamond[(i, j, 35)] = True
                if gridmap[i][j] == '4':
                    diamond[(i, j, 75)] = True
                if s.find(character) != -1:
                    start_agent = (i, j)
                if s.find(character_enemy) != -1:
                    start_enemy = (i, j)
        print(start_enemy,"start enemy")
        print(start_agent, "start_agent")

        transposition_size = height * width - (walls+len(diamond)+len(hole))

        sizedh_minmax = len(diamond) + len(hole)
    if turn != 1:
        previous_enemy_place = start_enemy
        prevous_enemy_score = score_enemy
        for i in range(0, height):
            for j in range(0, width):
                s = str(gridmap[i][j])
                if s.find(character) != -1:
                    start_agent = (i, j)
                if s.find(character_enemy) != -1:
                    start_enemy = (i, j)


        if start_enemy == previous_enemy_place and (start_enemy not in enemy_trap):
            enemy_trap.append(start_enemy)

        if (start_enemy[0],start_enemy[1],10) in diamond:
            if diccolornumber_enemy['y'] < 15:
                diccolornumber_enemy['y'] += 1
                del diamond[ (start_enemy[0],start_enemy[1],10)]

        if (start_enemy[0],start_enemy[1],25) in diamond:
            if diccolornumber_enemy['g'] < 8 and score_enemy-25 > 14:
                diccolornumber_enemy['g'] += 1
                del diamond [(start_enemy[0],start_enemy[1],25)]

        if (start_enemy[0],start_enemy[1],35) in diamond:
            if diccolornumber_enemy['r'] < 5 and score_enemy - 35 > 49:
                diccolornumber_enemy['r'] += 1
                del diamond[(start_enemy[0],start_enemy[1],35)]
        if (start_enemy[0], start_enemy[1], 75) in diamond:
            if diccolornumber_enemy['b'] < 4 and score_enemy - 75 > 139:
                diccolornumber_enemy['b'] += 1
                del diamond[(start_enemy[0], start_enemy[1], 75)]

        if (start_agent[0], start_agent[1], 10) in diamond:
            if diccolornumber_agent['y'] < 15:
                diccolornumber_agent['y'] += 1
                del diamond[(start_agent[0], start_agent[1], 10)]

        if (start_agent[0], start_agent[1], 25) in diamond:
            if diccolornumber_agent['g'] < 8 and score_agent - 25 > 14:
                diccolornumber_agent['g'] += 1
                del diamond[(start_agent[0], start_agent[1], 25)]

        if (start_agent[0], start_agent[1], 35) in diamond:
            if diccolornumber_agent['r'] < 5 and score_agent - 35 > 49:
                diccolornumber_agent['r'] += 1
                del diamond[(start_agent[0], start_agent[1], 35)]

        if (start_agent[0], start_agent[1], 75) in diamond:
            if diccolornumber_agent['b'] < 4 and score_agent - 75 > 139:
               diccolornumber_agent['b'] += 1
               del diamond[(start_agent[0], start_agent[1], 75)]





    # print(character_enemy,"character enemy")
    # print(character,"character")
    depth_minmax = floor(log((10 ** 4) * timelimit, max(sizedh_minmax, 2)))

    if (walls // (height + width)) * 100 < 5 and len(hole) == 0:

        depth_minmax -= 1

    depth_minmax = max(max_depth, depth_minmax)
    if depth_minmax % 2:
        depth_minmax = max(depth_minmax-1, 2)
    print("-"*15)
    print(maxturn-turn+1)
    print("-" * 15)
    # print(start_enemy,"start_enemy")
    # print(start_agent,"start_agent")
    # print(turn,"turn")

    print(score_enemy, "score_enemy", '#' * 5)
    print(start_enemy, "start_enemy", '#' * 6)
    print(start_agent,"startagent","@"*10)
    print(score_agent,"scoreageny",'@'*10)
    next_move,next_move_enemy,max_depth,maxvalue = minmax1(gridmap, height, width, maxturn-turn+1, maxturn-turn+1, diamond, hole, start_agent[0], start_agent[1], start_enemy[0], start_enemy[1], trapcount, depth_minmax, score_agent, score_enemy, diccolornumber_agent,diccolornumber_enemy,transposition, enemy_trap, agent_trap,transposition_size,max_depth,character,character_enemy)
    print(next_move_enemy,"next_moove")
    trapsize = len(agent_trap)
    maxvaluefortrap = float('-inf')

    next_move_trap = tuple()

    if not next_move_enemy == ():
        if trapsize == 0 and score_agent > 35:
            next_move_trap,maxvaluefortrap = trapornot(gridmap,height, width, next_move, next_move_enemy, maxvalue, score_agent, score_enemy, start_agent, start_enemy, 35, maxturn-turn+1, diccolornumber_agent, diccolornumber_enemy, agent_trap, enemy_trap, character, character_enemy)
            #print(next_move,"nextmovetrap")
        elif trapsize == 1 and score_agent > (35*2):
            next_move_trap,maxvaluefortrap = trapornot(gridmap, height, width, next_move, next_move_enemy, maxvalue, score_agent,
                                  score_enemy, start_agent, start_enemy, (35*2), maxturn - turn + 1, diccolornumber_agent,
                                  diccolornumber_enemy, agent_trap, enemy_trap, character, character_enemy)
            #print(next_move, "nextmovetrap")
        elif trapsize == 2 and score_agent > (35 * 3):
            next_move_trap,maxvaluefortrap = trapornot(gridmap, height, width, next_move, next_move_enemy, maxvalue, score_agent,
                                  score_enemy, start_agent, start_enemy, (35*3), maxturn - turn + 1, diccolornumber_agent,
                                  diccolornumber_enemy, agent_trap, enemy_trap, character, character_enemy)
            #print(next_move, "nextmovetrap")
    if next_move_trap != () and maxvaluefortrap > maxvalue:
        next_move = next_move_trap
    if not next_move == ():
       next_action = dij_show_action(start_agent[0], start_agent[1], next_move[0], next_move[1], gridmap, height, width,score_agent,score_enemy,enemy_trap,character,character_enemy,diccolornumber_agent)
       print(next_action, "next_action")
       if next_action == 'p':
           print("*****************************p**************************************")
           agent_trap.append(next_move)
       return next_action
    else:
        return 'n'
