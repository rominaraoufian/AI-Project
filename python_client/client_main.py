
from base import BaseAgent, Action
from getinfo import action_state_func

class Agent(BaseAgent):

    def do_turn(self) -> Action:
        action_state = action_state_func(self.grid,self.grid_height,self.grid_width,self.turn_count,self.max_turn_count,self.character,self.score,1)
        print(action_state)
        mapgrid = self.grid
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                print(mapgrid[i][j], end="")
            print()
        if action_state == 'u':
            return Action.UP
        if action_state == 'd':
            return Action.DOWN
        if action_state == 'l':
            return Action.LEFT
        if action_state == 'r':
            return Action.RIGHT
        if action_state == 't':
            return Action.TELEPORT
        if action_state == 'n':
            return Action.NOOP


if __name__ == '__main__':
    data = Agent().play()
    print("FINISH : ", data)
