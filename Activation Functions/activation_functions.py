# activation functions helps neural network with two hidden layers map non-linear functions (line fitting)
# there are two activations in a network one in the hidden layers and one in the output (they can be the same function)
# we don't use linear functions because all of the networks outputs will only fit/output to that linear line
# Rectified Linear Unit Activation function reps non-linear functions (if x > 0, y = x or if x <= 0, y = 0)
# weight influences the slope, while bias offset the function horizontally or vertically depending on the weights influence on the function
# start with the top neurons to adjust to the shape, and use the bottom neurons to offset it vertically. Then to 2nd top neuron and most bottom again, etc.

inputs = [0, 2 ,-1, 3.3, -2.7, 1.1, 2.2, -100]

output = []
for i in inputs: # Rectified Linear Unit Activation Function (ReLU)
    # if i > 0:
    #     output.append(i)
    # else:
    #     output.append(0)
    output.append(max(0,i))
print(output)