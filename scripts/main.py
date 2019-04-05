#coding:utf-8
from baseline_agent import BaselineAgent
from field import Field

PREY_NUM = 40

def get_input_vector(field_of_view):
    input_vector=[]
    field_of_view[0] = field_of_view[0][2:-2]
    field_of_view[1] = field_of_view[1][1:-1]
    field_of_view[-2] = field_of_view[-2][1:-1]
    field_of_view[-1] = field_of_view[-1][2:-2]

def main():
    field = Field()
    for i in range(PREY_NUM):
        field.prey_arrangement()
    agent = BaselineAgent(10,10)
    field_of_view = field.give_field_of_view(agent.x_coordinate, agent.y_coordinate)
    get_input_vector(field_of_view)

if __name__=='__main__':
    main()
