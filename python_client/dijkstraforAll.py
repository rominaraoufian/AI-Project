from queue import PriorityQueue
from math import inf


def dijkstraforall(gridmap,height, width, agentx,agenty, scoredij,trap,character,diccolornumber):

  # array_distance = [[inf]*width]*height
  array_distance= [[(inf,inf) for i in range(width)] for j in range(height)]

  dicdistance_diamond = {}
  dicdistance_hole = {}
  visited = {}
  distancelist = {}
  pq = PriorityQueue()
  pq.put((0, agentx, agenty,0, scoredij))
  distancelist[(agentx, agenty)] = 0
  array_distance[agentx][agenty] = (0,scoredij)
  flag = False
  while not pq.empty():

      temp = pq.get()
      dist = temp[0]
      current_nodex = temp[1]
      current_nodey = temp[2]
      scoredij = temp[4]
      actual_dist = temp[3]
      visited[(current_nodex, current_nodey)] = True
      if gridmap[current_nodex][current_nodey] == 'T' or gridmap[current_nodex][current_nodey] == 'T' + character:
          dicdistance_hole[(current_nodex,current_nodey,0)] = (actual_dist, scoredij)
      if gridmap[current_nodex][current_nodey] == '1':
          dicdistance_diamond[(current_nodex, current_nodey,10)] = (actual_dist, scoredij)
      if gridmap[current_nodex][current_nodey] == '2':
          dicdistance_diamond[(current_nodex, current_nodey, 25)] = (actual_dist, scoredij)
      if gridmap[current_nodex][current_nodey] == '3':
         dicdistance_diamond[(current_nodex, current_nodey, 35)] = (actual_dist, scoredij)
      if gridmap[current_nodex][current_nodey] == '4':
        dicdistance_diamond[(current_nodex, current_nodey, 75)] = (actual_dist, scoredij)
     # print(dist,current_nodex,current_nodey)
     #  print(array_distance[current_nodex][current_nodey],"array_distance[current_nodex][current_nodey]")
     #  print(current_nodex,current_nodey ,"current_nodex , current_nodey")
      array_distance[current_nodex][current_nodey] = (actual_dist, scoredij)

      if (gridmap[current_nodex][current_nodey] == '1'and (not(diccolornumber['y'] == 15))) or (
              gridmap[current_nodex][current_nodey] == '2' and (not((scoredij-1 < 15 or diccolornumber['g'] == 8))))or (gridmap[current_nodex][current_nodey] == '3' and (not (scoredij-1 < 50 or diccolornumber['r']==5))) or (
              gridmap[current_nodex][current_nodey] == '4' and (not((scoredij-1 < 140 or diccolornumber['b'] == 4)))):

          continue
      #up

      flag = False
      if (current_nodex-1 >= 0):
          if (current_nodex-1, current_nodey) in trap:
            flag = True
      if (current_nodex-1 >= 0) and ((current_nodex-1,current_nodey) not in visited) and (
         (gridmap[current_nodex-1][current_nodey] == 'E') or (gridmap[current_nodex-1][current_nodey] == 'T')or(gridmap[current_nodex-1][current_nodey]=="E"+character) or(gridmap[current_nodex-1][current_nodey]=="T"+character) or flag or(
         (gridmap[current_nodex-1][current_nodey] == '1') or (gridmap[current_nodex-1][current_nodey] == '2') or (gridmap[current_nodex-1][current_nodey] == '3') or (gridmap[current_nodex-1][current_nodey] == '4'))):

          # print("im in up")
          if (current_nodex-1, current_nodey) not in distancelist:
              if flag:
                distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                pq.put((dist+41, current_nodex-1, current_nodey, actual_dist+1, scoredij-41))
              else:
                  distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex - 1, current_nodey, actual_dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex-1, current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex - 1, current_nodey, actual_dist+1, scoredij-41))
              else:
                  if dist + 1 < distancelist[(current_nodex-1,current_nodey)]:
                      distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex - 1, current_nodey, actual_dist+1, scoredij-1))
      #down

      flag = False
      if (current_nodex+1 < height):
          if (current_nodex + 1, current_nodey) in trap:
              flag = True
      if (current_nodex+1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (
         (gridmap[current_nodex + 1][current_nodey] == 'E') or (gridmap[current_nodex + 1][current_nodey] == 'T')or(gridmap[current_nodex+1][current_nodey]=="E"+character) or(gridmap[current_nodex+1][current_nodey]=="T"+character) or flag
         or ((gridmap[current_nodex + 1][current_nodey] == '1') or (gridmap[current_nodex + 1][current_nodey] == '2') or (
                 gridmap[current_nodex + 1][current_nodey] == '3') or (gridmap[current_nodex + 1][current_nodey] == '4'))):

          # print("im in down")
          if (current_nodex + 1, current_nodey) not in distancelist:
              if flag:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                  pq.put((dist + 41, current_nodex + 1, current_nodey, actual_dist+1, scoredij - 41))
              else:
                  distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                  pq.put((dist + 1, current_nodex + 1, current_nodey, actual_dist+1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                      pq.put((dist + 41, current_nodex + 1, current_nodey, actual_dist+1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                      distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                      pq.put((dist + 1, current_nodex + 1, current_nodey, actual_dist+1, scoredij - 1))
      #left

      flag = False
      if(current_nodey - 1 >= 0):
          if (current_nodex,current_nodey-1) in trap:
              flag = True
      if (current_nodey - 1 >= 0) and ((current_nodex , current_nodey-1) not in visited) and (
         (gridmap[current_nodex][current_nodey-1] == 'E') or (gridmap[current_nodex][current_nodey-1] == 'T')or(gridmap[current_nodex][current_nodey-1]=="E"+character) or (gridmap[current_nodex][current_nodey-1]=="T"+character)
              or flag or((gridmap[current_nodex][current_nodey-1] == '1') or (gridmap[current_nodex][current_nodey-1] == '2') or (gridmap[current_nodex][current_nodey-1] == '3') or (gridmap[current_nodex][current_nodey-1] == '4'))):
          # print("im in left")
          if (current_nodex , current_nodey-1) not in distancelist:
              if flag:
                  distancelist[(current_nodex , current_nodey-1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey-1, actual_dist+1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey-1)] = dist + 1
                  pq.put((dist + 1, current_nodex , current_nodey-1, actual_dist+1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 41
                      pq.put((dist + 41, current_nodex , current_nodey-1, actual_dist+1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex , current_nodey-1)]:
                      distancelist[(current_nodex , current_nodey-1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey-1, actual_dist+1, scoredij - 1))
      #right
      flag = False
      if current_nodey + 1 < width:
          if (current_nodex , current_nodey+1) in trap:
              flag = True
      if (current_nodey + 1 < width) and ((current_nodex, current_nodey+1) not in visited) and (
         (gridmap[current_nodex][current_nodey+1] == 'E') or (gridmap[current_nodex][current_nodey+1] == 'T') or (gridmap[current_nodex][current_nodey+1]=="E"+character)or (gridmap[current_nodex][current_nodey+1]=="T"+character) or flag  or(
         (gridmap[current_nodex][current_nodey+1] == '1') or (gridmap[current_nodex][current_nodey+1] == '2') or (gridmap[current_nodex][current_nodey+1] == '3') or (gridmap[current_nodex][current_nodey+1] == '4'))):
          # print("im in right")
          if (current_nodex, current_nodey + 1) not in distancelist:
              if flag:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                  pq.put((dist + 41, current_nodex, current_nodey + 1, actual_dist + 1, scoredij - 41))
              else:
                  distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                  pq.put((dist + 1, current_nodex, current_nodey + 1, actual_dist + 1, scoredij - 1))

          else:
              if flag:
                  if dist + 41 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                      pq.put((dist + 41, current_nodex, current_nodey + 1, actual_dist + 1, scoredij - 41))
              else:
                  if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                      distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                      pq.put((dist + 1, current_nodex, current_nodey + 1, actual_dist + 1, scoredij - 1))

  # for item in array_distance:
  #     print(item)
  return (array_distance, dicdistance_diamond,dicdistance_hole)