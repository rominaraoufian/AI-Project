from json import dumps
import numpy as np
def hash_key(visiteddiamond,visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy):
    hash_visiteddiamond = dumps({dumps(i):visiteddiamond[i] for i in sorted(visiteddiamond)})
    hash_visitedhole = dumps({dumps(i): visitedhole[i] for i in sorted(visitedhole)})
    hash_key_list=[hash_visiteddiamond,hash_visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy]
    return  tuple(hash_key_list)


def sortmoves(dijkstradic, moves):

    scores = {}
    move_list = []

    # maybe sort all values are better
    for item in moves:
        d=(item[0], item[1])
        if (d not in dijkstradic):
            calculatedistance = float('-inf')
        else:
            calculatedistance = dijkstradic[d][0]
        value = (20 * item[2] + 80 * calculatedistance) / 100
        scores[(item[0],item[1],item[2])] = value
       # print((item[0],item[1],item[2]))
    print(len(scores))
    for i in range(min(6, len(scores))):
         max = float('-inf')
         maxlocation = tuple()
         for j in scores:
             if scores[j] > max:
                 #print(j, " j ", scores[j], " scores j")
                 max = scores[j]
                 maxlocation = j

         move_list.append(maxlocation)
        # print(maxlocation, " max_location")
         moves.pop(maxlocation)

         scores[maxlocation] = float('-inf')


    move_list.extend(moves.keys())
    return move_list



