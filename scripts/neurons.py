#coding:utf-8
import numpy as np
import math

INPUT_NUMBER = 10
HIDDEN_LAYER_NUMBER = 10
OUTPUT_NUMBER = 4

class Neurons:
    def __init__(self):
        #create randomized np.array. range is (-2.0 ~ +2.0).
        self.weights_ih = 4.0 * np.random.random(( INPUT_NUMBER, HIDDEN_LAYER_NUMBER)) -2.0
        self.weights_ho = 4.0 * np.random.random(( HIDDEN_LAYER_NUMBER, OUTPUT_NUMBER)) -2.0
    def set_weights(weights_ih,weights_ho):
        self.weights_ih = weights_ih
        self.weights_ho = weights_ho
    def get_output(self, input_vector):
        output_vector = np.dot(input_vector, self.weights_ih)
        output_vector = [math.tanh(i) for i in output_vector.tolist()]
        output_vector = np.dot(output_vector, self.weights_ho)
        output_vector = [math.tanh(i) for i in output_vector.tolist()]
        return output_vector

if __name__=='__main__':
    n = Neurons()
    print(n.weights_ih)
    input_vector=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
    print(n.get_output(input_vector))
