from dijkstra_level1 import dijkstra
import numpy as np


def minmax(gridmap, height, width, turn_agent, turn_enemy, diamondlist, holelist, agentx, agenty, enemyx, enemyy, trapcount, depth, scoreagent, scoreenemy, diccolornumberagent,diccolornumberenemy,transformtable):
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
            array_distance = dijkstra(gridmap, height, width, agentx, agenty, score_agent)
            for diamond in diamondlist:
                d = (diamond[0], diamond[1])
                if d not in visited_diamond:
                    visited_diamond[d] = (True, level)
                    if (array_distance[diamond[0]][diamond[1]] <= remain_turn_agent) and (level + 1 <= depth):
                        if (diamond[2] == 10) and (diccolor_number_copy_agent['y'] < 15) and ((score_agent - array_distance[diamond[0]][diamond[1]]) >= 0):
                            diccolor_number_copy_agent['y'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0],diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-array_distance[diamond[0]][diamond[1]],remain_turn_enemy, score_agent+10-array_distance[diamond[0]][diamond[1]], score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['y'] -= 1

                        if (diamond[2] == 25) and (score_agent >= 15) and (diccolor_number_copy_agent['g'] < 8) and (
                                (score_agent - array_distance[diamond[0]][diamond[1]]) >= 15):
                            diccolor_number_copy_agent['g'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-array_distance[diamond[0]][diamond[1]],remain_turn_enemy, score_agent+25-array_distance[diamond[0]][diamond[1]], score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['g'] -= 1

                        if (diamond[2] == 35) and (score_agent >= 50) and (diccolor_number_copy_agent['r'] < 5) and (
                                (score_agent - array_distance[diamond[0]][diamond[1]]) >= 50):
                            diccolor_number_copy_agent['r'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-array_distance[diamond[0]][diamond[1]],remain_turn_enemy, score_agent+35-array_distance[diamond[0]][diamond[1]], score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['r'] -= 1

                        if (diamond[2] == 75) and (score_agent >= 140) and (diccolor_number_copy_agent['b'] < 4) and (
                                (score_agent - array_distance[diamond[0]][diamond[1]]) >= 140):
                            diccolor_number_copy_agent['b'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, diamond[0], diamond[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-array_distance[diamond[0]][diamond[1]],remain_turn_enemy, score_agent+75-array_distance[diamond[0]][diamond[1]], score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)
                            diccolor_number_copy_agent['b'] -= 1

                    best_value = max(best_value, result_return)
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        return best_value
                    visited_diamond.pop(d, None)

            for hole in holelist:
                h = (hole[0], hole[1])
                visited_hole[(h[0], h[1], level)] = (True, level)
                current_hole = (h[0], h[1], 0)

                # distancehole = dijkstra(gridmap, height, width, agentx, agenty, h[0], h[1], score_agent)

                if (array_distance[hole[0]][hole[1]] <= remain_turn_agent) and (level + 1 <= depth):
                    value_hole = 0
                    for item_hole in holelist:
                        if item_hole != current_hole:
                            value_hole += alph_beta_minmax(not is_max_turn, item_hole[0], item_hole[1], enemyx, enemyy, alpha, beta, level+1, remain_turn_agent-array_distance[hole[0]][hole[1]]-1,remain_turn_enemy, score_agent-array_distance[hole[0]][hole[1]]-1, score_enemy,diccolor_number_copy_agent,diccolor_number_copy_enemy)

                    result_return = (value_hole // (len(holelist) - 1))

                best_value = max(best_value, result_return)
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    return best_value
                visited_hole.pop((h[0], h[1], level), None)

        else:
            array_distance_enemy = dijkstra(gridmap, height, width, enemyx, enemyy, score_enemy)
            for diamond in diamondlist:
                d = (diamond[0], diamond[1])
                if d not in visited_diamond:
                    visited_diamond[d] = (True, level)

                    if (array_distance_enemy[diamond[0]][diamond[1]] <= remain_turn_enemy) and (level + 1 <= depth):
                        if (diamond[2] == 10) and (diccolor_number_copy_enemy['y'] < 15) and (
                                (score_enemy - array_distance_enemy[diamond[0]][diamond[1]]) >= 0):
                            diccolor_number_copy_enemy['y'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy-array_distance_enemy[diamond[0]][diamond[1]], score_agent,
                                                             score_enemy+ 10 - array_distance_enemy[diamond[0]][diamond[1]], diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['y'] -= 1

                        if (diamond[2] == 25) and (score_agent >= 15) and (diccolor_number_copy_enemy['g'] < 8) and (
                                (score_enemy - array_distance_enemy[diamond[0]][diamond[1]]) >= 15):
                            diccolor_number_copy_enemy['g'] += 1
                            result_return = alph_beta_minmax(not is_max_turn, agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy - array_distance_enemy[diamond[0]][diamond[1]], score_agent ,
                                                             score_enemy+ 25 - array_distance_enemy[diamond[0]][diamond[1]], diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['g'] -= 1

                        if (diamond[2] == 35) and (score_agent >= 50) and (diccolor_number_copy_enemy['r'] < 5) and (
                                (score_enemy - array_distance_enemy[diamond[0]][diamond[1]]) >= 50):
                            diccolor_number_copy_enemy['r'] += 1
                            result_return = alph_beta_minmax(not is_max_turn,agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy - array_distance_enemy[diamond[0]][diamond[1]], score_agent,
                                                             score_enemy+ 35 - array_distance_enemy[diamond[0]][diamond[1]], diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['r'] -= 1

                        if (diamond[2] == 75) and (score_agent >= 140) and (diccolor_number_copy_enemy['b'] < 4) and (
                                (score_enemy - array_distance_enemy[diamond[0]][diamond[1]]) >= 140):
                            diccolor_number_copy_enemy['b'] += 1
                            result_return = alph_beta_minmax(not is_max_turn,agentx, agenty, diamond[0], diamond[1],
                                                             alpha, beta, level + 1, remain_turn_agent,
                                                             remain_turn_enemy- array_distance_enemy[diamond[0]][diamond[1]], score_agent,
                                                             score_enemy+ 75 - array_distance_enemy[diamond[0]][diamond[1]], diccolor_number_copy_agent,
                                                             diccolor_number_copy_enemy)
                            diccolor_number_copy_enemy['b'] -= 1

                    best_value = max(best_value, result_return)
                    beta = max(beta, best_value)
                    if beta <= alpha:
                        return best_value
                    visited_diamond.pop(d, None)

            for hole in holelist:
                h = (hole[0], hole[1])
                visited_hole[(h[0], h[1], level)] = (True, level)
                current_hole = (h[0], h[1], 0)
                # distancehole = dijkstra(gridmap, height, width, enemyx, enemyy, h[0], h[1], score_enemy)

                if (array_distance_enemy[hole[0]][hole[1]] <= remain_turn_enemy) and (level + 1 <= depth):
                    value_hole = 0
                    for item_hole in holelist:
                        if item_hole != current_hole:
                            value_hole += alph_beta_minmax(not is_max_turn, agentx, agenty, item_hole[0], item_hole[1],
                                                           alpha, beta, level + 1, remain_turn_agent,
                                                           remain_turn_enemy - array_distance_enemy[hole[0]][hole[1]] - 1, score_agent,
                                                           score_enemy - array_distance_enemy[hole[0]][hole[1]] - 1, diccolor_number_copy_agent,
                                                           diccolor_number_copy_enemy)

                    result_return = (value_hole // (len(holelist) - 1))

                best_value = max(best_value, result_return)
                beta = max(beta, best_value)
                if beta <= alpha:
                    return best_value
                visited_hole.pop((h[0], h[1], level), None)


    diccolor_number_copy_agent=diccolornumberagent
    diccolor_number_copy_enemy=diccolornumberenemy
    alph_beta_minmax(True, agentx, agenty, enemyx, enemyy, float('-inf'), float('inf'), 0, turn_agent,turn_enemy, scoreagent, scoreenemy, diccolor_number_copy_agent,diccolor_number_copy_enemy)
    return next_move
