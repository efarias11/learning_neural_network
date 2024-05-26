import numpy as np

inputs = [1, 2,3,2.5]
weights = [.2, .8, -.5, 1]
bias = 2

outputs = np.dot(weights, inputs) + bias
# np.dot([.2, .8, -.5, 1], [1, 2,3,2.5]) = (0.2*1.0 + 0.8*2.0 + -0.5*3.0 +1.0*2.5) + 2 = 4.8

print(outputs)