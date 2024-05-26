import numpy as np # np treats these lists as arrays
import nnfs 
from nnfs.datasets import spiral_data

nnfs.init()

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons): # np.random.randn(rows, columns)
        self.weights = 0.01*np.random.randn(n_inputs, n_neurons) # np.random.randn generates random values weight values around the center 0
                                                                 # best to keep the weight values between -1 and 1 and we scale this by multiplying 0.01
        self.biases = np.zeros((1, n_neurons)) # np.zeros generates 0's in the bias vector 

    def foward(self, inputs): # moving forward through the model, input layer -> hidden layer -> output layer
        self.output = np.dot(inputs, self.weights) + self.biases # mathing for an output

X, y = spiral_data(samples=100, classes=3) # creating the dataset
dense1 = Layer_Dense(2, 3) # create dense layer with 2 input features and 3 output values

dense1.foward(X) # performing a forward pass operation with the training data

print(dense1.output[:5]) # seeing the first few sample outputs