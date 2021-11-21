from json import dumps
import numpy as np
def hash_key(visiteddiamond,visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy):
    hash_visiteddiamond = dumps({dumps(i):visiteddiamond[i] for i in sorted(visiteddiamond)})
    hash_visitedhole = dumps({dumps(i): visitedhole[i] for i in sorted(visitedhole)})
    hash_key_list=[hash_visiteddiamond,hash_visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy]
    return  tuple(hash_key_list)


def sortmoves(dijkstradic,remain_turn):

    scores = {}
    move_list = []
    # maybe sort all values are better
    dijkstradic_copy = dijkstradic.copy()

    for item in dijkstradic:
        value = (20 * (dijkstradic[item][1]+item[2]) + 80 * (remain_turn - dijkstradic[item][0])) / 100
        scores[item] = value
        print(item,value,"scorevale")
    print(len(scores),"sizescores")
    for i in range(min(6, len(scores))):
         max = float('-inf')
         maxlocation = tuple()
         for j in scores:
             if scores[j] > max:
                 #print(j, " j ", scores[j], " scores j")
                 max = scores[j]
                 maxlocation = j

         move_list.append(maxlocation)
         dijkstradic_copy.pop(maxlocation)
        # print(maxlocation, " max_location")
         scores[maxlocation] = float('-inf')
    print(dijkstradic,"dijkstradic")
    move_list.extend(list(dijkstradic_copy.keys()))
    return move_list




