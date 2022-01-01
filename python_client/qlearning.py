def is_terminal(observation):
    agentx = observation[0][0]
    agenty = observation[0][1]
    turn = observation[1]
    diamond = observation[2]
    dic_color_number = observation[3]
    if turn == 0 or (not len(diamond)):
        return True
    if dic_color_number['y'] == 15 and dic_color_number['g'] == 8 and dic_color_number['r'] == 5 and dic_color_number['b'] == 4:
        return True
