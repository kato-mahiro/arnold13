#coding:utf-8
import random
from baseline_agent import BaselineAgent
from field import Field

PREY_NUM = 40

def main():
    field = Field()
    for i in range(PREY_NUM):
        field.prey_arrangement()
    for i in range(len(field.grid[0])):
        print(' '.join(field.grid[i]))
    print("===")
    agent = BaselineAgent(10,10)
    field_of_view = field.give_field_of_view(agent.x_coordinate, agent.y_coordinate)
    for i in range(len(field_of_view[0])):
        print(' '.join(field_of_view[i]))
    print("===")
    input_vector = field.give_input_vector(field_of_view)
    print(input_vector)

if __name__=='__main__':
    main()
