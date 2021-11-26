from dijkstraforAll import  dijkstraforall
from dijkstra_level2 import dijkstrawayenemy
from math import inf
def hitortrap(gridmap, height, width, next_move_enemy, score_agent, score_enemy,maxvalue,start_agent, start_enemy, agentturn, enemyturn, agent_trap, enemy_trap, character, character_enemy,diccolornumber_agent, diccolornumber_enemy, trapno):
   maxvaluefortrap = float('-inf')
   nextmove = tuple()
   if next_move_enemy != ():
       dicforall, distancediamond, distancehole = dijkstraforall(gridmap,height, width, start_agent[0],start_agent[1], score_agent,score_enemy,enemy_trap,character,character_enemy,diccolornumber_agent)
       enemyway = dijkstrawayenemy(start_enemy[0], start_enemy[1], next_move_enemy[0], next_move_enemy[1], gridmap, height, width,score_enemy,character_enemy,diccolornumber_enemy, agent_trap, character, score_agent)
       value = float('-inf')
       trapcount = len(agent_trap) + 1
       leastscore = 35 * (len(agent_trap) + 1)
       flagtrap = False
       if score_agent >= trapcount * 35 and trapcount <= trapno:
            flagtrap = True
       while not enemyway.empty():
           place = enemyway.get()
           if place == ():
               continue
           if dicforall[place[0]][place[1]] == inf:
               #check this if later
               return (), -inf
           place_togo = dicforall[place[0]][place[1]][0]
           flagE = True if gridmap[place[0]][place[1]] == 'E' else False
           flagagent = True if gridmap[place[0]][place[1]] == ('E'+ character) else False
           flagenemy = True if gridmap[place[0]][place[1]] == ('E'+ character_enemy) else False
           if ((place_togo + 2) <= place[2]) and flagtrap and (flagE or flagagent):
                   value = ((40 - 3/2*(place_togo + 2)) * 40) // 100
                   if value >= maxvaluefortrap:
                       print("i choose trap0.............")
                       maxvaluefortrap = value
                       nextmove = (place[0], place[1])

           elif (place_togo) <= place[2] and score_agent > score_enemy and (flagE or flagagent):
               value = ((20 - 3/2*(place_togo )) * 40) // 100
               if value >= maxvaluefortrap:
                   print("i choose trap0.............")
                   maxvaluefortrap = value
                   nextmove = (place[0], place[1])
           elif place_togo == place[2] and score_agent >= score_enemy and flagenemy:
               value = ((20 - 3/2*(place_togo)) * 40) // 100
               if value >= maxvaluefortrap:
                   print("i choose trap0.............")
                   maxvaluefortrap = value
                   nextmove = (place[0], place[1])


   return nextmove, maxvaluefortrap