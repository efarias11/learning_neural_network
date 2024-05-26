import numpy as np

inputs =  [[1, 2, 3, 2.5], # shape (3,4)
           [2, 5, -1, 2], 
           [-1.5, 2.7, 3.3, -0.8]]

weights = [[.2, .8, -.5, 1], # shape (3,4), we need to transpose (T) this, so the shape can become (4,3) for the operation to work
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]
biases = [2, 3, .5]

outputs = np.dot(inputs, np.array(weights).T) + biases
print(outputs)