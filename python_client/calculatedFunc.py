from json import dumps
import numpy as np
def hash_key(visiteddiamond,visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy):
    hash_visiteddiamond = dumps({dumps(i):visiteddiamond[i] for i in sorted(visiteddiamond)})
    hash_visitedhole = dumps({dumps(i): visitedhole[i] for i in sorted(visitedhole)})
    hash_key_list=[hash_visiteddiamond,hash_visitedhole,agentx,agenty,enemyx,enemyy,remain_turn_agent,remain_turn_enemy,score_agent,score_enemy]
    return  tuple(hash_key_list)


def sortmoves(dijkstradic, movesnp):

    scores = {}
    move_list = []

    # maybe sort all values are better
    for item in movesnp:
        d=(item[0], item[1])
        if (d not in dijkstradic):
            calculatedistance = float('-inf')
        else:
            calculatedistance = dijkstradic[d][0]
        value = (20 * item[2] + 80 * calculatedistance) / 100
        scores[(item[0],item[1],item[2])] = value

    for i in range(min(6, len(scores))):
         max = float('-inf')
         maxlocation = float('-inf')
         for j in scores:
             if scores[j] > max:
                 max = scores[j]
                 maxlocation = j

         move_list.append(maxlocation)
         scores[maxlocation] = float('-inf')
         movesnp = np.delete(movesnp, np.where(movesnp == maxlocation),axis=0)
         movesnp = movesnp.reshape(np.size(movesnp) // 3, 3)


    move_listnp=np.array(move_list)

    return np.concatenate((move_listnp,movesnp), axis=0)
