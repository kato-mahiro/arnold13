from neurons import Neurons
from const import *
from pprint import pprint

print("INPUT_NUMBER: ",INPUT_NUMBER)
print("ECHO_NUMBER: ",ECHO_NUMBER)
print("HIDDEN_NUMBER: ",HIDDEN_NUMBER)
print("OUTPUT_NUMBER: ",OUTPUT_NUMBER)
print("MODURATORY_NUMBER: ",MODURATORY_NUMBER) 

def test__init__(neurons):
    print("weights_ih\n",neurons.weights_ih)
    print("weights_ho\n",neurons.weights_ho)
    print("weights_im\n",neurons.weights_im)
    print("weights_mh\n",neurons.weights_mh)
    print("weights_em\n",neurons.weights_em)
    print("echo_values\n",neurons.echo_values)

def test_get_output(neurons,input_vector):
    print("weigh_ho\n",neurons.weights_ho)
    output_vector = neurons.get_output(input_vector)
    print("weigh_ho\n",neurons.weights_ho)

neurons = Neurons(weights_ih=[[1.0,1.0,1.0],[1.0,1.0,1.0]],\
                  weights_ho=[[1.0,1.0],[1.0,1.0],[1.0,1.0]],\
                  weights_im=[[1.0,1.0],[1.0,1.0]],\
                  weights_mh=[[1.0,1.0,1.0],[1.0,1.0,1.0]],\
                  weights_em=[[1.0,1.0],[1.0,1.0]])

test__init__(neurons)
test_get_output(neurons,[1.0,1.0])
