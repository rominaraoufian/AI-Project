from dijkstra_level2 import dijkstrawayenemy
from dijkstraforAll import dijkstraforall
from dijkstra_level1 import dijkstra
from queue import LifoQueue
from math import inf
#maybe we can check collision here
#should change value


def trapornot(gridmap, height, width, next_move_agent, next_move_enemy, maxvalue, score_agent, score_enemy, start_agent, start_enemy, leastscore, diccolornumber_agent, diccolornumber_enemy, agent_trap, enemy_trap, character, character_enemy):

    # print("im wanna fill enemy way")
    print(start_agent , " im start agent in trap or not")
    print(start_enemy , " im start enemy in trap or not")
    dicforall, dicfordiamond, dicforhole = dijkstraforall(gridmap, height, width, start_agent[0], start_agent[1], score_agent, score_enemy, enemy_trap, character,character_enemy, diccolornumber_agent)
    distance=float('inf')
    if next_move_enemy == () and next_move_agent != ():
        if gridmap[next_move_agent[0]][next_move_agent[1]] == '1' and diccolornumber_enemy['y'] < 15:
           distance,scorenemy = dijkstra(gridmap, height, width, start_enemy[0], start_enemy[1], next_move_agent[0], next_move_agent[1], score_enemy,score_agent,agent_trap,character_enemy,character,diccolornumber_enemy)

        if gridmap[next_move_agent[0]][next_move_agent[1]] == '2' and diccolornumber_enemy['g'] < 8 and score_enemy >= 15:
            distance, scorenemy = dijkstra(gridmap, height, width, start_enemy[0], start_enemy[1], next_move_agent[0],next_move_agent[1], score_enemy, score_agent, agent_trap, character_enemy, character, diccolornumber_enemy)

        if gridmap[next_move_agent[0]][next_move_agent[1]] == '3' and diccolornumber_enemy['r'] < 5 and score_enemy >= 50:
            distance, scorenemy = dijkstra(gridmap, height, width, start_enemy[0], start_enemy[1], next_move_agent[0],  next_move_agent[1], score_enemy, score_agent, agent_trap, character_enemy, character, diccolornumber_enemy)

        if gridmap[next_move_agent[0]][next_move_agent[1]] == '4' and diccolornumber_enemy['b'] < 4 and score_enemy >= 140:
            distance, scorenemy = dijkstra(gridmap, height, width, start_enemy[0], start_enemy[1], next_move_agent[0],next_move_agent[1], score_enemy, score_agent, agent_trap, character_enemy,character, diccolornumber_enemy)

        #check for hole
        if distance > dicforall[next_move_agent[0]][next_move_agent[1]][0]:
            next_move_enemy = next_move_agent

    if next_move_enemy == ():
        return (),float('-inf')

    enemyway = dijkstrawayenemy(start_enemy[0], start_enemy[1], next_move_enemy[0], next_move_enemy[1], gridmap, height, width, score_enemy, character_enemy, diccolornumber_enemy, agent_trap, character, score_agent)
    print("im in enemyway" , "*" * 20)
    #enemyway1 = dijkstraforall(gridmap, height, width, start_enemy[0], start_enemy[1], score_enemy, score_agent, agent_trap, character, character_enemy, diccolornumber_agent)
    print(next_move_enemy,"nextmoveenemy",'$'*10)
    print(next_move_agent,"nextmoveagent",'$'*10)

    maxvaluefortrap = float('-inf')
    nextmove = tuple()
    #print(enemyway, " enemyway")
    while not enemyway.empty():
        place = enemyway.get()
        print(place , "*" * 20)

        if place == ():
            continue
        if dicforall[place[0]][place[1]] == inf:
            continue
        place_togo = dicforall[place[0]][place[1]][0]
        print(place_togo,"placetogo")
        if gridmap[place[0]][place[1]] == 'E' or gridmap[place[0]][place[1]] == 'E' + character:
            if ((((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy)or (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy)) and ((score_agent-(place_togo+1)) >= leastscore):

                if (((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy):
                     value = ((40 - (place_togo + 2)) * 40) // 100
                if (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy):
                    value = ((40 - (place_togo + 1)) * 40) // 100
                print(value, "valuetrape", '~' * 40)
                if value >= maxvaluefortrap:
                    print("i choose trap0.............")
                    maxvaluefortrap = value
                    nextmove = (place[0],place[1])
        if (gridmap[place[0]][place[1]] == '1') and (diccolornumber_agent['y'] < 15) and (place[0] != next_move_enemy[0]) and (place[1] != next_move_enemy[1]):

            if((((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy)or (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy)) and (((score_agent + 10) - (place_togo + 1)) >= leastscore):
                if (((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy):
                    value = (((40 - (place_togo + 2)) * 40) // 100 + 10)
                if (((place_togo + 1) <= place[2]) and score_agent - 1 > score_enemy):
                    value = (((40 - (place_togo + 1)) * 40) // 100 + 10)

                print(value, "valuetrap1", '~' * 40)
                if value > maxvaluefortrap:
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
                    print("i choose trap1.............")
        if (gridmap[place[0]][place[1]] == '2') and (diccolornumber_agent['g'] < 8) and (score_agent - place_togo >= 15) and (
                place[0] != next_move_enemy[0]) and (place[1] != next_move_enemy[1]):
            if ((((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy)or (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy)) and (((score_agent + 25) - (place_togo+ 1)) >= leastscore):
                if (((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy):
                    value = (((40 - (place_togo + 2)) * 40) // 100 + 25)
                if (((place_togo + 1) <= place[2]) and score_agent - 1 > score_enemy):
                    value = (((40 - (place_togo + 1)) * 40) // 100 + 25)
                print(value, "valuetrap2", '~' * 40)
                if value > maxvaluefortrap:
                    print("i choose trap2.............")
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])

                    # print(nextmove, "nextmovetrap")
                print(value, "value for g")
        if (gridmap[place[0]][place[1]] == '3') and (diccolornumber_agent['r'] < 5) and (score_agent - place_togo >= 50) and (
                place[0] != next_move_enemy[0]) and (place[1] != next_move_enemy[1]):

            if ((((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy)or (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy)) and (((score_agent + 35) - (place_togo + 1)) >= leastscore):
                if (((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy):
                    value = (((40 - (place_togo + 2)) * 40) // 100 + 35)
                if (((place_togo + 1) <= place[2]) and score_agent - 1 > score_enemy):
                    value = (((40 - (place_togo + 1)) * 40) // 100 + 35)
                print(value, "valuetrap3", '~' * 40)
                if value > maxvaluefortrap:
                    print("i choose trap3.............")
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])
        # print(nextmove, "nextmovetrap")
                print(value, "value for r")
        if (gridmap[place[0]][place[1]] == '4') and (diccolornumber_agent['b'] < 4) and (score_agent - place_togo >= 140) and (
                place[0] != next_move_enemy[0]) and (place[1] != next_move_enemy[1]):
            if ((((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy)or (((place_togo + 1) <= place[2]) and score_agent-1 > score_enemy)) and (
                    ((score_agent + 75) - (place_togo + 1)) >= leastscore):

                print("im in trap four")
                if (((place_togo + 2) <= place[2]) and score_agent-1 <= score_enemy):
                    value = (((40 - (place_togo + 2)) * 40) // 100 + 75)
                if (((place_togo + 1) <= place[2]) and score_agent - 1 > score_enemy):
                    value = (((40 - (place_togo + 1)) * 40) // 100 + 75)
                    print(value,"valuetrap4",'~'*40)
                if value > maxvaluefortrap:
                    print("i choose trap4.............")
                    maxvaluefortrap = value
                    nextmove = (place[0], place[1])

    print(start_agent , "start agent")
    print(nextmove,"nextmove trap")
    print(maxvaluefortrap, "maxvaluefortrap")
    return nextmove, maxvaluefortrap
