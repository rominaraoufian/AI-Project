from queue import PriorityQueue
from math import inf
def dijkstra(gridmap,height, width, agentx,agenty,goalx,goaly, scoredij):

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
         (gridmap[current_nodex-1][current_nodey] == 'E') or (gridmap[current_nodex-1][current_nodey] == 'T')or(gridmap[current_nodex-1][current_nodey]=="EA") or(gridmap[current_nodex-1][current_nodey]=="EA")or(
         (current_nodex-1==goalx) and (current_nodey==goaly)) or (gridmap[current_nodex-1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex-1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex-1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex-1][current_nodey] == '4' and scoredij-1 < 140)):

          if (current_nodex-1,current_nodey) not in distancelist:
              distancelist[(current_nodex-1,current_nodey)]=dist+1
              pq.put((dist+1, current_nodex-1,current_nodey))

          else:
              if dist + 1 < distancelist[(current_nodex-1,current_nodey)]:
                  distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex - 1, current_nodey))
      #down

      if (current_nodex+1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (
         (gridmap[current_nodex + 1][current_nodey] == 'E') or (gridmap[current_nodex + 1][current_nodey] == 'T')or(gridmap[current_nodex+1][current_nodey]=="EA") or(gridmap[current_nodex+1][current_nodey]=="EA")or(
         (current_nodex + 1 == goalx) and (current_nodey == goaly))  or (gridmap[current_nodex+1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex+1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex+1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex+1][current_nodey] == '4' and scoredij-1 < 140)):


          if (current_nodex + 1, current_nodey) not in distancelist:
              distancelist[(current_nodex + 1, current_nodey)]=dist+1
              pq.put((dist + 1,current_nodex + 1, current_nodey))
          else:
              if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex + 1, current_nodey))
      #left
      if (current_nodey - 1 >= 0)  and ((current_nodex , current_nodey-1) not in visited) and (
         (gridmap[current_nodex][current_nodey-1] == 'E') or (gridmap[current_nodex][current_nodey-1] == 'T')or(gridmap[current_nodex][current_nodey-1]=="EA") or (gridmap[current_nodex][current_nodey-1]=="EA")or(
         (current_nodex  == goalx) and (current_nodey-1 == goaly)) or (gridmap[current_nodex][current_nodey-1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey-1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey-1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey-1] == '4' and scoredij-1 < 140)):
          if (current_nodex, current_nodey-1) not in distancelist:
              distancelist[(current_nodex, current_nodey-1)]=dist+1
              pq.put((dist + 1, current_nodex , current_nodey-1))
          else:
              if dist + 1 < distancelist[(current_nodex , current_nodey-1)]:
                  distancelist[(current_nodex , current_nodey-1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey - 1))

      #right
      if (current_nodey + 1 < width) and ((current_nodex , current_nodey+1) not in visited) and (
         (gridmap[current_nodex][current_nodey+1] == 'E') or (gridmap[current_nodex][current_nodey+1] == 'T') or (gridmap[current_nodex][current_nodey+1]=="EA")or (gridmap[current_nodex][current_nodey+1]=="EA") or(
         (current_nodex  == goalx) and (current_nodey+1 == goaly)) or (gridmap[current_nodex][current_nodey+1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey+1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey+1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey +1] == '4' and scoredij-1 < 140)):

          if (current_nodex, current_nodey+1) not in distancelist:
              distancelist[(current_nodex, current_nodey+1)]=dist+1
              pq.put((dist + 1, current_nodex, current_nodey+1))
          else:
              if dist + 1 < distancelist[(current_nodex , current_nodey+1)]:
                  distancelist[(current_nodex , current_nodey+1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey + 1))
      scoredij -= 1
  return inf