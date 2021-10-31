from queue import PriorityQueue,  LifoQueue

def dij_show_way(agentx, agenty, goalx, goaly, map, height, width):
        visited = {}
        distancelist = {}
        parent = {}
        way = LifoQueue()
        parent[(agentx, agenty)] = -1
        pq = PriorityQueue()
        pq.put((0, (agentx, agenty)))
        distancelist[(agentx, agenty)] = 0

        while not pq.empty():
            temp = pq.get()
            dist = temp[0]
            current_nodex = temp[1][0]
            current_nodey = temp[1][1]
            visited[(current_nodex, current_nodey)] = True
            if current_nodex == goalx and current_nodey == goaly:
                x = current_nodex
                y = current_nodey
                if map[x][y] == 'T':
                    way.put('t')
                while parent[(x, y)] != -1:
                    way.put(parent[(x, y)][3])
                    x = parent[(x, y)][0]
                    y = parent[(x, y)][1]
                return way
            # up
            if (current_nodex - 1 >= 0) and (visited[(current_nodex - 1, current_nodey)] not in visited) and (
                    map[current_nodex - 1][current_nodey] == 'E') and (map[current_nodex - 1][current_nodey] == 'T'):
                if distancelist[(current_nodex - 1, current_nodey)] not in distancelist:
                    pq.put((dist + 1, (current_nodex - 1, current_nodey)))
                    parent[(current_nodex-1, current_nodey)] = (current_nodex, current_nodey, 'u')
                else:
                    if dist + 1 < distancelist[(current_nodex - 1, current_nodey)]:
                        distancelist[(current_nodex - 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, (current_nodex - 1, current_nodey)))
                        parent[(current_nodex - 1, current_nodey)] = (current_nodex, current_nodey, 'u')
            # down
            if (current_nodex + 1 < height) and (visited[(current_nodex + 1, current_nodey)] not in visited) and (
                    map[current_nodex + 1][current_nodey] == 'E') and (map[current_nodex + 1][current_nodey] == 'T'):
                if distancelist[(current_nodex + 1, current_nodey)] not in distancelist:
                    pq.put((dist + 1, (current_nodex + 1, current_nodey)))
                    parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
                else:
                    if dist + 1 < distancelist[(current_nodex + 1, current_nodey)]:
                        distancelist[(current_nodex + 1, current_nodey)] = dist + 1
                        pq.put((dist + 1, (current_nodex + 1, current_nodey)))
                        parent[(current_nodex + 1, current_nodey)] = (current_nodex, current_nodey, 'd')
            # left
            if (current_nodey - 1 >= 0) and (visited[(current_nodex, current_nodey - 1)] not in visited) and (
                    map[current_nodex][current_nodey - 1] == 'E') and (map[current_nodex][current_nodey - 1] == 'T'):
                if distancelist[(current_nodex, current_nodey - 1)] not in distancelist:
                    pq.put((dist + 1, (current_nodex, current_nodey - 1)))
                    parent[(current_nodex, current_nodey - 1)] = (current_nodex, current_nodey, 'l')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey - 1)]:
                        distancelist[(current_nodex, current_nodey - 1)] = dist + 1
                        pq.put((dist + 1, (current_nodex, current_nodey-1)))
                        parent[(current_nodex , current_nodey-1)] = (current_nodex, current_nodey, 'l')

            # right
            if (current_nodey + 1 < width) and (visited[(current_nodex, current_nodey + 1)] not in visited) and (
                    map[current_nodex][current_nodey + 1] == 'E') and (map[current_nodex][current_nodey + 1] == 'T'):
                if distancelist[(current_nodex, current_nodey + 1)] not in distancelist:
                    pq.put((dist + 1, (current_nodex, current_nodey + 1)))
                    parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')
                else:
                    if dist + 1 < distancelist[(current_nodex, current_nodey + 1)]:
                        distancelist[(current_nodex, current_nodey + 1)] = dist + 1
                        pq.put((dist + 1, (current_nodex, current_nodey + 1)))
                        parent[(current_nodex, current_nodey + 1)] = (current_nodex, current_nodey, 'r')


