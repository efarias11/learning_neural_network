<<<<<<< HEAD
import numpy as np # np treats these lists as arrays

inputs =  [[1, 2, 3, 2.5], 
           [2, 5, -1, 2], 
           [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons): # np.random.randn(rows, columns)
        self.weights = 0.01*np.random.randn(n_inputs, n_neurons) # np.random.randn generates random values weight values around the center 0
                                                                 # best to keep the weight values between -1 and 1 and we scale this by multiplying 0.01
        self.biases = np.zeros((1, n_neurons)) # np.zeros generates 0's in the bias vector 

    def foward(self, inputs): # moving forward through the model, input layer -> hidden layer -> output layer
        self.output = np.dot(inputs, self.weights) + self.biases # mathing for an output
=======
import numpy as np # np treats these lists as arrays

inputs =  [[1, 2, 3, 2.5], 
           [2, 5, -1, 2], 
           [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons): # np.random.randn(rows, columns)
        self.weights = 0.01*np.random.randn(n_inputs, n_neurons) # np.random.randn generates random values weight values around the center 0
                                                                 # best to keep the weight values between -1 and 1 and we scale this by multiplying 0.01
        self.biases = np.zeros((1, n_neurons)) # np.zeros generates 0's in the bias vector 

    def foward(self, inputs): # moving forward through the model, input layer -> hidden layer -> output layer
        self.output = np.dot(inputs, self.weights) + self.biases # mathing for an output
>>>>>>> 11b8f4ac1fe48316e1cf3522f765accabbacde79
