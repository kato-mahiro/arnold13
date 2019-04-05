#coding:utf-8
import random
import pprint

FIELD_RANGE = 20
VIEW_RANGE = 7
PREY_NUM = 40

class Prey:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.adjacent_cells = [None for i in range(8)]

class Field:
    def __init__(self):
        self.grid = [ ['_' for i in range(FIELD_RANGE)] for j in range(FIELD_RANGE)]
        #note: grid[y][x]  --- x: horizontal, y: vertical. upper left corner is coordinate origin(0,0)
        self.preys = []

    def troidal_process(self,n):
        "this corrects the coordinates to avoid out of range."
        if n < 0:
            return FIELD_RANGE + n
        elif n >= FIELD_RANGE:
            return n - FIELD_RANGE
        else:
            return n

    def prey_arrangement(self):
        " arrange a prey object so it doesn't adjacent to other objects."
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
                if self.grid[prey.adjacent_cells[i][0]][prey.adjacent_cells[i][1]] == '#':
                    collision = True
                    break
            if collision == True:
                continue
            else:
                self.grid[prey.x][prey.y] = '#'
                if prey.direction == 'vertical':
                    self.grid[prey.x][prey.y+1] = '#'
                elif prey.direction == 'horizontal':
                    self.grid[prey.x+1][prey.y] = '#'
                return

    def give_field_of_view(self, x_coordinate, y_coordinate):
        field_of_view = [ ['_' for i in range(VIEW_RANGE)] for j in range(VIEW_RANGE) ]
        for y in range(VIEW_RANGE):
            for x in range(VIEW_RANGE):
                adjusted_x = self.troidal_process(x_coordinate + x - VIEW_RANGE//2)
                adjusted_y = self.troidal_process(y_coordinate + y - VIEW_RANGE//2)
                field_of_view[y][x] = self.grid[adjusted_y][adjusted_x]
        return field_of_view

    def give_input_vector(self, field_of_view):
        input_vector=[]
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

    def position_update(self, action_no, agent):
        if action_no == 0 or action_no == 1: #step_forward,jump_forward
            if agent.direction == 'up':
                agent.y_coordinate -= (1 + action_no)
            elif agent.direction == 'right':
                agent.x_coordinate += (1 + action_no)
            elif agent.direction == 'down':
                agent.y_coordinate += (1 + action_no)
            elif agent.direction == 'left':
                agent.x_coordinate -= (1 + action_no)
        if action_no == 2: #turn_right
            if agent.direction == 'up':
                agent.direction = 'right'
            elif agent.direction == 'right':
                agent.direction = 'down'
            elif agent.direction == 'down':
                agent.direction = 'left'
            elif agent.direction == 'left':
                agent.direction = 'up'
        if action_no == 3: #turn_left
            if agent.direction == 'up':
                agent.direction = 'left'
            elif agent.direction == 'right':
                agent.direction = 'up'
            elif agent.direction == 'down':
                agent.direction = 'right'
            elif agent.direction == 'left':
                agent.direction = 'down'
        agent.x_coordinate = self.troidal_process(agent.x_coordinate)
        agent.y_coordinate = self.troidal_process(agent.y_coordinate)

if __name__=='__main__':
    field = Field()
    for i in range(PREY_NUM):
        field.prey_arrangement()

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
