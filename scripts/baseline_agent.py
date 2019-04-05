#coding:utf-8
from neurons import Neurons

class BaselineAgent:
    def __init__(self,x,y):
        self.__neurons = Neurons()
        self.x_coordinate = x
        self.y_coordinate = y
        self.total_reword = 0
    def get_action(self,input_vector):
        output_list = self.__neurons.get_output(input_vector)
        return output_list.index(max(output_list))
