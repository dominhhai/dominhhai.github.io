"""
NN class
~~~~~~~~~~~~
Neural Network implement class.
This NN use sigmoid as activation functions with cross-entropy cost function.

E.x:
# init NN of 5 layers with
# * input layer: 784 nodes
# * output layer: 10 nodes
# * 2 hidden layers: each contains 100 nodes
nn = new NN((784, 100,  100, 10))

# train data
nn.train((x, y), epochs, mini_batch_size, eta)

# predict
y = nn.predict(x)
"""

import random
import numpy as np

class NN(object):
    def __init__(self, layers):
        """
        Init NN with ``layers`` size
        """
        self.layers = layers
        self.L = len(layers)
        # ``w `` is a list (L-1) dim np.ndarray of matrix W for each layers
        # Each row hold weights for inputs (from before layer) of correspoding node (on current layer)
        #  However, the first column is bias for correspoding node
        self.w = [np.random.randn(l2, l1 + 1) for l2, l1 in zip(sizes[1:], sizes[:-1])]
        
    def train(self, data, epochs, mini_batch_size, eta):
        """
        Train NN with data ``(x, y)``
        """
        
        print(data)
     
    def predict(self, x):
        """
        Predict label for input image ``x``
        """
        _, a = self.feedforward(x)
        return np.argmax(a[self.L-1])
    
    def cost(self, x):
        
        return 0
    
    def feedforward(self, x):
        z = []
        a = [x]
        for l in range(1, self.L):
            z_l =  np.dot(W, a[l-1])
            a_l = self.sigmoid(z)
            z.append(z_l)
            a.append(a_l)
        return (z, a)
    
    def backprop(self, x, y):
        return 0
    
    def update_mini_batch(self, mini_batch, eta):
        return 0
    
    def sigmoid(self, z):
        # Sigmoid
        return 1.0 / (1.0 + np.exp(-z))
    
    def sigmoid_prime(self, z):
        #  Derivative of activation function
        sz = self.sigmoid(z)
        return sz * (1 - sz)
    
    def softmax(self, z):
        sz = np.exp(z)
        return sz / np.sum(sz, axis=1, keepdims=True)
    
    