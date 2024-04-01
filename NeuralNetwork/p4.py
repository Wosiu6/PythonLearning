import numpy as np

inputs = [[1, -2, 3, 2.5]
          , [2, 3, -4, 5.5]
          , [6, 7, -8, 0.5]]

weights = [[0.2, 0.8, -0.5, 1.0]
           , [0.5, -0.91, 0.26, -0.5]
           , [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

weights2 = [[0.2, 5.8, -0.5]
           , [0.5, -6.91, 0.26]
           , [-0.26, -0.27, 7.17]]

biases2 = [12, 6, 1.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
print(layer1_outputs)

layer_2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print(layer_2_outputs)