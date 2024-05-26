# since the ReLU function has no context and each of its outputs are exclusive of each other
# The softmax function adds context producing normalized distributions of probablilites 
# with input data this function predicts/thinks what class/category each input data represents (representing confidence scores for each class)

layers_outputs = [4.8, 1.21, 2.385]

E = 2.71828182846

exp_values = []
for output in layers_outputs:
    exp_values.append(E**output)
print('exponentiated values:')
print(exp_values)