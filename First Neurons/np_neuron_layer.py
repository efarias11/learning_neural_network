<<<<<<< HEAD
import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2, 3, .5]

# np.dot treats the matrix as a list of vectors
outputs = np.dot(weights, inputs) + biases
# np.dot(weights, inputs) + biases = [np.dot(weights[0], inputs), np.dot(weights[1], inputs),
#                                     np.dot(weights[2], inputs)] + biases 
=======
import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2, 3, .5]

# np.dot treats the matrix as a list of vectors
outputs = np.dot(weights, inputs) + biases
# np.dot(weights, inputs) + biases = [np.dot(weights[0], inputs), np.dot(weights[1], inputs),
#                                     np.dot(weights[2], inputs)] + biases 
>>>>>>> 11b8f4ac1fe48316e1cf3522f765accabbacde79
print(outputs)