from dijkstra_level1 import dijkstra


def dfs_depth_n(map,height,width, turn, depth, agentx, agenty, diamondlist, holelist, score, diccolor_number):
   current_score = score
   max_value = -1
   next_move = tuple()


   def dfs(visited_diamond, visited_hole, level, agentx, agenty, remain_turn, score_agent, diccolor_number_copy):
       global max_value
       global next_move
       global current_score
       ## attention to hloes  the value maybe change
       if level == depth:
           ##get value range 0 to 1 or change percent
           value = (60 * (score_agent - current_score) + (40 * remain_turn)) // 100
           if value > max_value:
               max_value = value
               for keyvisited, valuevisited in visited_diamond.items():
                   if valuevisited[1] == 1:
                       next_move = keyvisited
               for keyvisited, valuevisited in visited_hole.items():
                   if valuevisited[1] == 1:
                       next_move = keyvisited
           return value

       if remain_turn == 0:
           value = (60 * (score_agent - current_score) + (40 * remain_turn)) // 100
           if value > max_value:
               max_value = value
               for keyvisited, valuevisited in visited_diamond.items():
                   if valuevisited[1] == 1:
                       next_move = keyvisited
               for keyvisited, valuevisited in visited_hole.items():
                   if valuevisited[1] == 1:
                       next_move = keyvisited
           return value

       result_return = 0
       max_return_result=0
       for diamond in diamondlist:
           d = (diamond[0], diamond[1])
           if d not in visited_diamond:
               visited_diamond[d] = (True, level)
               distance = dijkstra(map,height, width, agentx, agenty, diamond[0], diamond[1])
               if (distance <= remain_turn) and (level+1 <= depth):
                   if diamond[3] == 10 and diccolor_number_copy['y'] < 15:
                       diccolor_number_copy['y'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level+1, diamond[0], diamond[1], remain_turn-distance, score_agent + 10, diccolor_number_copy)
                   if diamond[3] == 25 and score_agent >= 15 and diccolor_number_copy['g'] < 8:
                       diccolor_number_copy['g'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent+25, diccolor_number_copy)
                   if diamond[3] == 35 and score_agent >= 50 and diccolor_number_copy['r'] < 5:
                       diccolor_number_copy['r'] += 1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent+35, diccolor_number_copy)
                   if diamond[3] == 75 and score_agent >= 140 and diccolor_number_copy['b'] <4:
                       diccolor_number_copy['b'] +=1
                       result_return = dfs(visited_diamond, visited_hole, level + 1, diamond[0], diamond[1], remain_turn - distance, score_agent+75, diccolor_number_copy)
               if max_return_result < result_return:
                   max_return_result=result_return
               visited_diamond.pop(d, None)

       for hole in holelist:
           h=(hole[0],hole[1])
           visited_hole[h]=(True,level) ## just for level we do not need to visit holes
           distancehole = dijkstra(map,height, width, agentx, agenty, h[0], h[1])
           if (distancehole <= remain_turn) and (level + 1 <= depth):
                value_hole =0
                for item_hole in holelist:
                    if item_hole != h:
                        value_hole += dfs(visited_diamond,visited_hole,level+1,h[0],h[1],remain_turn-distancehole,score_agent,diccolor_number_copy)

                result_return = (value_hole//(len(holelist)-1))
                if max_return_result < result_return:
                    max_return_result = result_return
           visited_hole.pop(h,None)

       ## return for middel nodes max value in middel node
       return max_return_result


   visited_diamond = {}
   visited_hole = {}
   ##not visit start agent
   diccolor_number_copy=diccolor_number
   dfs(visited_diamond, visited_hole, 0, agentx, agenty, turn,score,diccolor_number_copy)
   return next_move