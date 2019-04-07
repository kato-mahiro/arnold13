#coding:utf-8
import os
import random
from baseline_agent import BaselineAgent
from field import Field

PREY_NUM = 40

def draw(field, agent):
    grid_for_draw = [ g[:] for g in field.grid ]
    if agent.direction == 'up':
        grid_for_draw[agent.y_coordinate][agent.x_coordinate] = '^'
    elif agent.direction == 'right':
        grid_for_draw[agent.y_coordinate][agent.x_coordinate] = '>'
    elif agent.direction == 'down':
        grid_for_draw[agent.y_coordinate][agent.x_coordinate] = 'v'
    elif agent.direction == 'left':
        grid_for_draw[agent.y_coordinate][agent.x_coordinate] = '<'
    for i in range(len(field.grid[0])):
        print(' '.join(grid_for_draw[i]))


def main():
    field = Field()
    for i in range(PREY_NUM):
        field.add_prey()
    agent = BaselineAgent(10,10)

    while(True):
        print('total_reword:' ,agent.total_reword)
        draw(field,agent)
        input_vector = field.give_input_vector(agent.x_coordinate, agent.y_coordinate)
        c = input('action: ')
        if c == 'g':
            action_no = 0
        elif c == 'j':
            action_no = 1
        elif c == 'r':
            action_no = 2
        elif c == 'l':
            action_no = 3
        field.position_update(action_no,agent)

if __name__=='__main__':
    main()
