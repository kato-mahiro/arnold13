#coding:utf-8
from .neurons import Neurons
import random

class MainAgent:
    def __init__(self,x=10,y=10,weights_ih=None,weights_ho=None,weights_im=None,weights_mh=None,weights_em=None):
        self.__neurons = Neurons(weights_ih,weights_ho,weights_im,weights_mh,weights_em)
        self.x = x
        self.y = y
        self.total_reword = 0
        self.direction = 'up' # -up,down,right,left
        self.randomized_id = [0,1,2,3]
        random.shuffle(self.randomized_id)
    def get_action(self,input_vector):
        output_vector = self.__neurons.get_output(input_vector)
        max_number = output_vector.index(max(output_vector))
        return randomized_id[max_number]

if __name__=='__main__':
    for i in range(10):
        main_agent = MainAgent()
        print(main_agent.output_id)
