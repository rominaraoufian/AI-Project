from queue import PriorityQueue,  LifoQueue
import numpy as np

def dij_show_way(agentx, agenty, goalx, goaly, gridmap, height, width,scoredij):
        visited = {}
        distancelist = {}
        parent = {}
        way = LifoQueue()
        parent[(agentx, agenty)] = (-1,-1,'')
        pq = PriorityQueue()
        pq.put((0, (agentx, agenty)))
        distancelist[(agentx, agenty)] = 0
        if agentx == goalx and agenty == goaly:
            way.put('t')
            return way

        while not pq.empty():
            temp = pq.get()
            dist = temp[0]
            current_nodex = temp[1][0]
            current_nodey = temp[1][1]
            visited[(current_nodex, current_nodey)] = True
            if gridmap[agentx][agenty] == 'TA' and gridmap[goalx][goaly] == 'T':
                way.put('t')
                return way
            if current_nodex == goalx and current_nodey == goaly:
                x = current_nodex
                y = current_nodey
                if gridmap[x][y] == 'T':
                    way.put('t')
                while ((parent[(x, y)][0] != -1) and (parent[(x, y)][1] != -1) and (parent[(x, y)][2] != '')):
                    way.put(parent[(x, y)][2])
                    currentx = parent[(x, y)][0]
                    currenty = parent[(x, y)][1]
                    x = currentx
                    y = currenty
                return way
            # up
            if (current_nodex - 1 >= 0) and ((current_nodex - 1, current_nodey) not in visited) and (
               (gridmap[current_nodex - 1][current_nodey] == 'E') or (gridmap[current_nodex - 1][current_nodey] == 'T')or(gridmap[current_nodex-1][current_nodey]=="EA") or (gridmap[current_nodex-1][current_nodey]=="TA")or(
               (current_nodex - 1 == goalx) and (current_nodey == goaly)) or (gridmap[current_nodex-1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex-1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex-1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex-1][current_nodey] == '4' and scoredij-1 < 140)):

                if (current_nodex - 1, current_nodey) not in distancelist:
                    distancelist[(current_nodex - 1, current_nodey)]=dist+1
                    pq.put((dist + 1, (current_nodex - 1, current_nodey)))
                    parent[(current_nodex-1, current_nodey)] = (current_nodex, current_nodey, 'u')
                else:
                    if dist + 1 < distancelist[(current_nodex - 1, current_nodey)]:
                        distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, (current_nodex - 1, current_nodey)))
                        parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')
            # down
            if (current_nodex + 1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (

               (gridmap[current_nodex + 1][current_nodey] == 'E') or (gridmap[current_nodex + 1][current_nodey] == 'T')or(gridmap[current_nodex+1][current_nodey]=="EA") or (gridmap[current_nodex+1][current_nodey]=="TA")or(
               (current_nodex + 1 == goalx) and (current_nodey == goaly))or (gridmap[current_nodex+1][current_nodey] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex+1][current_nodey] == '2' and scoredij-1 < 15) or (gridmap[current_nodex+1][current_nodey] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex+1][current_nodey] == '4' and scoredij-1 < 140)):

                if (current_nodex + 1, current_nodey) not in distancelist:
                    distancelist[(current_nodex + 1, current_nodey)]=dist+1
                    pq.put((dist + 1, (current_nodex + 1, current_nodey)))
                    parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
                else:
                    if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                        distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, (current_nodex + 1, current_nodey)))
                        parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
            # left
            if (current_nodey - 1 >= 0) and ((current_nodex, current_nodey - 1) not in visited) and (

               (gridmap[current_nodex][current_nodey - 1] == 'E') or (gridmap[current_nodex][current_nodey - 1] == 'T')or(gridmap[current_nodex][current_nodey-1]=="EA") or (gridmap[current_nodex][current_nodey-1]=="TA")or (
               (current_nodex == goalx) and (current_nodey-1 == goaly))or (gridmap[current_nodex][current_nodey-1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey-1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey-1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey-1] == '4' and scoredij-1 < 140)):

                if (current_nodex, current_nodey - 1) not in distancelist:
                    distancelist[(current_nodex, current_nodey - 1)]=dist+1
                    pq.put((dist + 1, (current_nodex, current_nodey - 1)))
                    parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey - 1)]:
                        distancelist[(current_nodex, current_nodey - 1)] = dist + 1
                        pq.put((dist + 1, (current_nodex, current_nodey-1)))
                        parent[(current_nodex, current_nodey-1)] = (current_nodex, current_nodey, 'l')

            # right
            if (current_nodey + 1 < width) and ((current_nodex, current_nodey + 1) not in visited) and (
               (gridmap[current_nodex][current_nodey + 1] == 'E') or (gridmap[current_nodex][current_nodey + 1] == 'T') or(gridmap[current_nodex][current_nodey+1]=="EA")or (gridmap[current_nodex][current_nodey+1]=="TA") or(
               (current_nodex == goalx) and (current_nodey+1 == goaly)) or (gridmap[current_nodex][current_nodey+1] == '1' and scoredij-1 < 0) or (
              gridmap[current_nodex][current_nodey+1] == '2' and scoredij-1 < 15) or (gridmap[current_nodex][current_nodey+1] == '3' and scoredij-1 < 50 ) or (
              gridmap[current_nodex][current_nodey +1] == '4' and scoredij-1 < 140)):
                if (current_nodex, current_nodey + 1) not in distancelist:
                    distancelist[(current_nodex, current_nodey + 1)]=dist+1
                    pq.put((dist + 1, (current_nodex, current_nodey + 1)))
                    parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                        distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                        pq.put((dist + 1, (current_nodex, current_nodey + 1)))
                        parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')


            scoredij -= 1


