
def holeornot(gridmap, height,width,holecounter, hole, score_agent, score_enemy, agent_trap, enemy_trap, befor_score_agent,start_agent,start_enemy,next_move,next_move_enemy,character,character_enemy):
    holenumber = len(hole)
    maximun_holecounter = holenumber + 2
    nextmove = tuple()
    sx=start_agent[0]
    sy=start_agent[1]
    ex=start_enemy[0]
    ey=start_enemy[1]
    if gridmap[start_agent[0]][start_agent[1]] == 'T'+ character and gridmap[next_move[0]][next_move[1]] == 'T':
        if holecounter > maximun_holecounter:
            if gridmap[start_enemy[0]][start_enemy[1]] == 'T' + character_enemy and gridmap[next_move_enemy[0]][
                next_move_enemy[1]] == 'T':
                pass





# if  befor_score_agent - score_agent > 20 and holecounter > 1:
#     pass



