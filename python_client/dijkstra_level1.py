from queue import PriorityQueue
def dijkstra(map,height, width, agentx,agenty,goalx,goaly):

  visited = {}
  distancelist = {}
  pq = PriorityQueue()
  pq.put((0,agentx, agenty))
  distancelist[(agentx, agenty)] = 0
  while not pq.empty():
      temp = pq.get()
      dist = temp[0]
      current_nodex = temp[1]
      current_nodey = temp[2]
      visited[(current_nodex,current_nodey)] = True
      # print(dist,current_nodex,current_nodey)
      if current_nodex == goalx and current_nodey == goaly:
          return dist
      #up
      if (current_nodex-1 >= 0) and ((current_nodex-1,current_nodey) not in visited) and (
         (map[current_nodex-1][current_nodey] == 'E') or (map[current_nodex-1][current_nodey] == 'T')or(map[current_nodex-1][current_nodey]=="EA")or(
         (current_nodex-1==goalx) and (current_nodey==goaly))):

          if (current_nodex-1,current_nodey) not in distancelist:
              distancelist[(current_nodex-1,current_nodey)]=dist+1
              pq.put((dist+1, current_nodex-1,current_nodey))

          else:
              if dist + 1 < distancelist[(current_nodex-1,current_nodey)]:
                  distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex - 1, current_nodey))
      #down

      if (current_nodex+1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (
         (map[current_nodex + 1][current_nodey] == 'E') or (map[current_nodex + 1][current_nodey] == 'T')or(map[current_nodex+1][current_nodey]=="EA")or(
         (current_nodex + 1 == goalx) and (current_nodey == goaly))):


          if (current_nodex + 1, current_nodey) not in distancelist:
              distancelist[(current_nodex + 1, current_nodey)]=dist+1
              pq.put((dist + 1,current_nodex + 1, current_nodey))
          else:
              if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex + 1, current_nodey))
      #left
      if (current_nodey - 1 >= 0)  and ((current_nodex , current_nodey-1) not in visited) and (
         (map[current_nodex][current_nodey-1] == 'E') or (map[current_nodex][current_nodey-1] == 'T')or(map[current_nodex][current_nodey-1]=="EA")or(
         (current_nodex  == goalx) and (current_nodey-1 == goaly))):
          if (current_nodex, current_nodey-1) not in distancelist:
              distancelist[(current_nodex, current_nodey-1)]=dist+1
              pq.put((dist + 1, current_nodex , current_nodey-1))
          else:
              if dist + 1 < distancelist[(current_nodex , current_nodey-1)]:
                  distancelist[(current_nodex , current_nodey-1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey - 1))

      #right
      if (current_nodey + 1 < width) and ((current_nodex , current_nodey+1) not in visited) and (
         (map[current_nodex][current_nodey+1] == 'E') or (map[current_nodex][current_nodey+1] == 'T') or (map[current_nodex][current_nodey+1]=="EA")or(
         (current_nodex  == goalx) and (current_nodey+1 == goaly))):

          if (current_nodex, current_nodey+1) not in distancelist:
              distancelist[(current_nodex, current_nodey+1)]=dist+1
              pq.put((dist + 1, current_nodex, current_nodey+1))
          else:
              if dist + 1 < distancelist[(current_nodex , current_nodey+1)]:
                  distancelist[(current_nodex , current_nodey+1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey + 1))