def dij_show_action(agentx, agenty, goalx, goaly, gridmap, height, width,scoredij,traps):
    visited = {}
    distancelist = {}
    parent = {}
    way = LifoQueue()
    parent[(agentx, agenty)] = (-1, -1, '')
    pq = PriorityQueue()
    pq.put((0, agentx, agenty, 0, scoredij))

    distancelist[(agentx, agenty)] = 0
    #change for trap
    if agentx == goalx and agenty == goaly:
        # way.put('t')
        return 't'
    flag = False
    while not pq.empty():
        temp = pq.get()
        dist = temp[0]
        current_nodex = temp[1]
        current_nodey = temp[2]
        scoredij = temp[4]
        actual_dist = temp[3]
        visited[(current_nodex, current_nodey)] = True
        if gridmap[agentx][agenty] == 'TA' and gridmap[goalx][goaly] == 'T':
            # way.put('t')
            return 't'
        if current_nodex == goalx and current_nodey == goaly:
            x = current_nodex
            y = current_nodey
            if gridmap[x][y] == 'T':
                way.put('t')
            while ((parent[(x, y)][0] != -1) and (parent[(x, y)][1] != -1) and (parent[(x, y)][2] != '')):
                way.put(parent[(x, y)][2])
                currentx = parent[(x, y)][0]
                currenty = parent[(x, y)][1]
                x = currentx
                y = currenty
            return way.get()

        # up
        flag = np.any(traps == gridmap[current_nodex - 1][current_nodey])
        if (current_nodex - 1 >= 0) and ((current_nodex - 1, current_nodey) not in visited) and (
                (gridmap[current_nodex - 1][current_nodey] == 'E') or (
                gridmap[current_nodex - 1][current_nodey] == 'T') or (
                        gridmap[current_nodex - 1][current_nodey] == "EA") or (
                        gridmap[current_nodex - 1][current_nodey] == "TA") or (
                        (current_nodex - 1 == goalx) and (current_nodey == goaly)) or (
                        gridmap[current_nodex - 1][current_nodey] == '1' and scoredij - 1 < 0) or (
                        gridmap[current_nodex - 1][current_nodey] == '2' and scoredij - 1 < 15) or (
                        gridmap[current_nodex - 1][current_nodey] == '3' and scoredij - 1 < 50) or (
                        gridmap[current_nodex - 1][current_nodey] == '4' and scoredij - 1 < 140)or flag):
            if (current_nodex - 1, current_nodey) not in distancelist:
                if flag:
                    distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                    pq.put((dist + 41, current_nodex - 1, current_nodey, dist + 1, scoredij - 41))
                    parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')
                else:
                    distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                    pq.put((dist + 1, current_nodex - 1, current_nodey, dist + 1, scoredij - 1))
                    parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')

            else:
                if flag:
                    if dist + 41 < distancelist[(current_nodex - 1, current_nodey)]:
                        distancelist[(current_nodex - 1, current_nodey)] = dist + 41
                        pq.put((dist + 41, current_nodex - 1, current_nodey, dist + 1, scoredij - 41))
                        parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')
                else:
                    if dist + 1 < distancelist[(current_nodex - 1, current_nodey)]:
                        distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, current_nodex - 1, current_nodey, dist + 1, scoredij - 1))
                        parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')


        # down
        flag = np.any(traps == gridmap[current_nodex + 1][current_nodey])
        if (current_nodex + 1 < height) and ((current_nodex + 1, current_nodey) not in visited) and (

                (gridmap[current_nodex + 1][current_nodey] == 'E') or (
                gridmap[current_nodex + 1][current_nodey] == 'T') or (
                        gridmap[current_nodex + 1][current_nodey] == "EA") or (
                        gridmap[current_nodex + 1][current_nodey] == "TA") or (
                        (current_nodex + 1 == goalx) and (current_nodey == goaly)) or (
                        gridmap[current_nodex + 1][current_nodey] == '1' and scoredij - 1 < 0) or (
                        gridmap[current_nodex + 1][current_nodey] == '2' and scoredij - 1 < 15) or (
                        gridmap[current_nodex + 1][current_nodey] == '3' and scoredij - 1 < 50) or (
                        gridmap[current_nodex + 1][current_nodey] == '4' and scoredij - 1 < 140)or flag):
            if (current_nodex + 1, current_nodey) not in distancelist:
                if flag:
                    distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                    pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
                    parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
                else:
                    distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                    pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))
                    parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')

            else:
                if flag:
                    if dist + 41 < distancelist[(current_nodex + 1, current_nodey)]:
                        distancelist[(current_nodex + 1, current_nodey)] = dist + 41
                        pq.put((dist + 41, current_nodex + 1, current_nodey, dist + 1, scoredij - 41))
                        parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
                else:
                    if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                        distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, current_nodex + 1, current_nodey, dist + 1, scoredij - 1))
                        parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')

        # left
        flag = np.any(traps == gridmap[current_nodex][current_nodey-1])
        if (current_nodey - 1 >= 0) and ((current_nodex, current_nodey - 1) not in visited) and (

                (gridmap[current_nodex][current_nodey - 1] == 'E') or (
                gridmap[current_nodex][current_nodey - 1] == 'T') or (
                        gridmap[current_nodex][current_nodey - 1] == "EA") or (
                        gridmap[current_nodex][current_nodey - 1] == "TA") or (
                        (current_nodex == goalx) and (current_nodey - 1 == goaly)) or (
                        gridmap[current_nodex][current_nodey - 1] == '1' and scoredij - 1 < 0) or (
                        gridmap[current_nodex][current_nodey - 1] == '2' and scoredij - 1 < 15) or (
                        gridmap[current_nodex][current_nodey - 1] == '3' and scoredij - 1 < 50) or (
                        gridmap[current_nodex][current_nodey - 1] == '4' and scoredij - 1 < 140)or flag):
            if (current_nodex, current_nodey - 1) not in distancelist:
                if flag:
                    distancelist[(current_nodex, current_nodey - 1)] = dist + 41
                    pq.put((dist + 41, current_nodex, current_nodey - 1, dist + 1, scoredij - 41))
                    parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')
                else:
                    distancelist[(current_nodex, current_nodey - 1)] = dist + 1
                    pq.put((dist + 1, current_nodex, current_nodey - 1, dist + 1, scoredij - 1))
                    parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')

            else:
                if flag:
                    if dist + 41 < distancelist[(current_nodex, current_nodey - 1)]:
                        distancelist[(current_nodex, current_nodey - 1)] = dist + 41
                        pq.put((dist + 41, current_nodex, current_nodey - 1, dist + 1, scoredij - 41))
                        parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey - 1)]:
                        distancelist[(current_nodex, current_nodey - 1)] = dist + 1
                        pq.put((dist + 1, current_nodex, current_nodey - 1, dist + 1, scoredij - 1))
                        parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')


        # right
        flag = np.any(traps == gridmap[current_nodex][current_nodey+1])
        if (current_nodey + 1 < width) and ((current_nodex, current_nodey + 1) not in visited) and (
                (gridmap[current_nodex][current_nodey + 1] == 'E') or (
                gridmap[current_nodex][current_nodey + 1] == 'T') or (
                        gridmap[current_nodex][current_nodey + 1] == "EA") or (
                        gridmap[current_nodex][current_nodey + 1] == "TA") or (
                        (current_nodex == goalx) and (current_nodey + 1 == goaly)) or (
                        gridmap[current_nodex][current_nodey + 1] == '1' and scoredij - 1 < 0) or (
                        gridmap[current_nodex][current_nodey + 1] == '2' and scoredij - 1 < 15) or (
                        gridmap[current_nodex][current_nodey + 1] == '3' and scoredij - 1 < 50) or (
                        gridmap[current_nodex][current_nodey + 1] == '4' and scoredij - 1 < 140)or flag):
            if (current_nodex, current_nodey + 1) not in distancelist:
                if flag:
                    distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                    pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
                    parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')
                else:
                    distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                    pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))
                    parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')

            else:
                if flag:
                    if dist + 41 < distancelist[(current_nodex, current_nodey + 1)]:
                        distancelist[(current_nodex, current_nodey + 1)] = dist + 41
                        pq.put((dist + 41, current_nodex, current_nodey + 1, dist + 1, scoredij - 41))
                        parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                        distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                        pq.put((dist + 1, current_nodex, current_nodey + 1, dist + 1, scoredij - 1))
                        parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')


