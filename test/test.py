import os
from baseline_agent import BaselineAgent
from field import Field
from neurons import Neurons

PREY_NUM = 40

def draw(field):
    grid_for_draw = [ g[:] for g in field.grid ]
    if field.agent.direction == 'up':
        grid_for_draw[field.agent.y][field.agent.x] = '^'
    elif field.agent.direction == 'right':
        grid_for_draw[field.agent.y][field.agent.x] = '>'
    elif field.agent.direction == 'down':
        grid_for_draw[field.agent.y][field.agent.x] = 'v'
    elif field.agent.direction == 'left':
        grid_for_draw[field.agent.y][field.agent.x] = '<'
    for i in range(len(field.grid[0])):
        print(' '.join(grid_for_draw[i]))
    print('total_reword:' ,field.agent.total_reword)

def TestManual():
    field = Field()
    for i in range(PREY_NUM):
        field.add_prey()
    field.set_agent( BaselineAgent(10,10))
    while(True):
        os.system('clear')
        draw(field)
        input_vector = field.give_input_vector()
        print(input_vector)
        c = input('action: ')
        if c == 'g':
            action_no = 0
        elif c == 'j':
            action_no = 1
        elif c == 'r':
            action_no = 2
        elif c == 'l':
            action_no = 3
        field.position_update(action_no)

def TestAuto():
    field = Field()
    for i in range(PREY_NUM):
        field.add_prey()
    field.set_agent( BaselineAgent(10,10))
    for i in range(400):
        os.system('clear')
        draw(field)
        field.one_step_action()
        print(field.agent.total_reword)

if __name__=='__main__':
    TestManual()
