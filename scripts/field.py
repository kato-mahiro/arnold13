#coding:utf-8
import random

FIELD_RANGE = 20
VIEW_RANGE = 7
PREY_NUM = 40
object_num = 0

class Prey:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.adjacent_cells = [None for i in range(8)]

class Field:
    def __init__(self):
        self.grid = [ ['_' for i in range(FIELD_RANGE)] for j in range(FIELD_RANGE)]
        self.preys = []

    def troidal_process(self,n):
        "this correct the coordinates to avoid out of range."
        if n < 0:
            return FIELD_RANGE + n
        elif n >= FIELD_RANGE:
            return n - FIELD_RANGE
        else:
            return n

    def prey_arrangement(self):
        global object_num
        " arrange a prey object so it doesn't adjacent to other objects."
        while(True):
            collision = False
            prey = Prey(random.randint(0, FIELD_RANGE-2), random.randint(0, FIELD_RANGE-2),\
                                                          random.choice(['vertical','horizontal']) )
            if prey.direction == 'vertical':
                print("縦方向オブジェクト")
                prey.adjacent_cells[0] = ([prey.x, prey.y-1])
                prey.adjacent_cells[1] = ([prey.x+1, prey.y])
                prey.adjacent_cells[2] = ([prey.x+1, prey.y+1])
                prey.adjacent_cells[3] = ([prey.x, prey.y+2])
                prey.adjacent_cells[4] = ([prey.x-1, prey.y+1])
                prey.adjacent_cells[5] = ([prey.x-1, prey.y])
                prey.adjacent_cells[6] = ([prey.x, prey.y])
                prey.adjacent_cells[7] = ([prey.x, prey.y+1])
            elif prey.direction == 'horizontal':
                print("横方向オブジェクト")
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
                print(prey.adjacent_cells[i])
                if self.grid[prey.adjacent_cells[i][0]][prey.adjacent_cells[i][1]] == '#':
                    collision = True
                    print("衝突した")
                    break
            if collision == True:
                continue
            else:
                print("オブジェクトを追加する")
                object_num += 1
                self.grid[prey.x][prey.y] = '#'
                if prey.direction == 'vertical':
                    self.grid[prey.x][prey.y+1] = '#'
                elif prey.direction == 'horizontal':
                    self.grid[prey.x+1][prey.y] = '#'
                return 


if __name__=='__main__':
    field = Field()
    for i in range(PREY_NUM):
        field.prey_arrangement()
    for i in range(FIELD_RANGE):
        print( ' '.join(field.grid[i]))
    print(object_num)
