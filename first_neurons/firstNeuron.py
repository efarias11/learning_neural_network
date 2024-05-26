# inputs = [1, 2, 3]
# weights = [.2, .8, -.5]
# bias  = 2
# # three input nodes has three edges (weights) connected to a single neuron (each neuron has a single bias)
# output  = (inputs[0]*weights[0] +
#            inputs[1]*weights[1] + 
#            inputs[2]*weights[2] + bias) # multiplying and summing the input "nodes" with their "edges" (weights) then adding the bias of the single neuron to it
# print(output) # = 2.3

# adding another input needs another associated weight
inputs = [1, 2, 3, 2.5]
weights = [.2, .8, -.5, 1]
bias  = 2
output  = (inputs[0]*weights[0] +
           inputs[1]*weights[1] + 
           inputs[2]*weights[2] + 
           inputs[3]*weights[3] + bias) 
print(output) # = 4.8