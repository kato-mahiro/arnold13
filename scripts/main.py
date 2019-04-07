#coding:utf-8
import random
from baseline_agent import BaselineAgent
from field import Field

PREY_NUM = 40

def main():
    field = Field()
    for i in range(PREY_NUM):
        field.add_prey()
    agent = BaselineAgent(10,10)

    input_vector = field.give_input_vector(agent.x_coordinate, agent.y_coordinate)
    print(input_vector)
    action_no = agent.get_action(input_vector)
    field.position_update(action_no,agent)

if __name__=='__main__':
    main()
