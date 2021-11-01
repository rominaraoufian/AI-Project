from dijkstra_level1 import dijkstra

max_value = -1
next_move = tuple()

def dfs_depth_n(gridmap,height,width, turn, depth, agentx, agenty, diamondlist, holelist, score, diccolor_number):
   current_score = score
   global max_value
   global next_move
   next_move=tuple()
   max_value=-1
   # print(agentx,agenty,"pagentx,agenty")
   def dfs(visited_diamond, visited_hole, level, agentx, agenty, remain_turn, score_agent, diccolor_number_copy):
       global max_value
       global next_move

       ## attention to hloes  the value maybe change
       if level == depth:
           print("level == depth")
           print(diamondlist,"diamondlist")
           print(holelist,"holelist")
           ##get value range 0 to 1 or change percent
           value = ((20 * (score_agent - current_score)) + (80 * remain_turn)) // 100
           if value > max_value:
               max_value = value
               for keyvisited, valuevisited in visited_diamond.items():
                   if valuevisited[1] == 0:
                       next_move = keyvisited
               for keyvisited, valuevisited in visited_hole.items():
                   if valuevisited[1] == 0:
                       next_move = keyvisited
           # print(value, 'value')
           # print(visited_diamond,"visitdimond")
           # print(visited_hole, "visitedhole")
           # print(remain_turn, "remain_turn")
           # print(max_value, "max_value")
           # return value

       if remain_turn == 0:
           print("remain_turn == 0")
           print(diamondlist, "diamondlist")
           print(holelist, "holelist")
           value = (20 * (score_agent - current_score) + (80 * remain_turn)) // 100
           if value > max_value:
               max_value = value
               for keyvisited, valuevisited in visited_diamond.items():
                   if valuevisited[1] == 0:
                       next_move = keyvisited

               for keyvisited, valuevisited in visited_hole.items():
                   if valuevisited[1] == 0:
                       next_move = keyvisited

               for keyvisited, valuevisited in visited_hole.items():
                   if valuevisited[1] == 0:
                       next_move = keyvisited
           return value

       result_return = 0
       max_return_result = 0

       for diamond in diamondlist:

           d = (diamond[0], diamond[1])
           if d not in visited_diamond:

               visited_diamond[d] = (True, level)
               distance = dijkstra(gridmap, height, width, agentx, agenty, diamond[0], diamond[1])
               # print(agentx,agenty,"agentx,agenty")
               # print(diamond[0],diamond[1],"d[0],d[1]")
               # print(distance,"distance")
               # print(height,"h")
               # print(width,"w")
               if (distance <= remain_turn) and (level+1 <= depth):

                   if (diamond[2] == 10) and (diccolor_number_copy['y'] < 15) and ((score_agent-distance) >= 0):

                       # print("im in yellow")
                       # print(score_agent, "score_agent")
                       diccolor_number_copy['y'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level+1, diamond[0], diamond[1], remain_turn - distance, score_agent + 10 - distance, diccolor_number_copy)
                       diccolor_number_copy['y'] -= 1
                   if (diamond[2] == 25) and (score_agent >= 15) and (diccolor_number_copy['g'] < 8) and ((score_agent - distance) >= 15):

                       # print("im in green")
                       # print(score_agent, "score_agent")
                       diccolor_number_copy['g'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent + 25 - distance, diccolor_number_copy)
                       diccolor_number_copy['g'] -= 1
                   if (diamond[2] == 35) and (score_agent >= 50) and (diccolor_number_copy['r'] < 5) and ((score_agent - distance) >= 50):
                       # print("im in red")
                       # print(score_agent,"score_agent")
                       diccolor_number_copy['r'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent + 35 - distance, diccolor_number_copy)
                       diccolor_number_copy['r'] -= 1
                   if (diamond[2] == 75) and (score_agent >= 140) and (diccolor_number_copy['b'] < 4) and ((score_agent - distance) >= 140):
                       # print("im in blue")
                       # print(score_agent, "score_agent")
                       diccolor_number_copy['b'] +=1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent + 75 - distance, diccolor_number_copy)
                       diccolor_number_copy['b'] -= 1
               if max_return_result < result_return:
                   max_return_result = result_return
               visited_diamond.pop(d, None)

       print(holelist,"holelist")
       for hole in holelist:
           h = (hole[0], hole[1])
           if (h[0] != agentx) and (h[1] != agenty):
               visited_hole[h] = (True, level) ## just for level we do not need to visit holes
               current_hole=(h[0],h[1],0)
               next_step=(agentx,agenty,0)
               if next_step in holelist:
                   distancehole =0
               else:
                 distancehole = dijkstra(gridmap,height, width, agentx, agenty, h[0], h[1])
               print(distancehole,"distancehole")
               print(h[0],h[1],"h[0],h[1]")
               print(agentx,agenty,"agentx,agenty")
               if (distancehole <= remain_turn) and (level + 1 <= depth):
                    value_hole = 0
                    for item_hole in holelist:
                        if item_hole != current_hole:
                            ## remain_turn-distancehole-1 because hole do not have distance
                            value_hole += dfs(visited_diamond, visited_hole, level+1, h[0], h[1], remain_turn-distancehole-1, score_agent - distancehole-1, diccolor_number_copy)
                    result_return = (value_hole//(len(holelist)-1))
                    print("avg value for hole")
                    print(result_return,"hole result")
                    print(holelist)
                    if max_return_result < result_return:
                        max_return_result = result_return
               visited_hole.pop(h, None)

       ## return for middel nodes max value in middel node

       return max_return_result


   visited_diamond = {}
   visited_hole = {}
   ##not visit start agent
   diccolor_number_copy = diccolor_number.copy()
   dfs(visited_diamond, visited_hole, 0, agentx, agenty, turn,score,diccolor_number_copy)

   # print(next_move,"nextmove")

   return next_move