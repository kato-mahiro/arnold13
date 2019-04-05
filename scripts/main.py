#coding:utf-8
import random
from baseline_agent import BaselineAgent
from field import Field

PREY_NUM = 40

def get_input_vector(field_of_view):
    for i in range(7):
        print(' '.join(field_of_view[i]))
    input_vector=[]
    field_of_view[0] = field_of_view[0][2:-2]
    field_of_view[1] = field_of_view[1][1:-1]
    field_of_view[-2] = field_of_view[-2][1:-1]
    field_of_view[-1] = field_of_view[-1][2:-2]
    for i in range(7):
        input_vector += field_of_view[i]
    input_vector += [1.0] #(bias neuron)
    input_vector += [random.choice([0.0,1.0])]
    for i in range(len(input_vector)):
        if input_vector[i] == '_':
            input_vector[i] = 0.0
        elif input_vector[i] == '#':
            input_vector[i] = 1.0

def main():
    field = Field()
    for i in range(PREY_NUM):
        field.prey_arrangement()
    agent = BaselineAgent(10,10)
    field_of_view = field.give_field_of_view(agent.x_coordinate, agent.y_coordinate)
    get_input_vector(field_of_view)

if __name__=='__main__':
    main()
