from queue import PriorityQueue
from math import inf
import numpy as np

def dijkstra(gridmap,height, width, agentx,agenty, scoredij,traps):
  # array_distance_initial = np.empty(height*width)
  # array_distance_initial.fill(inf)
  # array_distance = array_distance_initial.reshape((height, width))  # ***
  array_distance = {}
  visited = {}
  distancelist = {}
  pq = PriorityQueue()
  pq.put((0, agentx, agenty,0, scoredij))
  distancelist[(agentx, agenty)] = 0
  array_distance[(agentx,agenty)] = (0,scoredij)
  flag = False
  while not pq.empty():
      temp = pq.get()
      dist = temp[0]
      current_nodex = temp[1]
      current_nodey = temp[2]
      scoredij = temp[4]
      actual_dist = temp[3]
      visited[(current_nodex,current_nodey)] = True
      # print(dist,current_nodex,current_nodey)
      array_distance[(current_nodex,current_nodey)] = (actual_dist, scoredij)
      #up
      flag = np.any(traps == gridmap[current_nodex-1][current_nodey])
      if (current_nodex-1 >= 0) and ((current_nodex-1,current_nodey) not in visited) and (
         (gridmap[current_nodex-1][current_nodey] == 'E') or (gridmap[current_nodex-1][current_nodey] == 'T')or(gridmap[current_nodex-1][current_nodey]=="EA") or(gridmap[current_nodex-1][current_nodey]=="TA") or (gridmap[current_nodex-1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex-1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex-1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex-1][current_nodey] == '4' and scoredij-1 < 140) or flag):

          if (current_nodex-1, current_nodey) not in distancelist:
              if flag:
                distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                pq.put((dist+41, current_nodex-1, current_nodey, dist+1, scoredij-41))
              else:
                  distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex - 1, current_nodey, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex-1,current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex - 1, current_nodey, dist+1, scoredij-41))
              else:
                  if dist + 1 < distancelist[(current_nodex-1,current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex - 1, current_nodey, dist+1, scoredij-1))
      #down
      flag = np.any(traps == gridmap[current_nodex+1][current_nodey])
      if (current_nodex+1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (
         (gridmap[current_nodex + 1][current_nodey] == 'E') or (gridmap[current_nodex + 1][current_nodey] == 'T')or(gridmap[current_nodex+1][current_nodey]=="EA") or(gridmap[current_nodex+1][current_nodey]=="TA")or (gridmap[current_nodex+1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex+1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex+1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex+1][current_nodey] == '4' and scoredij-1 < 140) or flag):

          if (current_nodex + 1, current_nodey) not in distancelist:
              if flag:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                  pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))
      #left
      flag = np.any(traps == gridmap[current_nodex][current_nodey-1])
      if (current_nodey - 1 >= 0) and ((current_nodex , current_nodey-1) not in visited) and (
         (gridmap[current_nodex][current_nodey-1] == 'E') or (gridmap[current_nodex][current_nodey-1] == 'T')or(gridmap[current_nodex][current_nodey-1]=="EA") or (gridmap[current_nodex][current_nodey-1]=="TA") or (gridmap[current_nodex][current_nodey-1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey-1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey-1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey-1] == '4' and scoredij-1 < 140) or flag):
          if (current_nodex , current_nodey-1) not in distancelist:
              if flag:
                  distancelist[(current_nodex , current_nodey-1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey-1, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey-1)] = dist + 1
                  pq.put((dist + 1, current_nodex , current_nodey-1, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 41
                      pq.put((dist + 41, current_nodex , current_nodey-1, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex , current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey-1, dist + 1, scoredij - 1))
      #right
      flag = np.any(traps == gridmap[current_nodex][current_nodey + 1])
      if (current_nodey + 1 < width) and ((current_nodex, current_nodey+1) not in visited) and (
         (gridmap[current_nodex][current_nodey+1] == 'E') or (gridmap[current_nodex][current_nodey+1] == 'T') or (gridmap[current_nodex][current_nodey+1]=="EA")or (gridmap[current_nodex][current_nodey+1]=="TA")  or (gridmap[current_nodex][current_nodey+1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey+1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey+1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey +1] == '4' and scoredij-1 < 140) or flag):

          if (current_nodex, current_nodey + 1) not in distancelist:
              if flag:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                      pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))

  return array_distance