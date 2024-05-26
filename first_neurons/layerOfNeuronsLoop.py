inputs = [1, 2, 3, 2.5]
weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]
biases = [2,3,.5]

layer_output = [] 

for neuron_weights, neuron_bias in zip(weights, biases): # zip pairs the weights with the biases (weights = [.2, .8, -.5, 1] is paired with the bias value 2 for example)
    neuron_output = 0 # creating an empty initialized variable to throw each neuron output value
    
    for n_input, weight in zip(inputs, neuron_weights): # input is paired with its corresponding weight values
        neuron_output += n_input*weight # summing all the multiplied input and weights together
    
    neuron_output += neuron_bias # adding the biases to the summed inputs and weights
    layer_output.append(neuron_output) # throwing these new mathed values to this list
print(layer_output)