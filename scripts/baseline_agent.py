#coding:utf-8

class BaselineAgent:
    def __init__(self, neurons, initial_position):
        self.__neurons = neurons
        self.position = initial_position
        self.total_reword = 0
    def get_action(self,field_of_view):
        output_list = self.__neurons.get_output(field_of_view)
        return output_list.index(max(output_list))
