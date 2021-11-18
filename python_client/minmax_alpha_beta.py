from dijkstra_level1 import dijkstra
from calculatedFunc import hash_key, sortmoves
from queue import Queue
import numpy as np

storedHkeys = Queue()

def minmax(gridmap, height, width, turn_agent, turn_enemy, diamondlist, holelist, agentx, agenty, enemyx, enemyy, trapcount, depth, scoreagent, scoreenemy, diccolornumberagent,diccolornumberenemy,transpositiontable, enemytraps, agenttraps,transpositionsize):
    current_score_agent = scoreagent
    current_score_enemy = scoreenemy
    visited_diamond = {}
    visited_hole = {}
    max_value = -1
    next_move = tuple()


    def alph_beta_minmax(is_max_turn, agentx, agenty, enemyx, enemyy, alpha, beta, level, remain_turn_agent, remain_turn_enemy, score_agent, score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy):
        global current_score_agent
        global current_score_enemy
        global max_value
        global next_move
        hash_state=hash_key(visited_diamond,visited_hole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy)
        #transposition value (exact,lowerbound,upperbound,depth)
        #transpositiontable[hash_state][3] >= level or transpositiontable[hash_state][3] <= level because position of  add value
        if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] <= level):
            if transpositiontable[hash_state][0] != float('inf'):
                return transpositiontable[hash_state][0]
            if (transpositiontable[hash_state][1] != float('inf')) and (is_max_turn) :
                if transpositiontable[hash_state][1] <= beta:
                    return  transpositiontable[hash_state][1]
            if (transpositiontable[hash_state][2] != float('inf')) and (not is_max_turn):
                if transpositiontable[hash_state][2] >= alpha:
                    return  transpositiontable[hash_state][2]


        if level == depth:
            if len(visited_diamond) == 0:
                value = ((20 * ((score_agent - current_score_agent)-(score_enemy-current_score_enemy))) + (remain_turn_agent - remain_turn_enemy) * 80) // 100
            else:
                value = (((20 * ((score_agent - current_score_agent)-(score_enemy-current_score_enemy))) + (80 * (remain_turn_agent - remain_turn_enemy))) // 100)
            if value > max_value:
                max_value = value
                for keyvisited, valuevisited in visited_diamond.items():
                    if valuevisited[1] == 0:
                        next_move = keyvisited
                for keyvisited, valuevisited in visited_hole.items():
                    if valuevisited[1] == 0:
                        next_move = (keyvisited[0], keyvisited[1])
            return value

        if remain_turn_agent == 0:
            if len(visited_diamond) == 0:
                value = ((20 * ((score_agent - current_score_agent) - (score_enemy - current_score_enemy))) + (remain_turn_agent - remain_turn_enemy) * 80) // 100
            else:
                value = (((20 * ((score_agent - current_score_agent)-(score_enemy-current_score_enemy))) + (80 * (remain_turn_agent-remain_turn_enemy))) // 100)
            if value > max_value:
                max_value = value
                for keyvisited, valuevisited in visited_diamond.items():
                    if valuevisited[1] == 0:
                        next_move = keyvisited
                for keyvisited, valuevisited in visited_hole.items():
                    if valuevisited[1] == 0:
                        next_move = (keyvisited[0], keyvisited[1])
            return value

        if len(diamondlist) == len(visited_diamond):
            value = (((20 * ((score_agent - current_score_agent)-(score_enemy-current_score_enemy))) + (80 * (remain_turn_agent - remain_turn_enemy))) // 100)
            if value > max_value:
                max_value = value
                for keyvisited, valuevisited in visited_diamond.items():
                    if valuevisited[1] == 0:
                        next_move = keyvisited
                for keyvisited, valuevisited in visited_hole.items():
                    if valuevisited[1] == 0:
                        next_move = (keyvisited[0], keyvisited[1])

            return value
        best_value = float('-inf') if is_max_turn else float('inf')
        if is_max_turn:
            dicdistance = dijkstra(gridmap, height, width, agentx, agenty, score_agent, enemytraps)
            sort_diamond_list = sortmoves(dicdistance, diamondlist)
            for diamond in sort_diamond_list:
                d = (diamond[0], diamond[1])
                if (d not in dicdistance):
                    calculatescore = score_agent
                    calculatedistance = float('inf')
                else:
                    calculatescore = dicdistance[(diamond[0], diamond[1])][1]
                    calculatedistance = dicdistance[(diamond[0], diamond[1])][0]
                if d not in visited_diamond:
                    visited_diamond[d] = (True, level)
                    if (calculatedistance <= remain_turn_agent) and (level + 1 <= depth):
                        if (diamond[2] == 10) and (diccolor_number_copy_agent['y'] < 15):
                            diccolor_number_copy_agent['y'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0],diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-calculatedistance,remain_turn_enemy, 10+calculatescore , score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['y'] -= 1

                        if (diamond[2] == 25) and (score_agent >= 15) and (diccolor_number_copy_agent['g'] < 8) and (
                                calculatescore  >= 15):
                            diccolor_number_copy_agent['g'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-calculatedistance,remain_turn_enemy, 25+calculatescore , score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['g'] -= 1

                        if (diamond[2] == 35) and (score_agent >= 50) and (diccolor_number_copy_agent['r'] < 5) and (
                                calculatescore  >= 50):
                            diccolor_number_copy_agent['r'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-calculatedistance,remain_turn_enemy, 35+calculatescore , score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['r'] -= 1

                        if (diamond[2] == 75) and (score_agent >= 140) and (diccolor_number_copy_agent['b'] < 4) and (
                                calculatescore >= 140):
                            diccolor_number_copy_agent['b'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-calculatedistance,remain_turn_enemy, 75+calculatescore , score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['b'] -= 1

                    best_value = max(best_value, result_return)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] > level):
                            transpositiontable[hash_state] = (transpositiontable[hash_state][0],best_value , transpositiontable[hash_state][2], level)
                        else:
                            if len(transpositiontable) < transpositionsize:
                                storedHkeys.put(hash_state)
                                transpositiontable[hash_state] = (float('inf'), best_value, float('inf'), level)
                            else:
                                storedHkeys.get()
                                storedHkeys.put(hash_state)
                                transpositiontable[hash_state] = (float('inf'), best_value, float('inf'), level)
                        return best_value
                    visited_diamond.pop(d, None)
            sort_hole_list = sortmoves(dicdistance, holelist)
            for hole in sort_hole_list:
                h = (hole[0], hole[1])
                if (h not in dicdistance):
                    calculatescore = score_agent
                    calculatedistance = float('inf')
                else:
                    calculatescore = dicdistance[(hole[0], hole[1])][1]
                    calculatedistance = dicdistance[(hole[0], hole[1])][0]
                visited_hole[(h[0], h[1], level)] = (True, level)
                current_hole = (h[0], h[1], 0)

                # distancehole = dijkstra(gridmap, height, width, agentx, agenty, h[0], h[1], score_agent)

                if (calculatedistance <= remain_turn_agent) and (level + 1 <= depth):
                    value_hole = 0
                    for item_hole in holelist:
                        if item_hole != current_hole:
                            value_hole += alph_beta_minmax(not is_max_turn, item_hole[0], item_hole[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-calculatedistance-1,remain_turn_enemy, calculatescore-1, score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)

                    result_return = (value_hole // (len(holelist) - 1))

                best_value = max(best_value, result_return)
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] > level):
                        transpositiontable[hash_state] = (transpositiontable[hash_state][0], best_value, transpositiontable[hash_state][2], level)
                    else:
                        if len(transpositiontable) < transpositionsize:
                            storedHkeys.put(hash_state)
                            transpositiontable[hash_state] = (float('inf'), best_value, float('inf'), level)
                        else:
                            storedHkeys.get()
                            storedHkeys.put(hash_state)
                            transpositiontable[hash_state] = (float('inf'), best_value, float('inf'), level)
                    return best_value
                visited_hole.pop((h[0], h[1], level), None)

        else:
            dicdistanceenemy = dijkstra(gridmap, height, width, enemyx, enemyy, score_enemy, agenttraps)
            sort_diamond_list = sortmoves(dicdistanceenemy, diamondlist)
            for diamond in sort_diamond_list:
                d = (diamond[0], diamond[1])
                for diamond in diamondlist:
                    d = (diamond[0], diamond[1])
                    if (d not in dicdistanceenemy):
                        calculatescore = score_agent
                        calculatedistance = float('inf')
                    else:
                        calculatescore = dicdistanceenemy[(diamond[0], diamond[1])][1]
                        calculatedistance = dicdistanceenemy[(diamond[0], diamond[1])][0]
                if d not in visited_diamond:
                    visited_diamond[d] = (True, level)

                    if (calculatedistance <= remain_turn_enemy) and (level + 1 <= depth):
                        if (diamond[2] == 10) and (diccolor_number_copy_enemy['y'] < 15):
                            diccolor_number_copy_enemy['y'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy-calculatedistance, score_agent,
                                                             10 +calculatescore, diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['y'] -= 1

                        if (diamond[2] == 25) and (score_agent >= 15) and (diccolor_number_copy_enemy['g'] < 8) and (
                                calculatescore >= 15):
                            diccolor_number_copy_enemy['g'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy - calculatedistance, score_agent ,
                                                              25 + calculatescore, diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['g'] -= 1

                        if (diamond[2] == 35) and (score_agent >= 50) and (diccolor_number_copy_enemy['r'] < 5) and (
                                calculatescore >= 50):
                            diccolor_number_copy_enemy['r'] += 1
                            result_return = alph_beta_minmax(not is_max_turn,agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy - calculatedistance, score_agent,
                                                             35 + calculatescore, diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['r'] -= 1

                        if (diamond[2] == 75) and (score_agent >= 140) and (diccolor_number_copy_enemy['b'] < 4) and (
                                calculatescore >= 140):
                            diccolor_number_copy_enemy['b'] += 1
                            result_return = alph_beta_minmax(not is_max_turn,agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy- calculatedistance, score_agent,
                                                             75 + calculatescore, diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['b'] -= 1

                    best_value = max(best_value, result_return)
                    beta = max(beta, best_value)
                    if beta <= alpha:
                        if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] > level):
                            transpositiontable[hash_state] = (transpositiontable[hash_state][0], transpositiontable[hash_state][1],best_value , level)
                        else:
                            if len(transpositiontable) < transpositionsize:
                                storedHkeys.put(hash_state)
                                transpositiontable[hash_state] = (float('inf'), float('inf'), best_value, level)
                            else:
                                storedHkeys.get()
                                storedHkeys.put(hash_state)
                                transpositiontable[hash_state] = (float('inf'),float('inf'), best_value, level)

                        return best_value
                    visited_diamond.pop(d, None)
            sort_hole_list = sortmoves(dicdistanceenemy, holelist)
            for hole in sort_hole_list:
                h = (hole[0], hole[1])
                if (h not in dicdistanceenemy):
                    calculatescore = score_agent
                    calculatedistance = float('inf')
                else:
                    calculatescore = dicdistanceenemy[(hole[0], hole[1])][1]
                    calculatedistance = dicdistanceenemy[(hole[0], hole[1])][0]
                visited_hole[(h[0], h[1], level)] = (True, level)
                current_hole = (h[0], h[1], 0)
                # distancehole = dijkstra(gridmap, height, width, enemyx, enemyy, h[0], h[1], score_enemy)

                if (calculatedistance <= remain_turn_enemy) and (level + 1 <= depth):
                    value_hole = 0
                    for item_hole in holelist:
                        if item_hole != current_hole:
                            value_hole += alph_beta_minmax(not is_max_turn, agentx, agenty, item_hole[0], item_hole[1],
                                                           alpha, beta, level + 1, remain_turn_agent,
                                                           remain_turn_enemy - calculatedistance - 1, score_agent,
                                                           calculatescore- 1, diccolor_number_copy_agent,
                                                           diccolor_number_copy_enemy)

                    result_return = (value_hole // (len(holelist) - 1))

                best_value = max(best_value, result_return)
                beta = max(beta, best_value)
                if beta <= alpha:
                    if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] > level):
                        transpositiontable[hash_state] = (transpositiontable[hash_state][0], transpositiontable[hash_state][1], best_value, level)
                    else:
                        if len(transpositiontable) < transpositionsize:
                            storedHkeys.put(hash_state)
                            transpositiontable[hash_state] = (float('inf'), float('inf'), best_value, level)
                        else:
                            storedHkeys.get()
                            storedHkeys.put(hash_state)
                            transpositiontable[hash_state] = (float('inf'), float('inf'), best_value, level)
                    return best_value
                visited_hole.pop((h[0], h[1], level), None)

        #check size for this transposition for update
        if (hash_state in transpositiontable) and (transpositiontable[hash_state][3] > level):
            transpositiontable[hash_state]=(best_value,transpositiontable[hash_state][1],transpositiontable[hash_state][2],level)
        else:
            if len(transpositiontable) < transpositionsize:
                storedHkeys.put(hash_state)
                transpositiontable[hash_state] = (best_value,float('inf'), float('inf'),  level)
            else:
                storedHkeys.get()
                storedHkeys.put(hash_state)
                transpositiontable[hash_state] = (best_value,float('inf'), float('inf'), level)
        return best_value

    diccolor_number_copy_agent = diccolornumberagent
    diccolor_number_copy_enemy=diccolornumberenemy
    alph_beta_minmax(True, agentx, agenty, enemyx, enemyy, float('-inf'), float('inf'), 0, turn_agent,turn_enemy, scoreagent, scoreenemy, diccolor_number_copy_agent,diccolor_number_copy_enemy)
    return next_move