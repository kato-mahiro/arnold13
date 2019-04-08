"""
This script provide one trial.
a trial return result value(total reword which agent have got)
"""
from baseline_agent import BaselineAgent
from field import Field
from decoder import decoder
from const import *

def trial(gene):
    field = Field()
    for i in range(PREY_NUM):
        field.add_prey()
    weights_ih,weights_ho = decoder(gene)
    agent = BaselineAgent(10,10,weights_ih,weights_ho)

    for i in range(400):
        input_vector = field.give_input_vector(agent.x_coordinate,agent.y_coordinate)
        action_no = agent.get_action(input_vector)
        field.position_update(action_no,agent)
    return agent.total_reword

if __name__=='__main__':
    for i in range(100):
        print(trial())
