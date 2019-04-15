#coding:utf-8
import random
import pprint
import numpy as np
from .const import *
from .baseline_agent import BaselineAgent

class Prey:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.x2 = None
        self.y2 = None
        self.direction = direction
        self.adjacent_cells = [None for i in range(8)]

class Field:
    def __init__(self):
        self.grid = [ ['_' for i in range(FIELD_RANGE)] for j in range(FIELD_RANGE)]
        "note: grid[y][x]  --- x: horizontal, y: vertical. upper left corner is coordinate origin(0,0)"
        self.preys = []

    def set_agent(self,agent):
        self.agent = agent

    def troidal_process(self,n):
        "this corrects the coordinates to avoid out of range."
        if n < 0:
            return FIELD_RANGE + n
        elif n >= FIELD_RANGE:
            return n - FIELD_RANGE
        else:
            return n

    def add_prey(self):
        " add a prey object so it doesn't adjacent to other objects."
        while(True):
            collision = False
            prey = Prey(random.randint(0, FIELD_RANGE-2), random.randint(0, FIELD_RANGE-2),\
                                                          random.choice(['vertical','horizontal']) )
            if prey.direction == 'vertical':
                prey.adjacent_cells[0] = ([prey.x, prey.y-1])
                prey.adjacent_cells[1] = ([prey.x+1, prey.y])
                prey.adjacent_cells[2] = ([prey.x+1, prey.y+1])
                prey.adjacent_cells[3] = ([prey.x, prey.y+2])
                prey.adjacent_cells[4] = ([prey.x-1, prey.y+1])
                prey.adjacent_cells[5] = ([prey.x-1, prey.y])
                prey.adjacent_cells[6] = ([prey.x, prey.y])
                prey.adjacent_cells[7] = ([prey.x, prey.y+1])
            elif prey.direction == 'horizontal':
                prey.adjacent_cells[0] = ([prey.x, prey.y-1])
                prey.adjacent_cells[1] = ([prey.x+1, prey.y-1])
                prey.adjacent_cells[2] = ([prey.x+2, prey.y])
                prey.adjacent_cells[3] = ([prey.x+1, prey.y+1])
                prey.adjacent_cells[4] = ([prey.x, prey.y+1])
                prey.adjacent_cells[5] = ([prey.x-1, prey.y])
                prey.adjacent_cells[6] = ([prey.x, prey.y])
                prey.adjacent_cells[7] = ([prey.x+1, prey.y])

            for i in range(8):
                prey.adjacent_cells[i][0] = self.troidal_process(prey.adjacent_cells[i][0])
                prey.adjacent_cells[i][1] = self.troidal_process(prey.adjacent_cells[i][1])
                if self.grid[prey.adjacent_cells[i][1]][prey.adjacent_cells[i][0]] == '#':
                    collision = True
                    break
            if collision == True:
                continue
            else:
                self.grid[prey.y][prey.x] = '#'
                if prey.direction == 'vertical':
                    prey.x2 = prey.x
                    prey.y2 = prey.y +1
                    self.grid[prey.y2][prey.x] = '#'
                elif prey.direction == 'horizontal':
                    prey.x2 = prey.x +1
                    prey.y2 = prey.y
                    self.grid[prey.y2][prey.x2] = '#'
                self.preys.append(prey)
                return

    def del_prey(self,prey_no):
        self.grid[self.preys[prey_no].y][self.preys[prey_no].x] = '_'
        self.grid[self.preys[prey_no].y2][self.preys[prey_no].x2] = '_'
        del(self.preys[prey_no])

    def give_input_vector(self):
        is_check_field_of_view = False
        field_of_view = [ ['_' for i in range(VIEW_RANGE)] for j in range(VIEW_RANGE) ]
        input_vector=[]
        for y in range(VIEW_RANGE):
            for x in range(VIEW_RANGE):
                adjusted_x = self.troidal_process(self.agent.x + x - VIEW_RANGE//2)
                adjusted_y = self.troidal_process(self.agent.y + y - VIEW_RANGE//2)
                field_of_view[y][x] = self.grid[adjusted_y][adjusted_x]
        # need to rotate acording to agent's direction
        if self.agent.direction == 'right':
            field_of_view = np.rot90(field_of_view).tolist()
        elif self.agent.direction == 'down':
            field_of_view = np.rot90(field_of_view).tolist()
            field_of_view = np.rot90(field_of_view).tolist()
        elif self.agent.direction == 'left':
            field_of_view = np.rot90(field_of_view,k=-1).tolist()

        if is_check_field_of_view == True:
            print("==field_of_view===")
            for i in range(VIEW_RANGE):
                print(' '.join(field_of_view[i]))
            print("==================")
        "cut edge information"
        field_of_view[0] = field_of_view[0][2:-2]
        field_of_view[1] = field_of_view[1][1:-1]
        field_of_view[-2] = field_of_view[-2][1:-1]
        field_of_view[-1] = field_of_view[-1][2:-2]
        for i in range(VIEW_RANGE):
            input_vector += field_of_view[i]
        input_vector += [1.0] #(bias neuron)
        input_vector += [random.choice([0.0,1.0])]
        for i in range(len(input_vector)):
            if input_vector[i] == '_':
                input_vector[i] = 0.0
            elif input_vector[i] == '#':
                input_vector[i] = 1.0
        return input_vector

    def position_update(self, action_no):
        action_no = int(action_no)
        if action_no == 0 or action_no == 1: #step_forward,jump_forward
            if self.agent.direction == 'up':
                self.agent.y -= (1 + action_no)
            elif self.agent.direction == 'right':
                self.agent.x += (1 + action_no)
            elif self.agent.direction == 'down':
                self.agent.y += (1 + action_no)
            elif self.agent.direction == 'left':
                self.agent.x -= (1 + action_no)
        if action_no == 2: #turn_right
            if self.agent.direction == 'up':
                self.agent.direction = 'right'
            elif self.agent.direction == 'right':
                self.agent.direction = 'down'
            elif self.agent.direction == 'down':
                self.agent.direction = 'left'
            elif self.agent.direction == 'left':
                self.agent.direction = 'up'
        if action_no == 3: #turn_left
            if self.agent.direction == 'up':
                self.agent.direction = 'left'
            elif self.agent.direction == 'right':
                self.agent.direction = 'up'
            elif self.agent.direction == 'down':
                self.agent.direction = 'right'
            elif self.agent.direction == 'left':
               self.agent.direction = 'down'
        self.agent.x = self.troidal_process(self.agent.x)
        self.agent.y = self.troidal_process(self.agent.y)
        if action_no == 0 or action_no == 1:
            for n in range(len(self.preys)):
                if (self.preys[n].x == self.agent.x and self.preys[n].y == self.agent.y)\
                    or\
                   (self.preys[n].x2 == self.agent.x and self.preys[n].y2 == self.agent.y):
                    if (self.agent.direction == 'up' or self.agent.direction == 'down') and \
                                                self.preys[n].direction == 'vertical' :
                        self.agent.total_reword += 1.0
                    elif (self.agent.direction == 'right' or self.agent.direction == 'left') and \
                                                self.preys[n].direction == 'horizontal' :
                        self.agent.total_reword += 1.0
                    else:
                        self.agent.total_reword -= 1.0
                    self.del_prey(n)
                    self.add_prey()
                    return

    def one_step_action(self):
        input_vector = self.give_input_vector()
        action_no = self.agent.get_action(input_vector)
        self.position_update(action_no)

if __name__=='__main__':
    field = Field()
    for i in range(10):
        field.add_prey()
    for i in range(FIELD_RANGE):
        print(' '.join(field.grid[i]))
    print("---")

    for j in range(10):
        field.del_prey(0)
        for i in range(FIELD_RANGE):
            print(' '.join(field.grid[i]))
        print("---")

    """
    while(True):
        x = int(input())
        y = int(input())
        field.grid[y][x] = 'A'
        for i in range(FIELD_RANGE):
            print(' '.join(field.grid[i]))
        print("---")
        f = field.give_field_of_view(x,y)
        for i in range(VIEW_RANGE):
            print(' '.join(f[i]))
        print("---")
    """
