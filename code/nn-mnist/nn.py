"""
NN class
~~~~~~~~~~~~~~~~
Neural Network implement class.
This NN use sigmoid as activation functions with cross-entropy cost function.

Usage:
1. Init NN
nn = NN(layers)

2. Train
nn.train((x, y), epochs, mini_batch_size, eta)

3. Predict
y = nn.predict(x)

4. Test / Evaluation
correct_num = nn.evaluate(test_data)
"""
from __future__ import division
import random
import numpy as np

class NN():
    def __init__(self, layers):
        """
        Init NN with ``layers`` size.
        ``layers`` is array of layer sizes.
        E.x: [3, 4, 5, 2] will create a NN of 4 layers.
        In which,
          input layer containts 3 nodes,
         hidden layer 1 contains 4 nodes, 
         hidden layer 2 contains 5 nodes, 
         and, output layer contains 2 nodes
        """
        self.layers = layers
        self.L = len(layers)
        # ``w `` is a list (L-1) dim np.ndarray of matrix W for each layers
        # ``w[0]` is layer 2 (hidden layer 1), ..., ``w[L-2]`` is output layer 
        # Each row hold weights for inputs (from before layer) of correspoding node (on current layer)
        # The first column is bias for correspoding node
        self.w = [np.random.randn(l2, l1 + 1) for l2, l1 in zip(layers[1:], layers[:-1])]
        
    def train(self, train_data, epochs, mini_batch_size, eta):
        """
        Train NN with train data ``[(x, y)]``.
        This use mini-batch SGD method to train the NN.
        """
        # number of training data        
        m = len(train_data)
        # cost
        cost = []
        for j in range(epochs):
            # shuffle data before run
            random.shuffle(train_data)
            # divide data into mini batchs
            for k in range(0, m, mini_batch_size):
                mini_batch = train_data[k:k+mini_batch_size]
                m_batch = len(mini_batch)
                # calc gradient
                w_grad = [np.zeros(W.shape) for W in self.w]
                for x, y in mini_batch:
                    grad = self.backprop(x, y)
                    w_grad = [W_grad + g for W_grad, g in zip(w_grad, grad)]
                w_grad = [W_grad / m_batch for W_grad in w_grad]
                # check grad
                if not self.check_grad(mini_batch):
                    print('backprop fail!')
                    return False
                
                # update w
                self.w = [W - eta * W_grad for W, W_grad in zip(self.w, w_grad)]
            
            # calc cost
            cost.append(self.cost(train_data))
            print('Epoch {0} done'.format(j))
            
        return cost
    
    def predict(self, x):
        """
        Predict label of single input data ``x``
        """
        _, a = self.feedforward(x)
        return np.argmax(a[-1])
    
    def evaluate(self, test_data):
        """
        Evaluate NN with test data.
        This will return the number of correct result
        """
        results = [(self.predict(x), y) for (x, y) in test_data]
        return sum(int(_y == y) for (_y, y) in results)
    
    def cost(self, data):
        """
        Return cost of NN on test data
        """
        return 0
    
    def feedforward(self, x):
        """
        Feedforward through network for calc ``z``,`` a``.
        ``z`` is list of (L-1) vec-tor, ``z[0]`` for layer 2, and so on.
        ``a`` is list of (L) vec-tor, ``a[0]`` for layer 1, and so on.
        """
        z = []
        a = [self.add_bias(x)]
        for l in range(1, self.L):
            z_l = np.dot(self.w[l-1], a[l-1])
            a_l = self.sigmoid(z_l)
            if l < self.L - 1:
                a_l = self.add_bias(a_l)
            
            z.append(z_l)
            a.append(a_l)
            
        return (z, a)
    
    def backprop(self, x, y):
        """
        Backpropagation to calc derivatives
        """
        w_grad = [np.zeros(W.shape) for W in self.w]
        # feedforward
        z, a = self.feedforward(x)
        # backward
        dz = a[-1] - y
        for _l in range(1, self.L):
            l = -_l # layer index
            if l < -1:
                da = self.sigmoid_grad(z[l])
                dz = np.dot(self.w[l+1].transpose(), dz) * da
            # gradient    
            w_grad[l] = np.dot(dz, a[l-1].transpose())
        
        return w_grad
    
    def add_bias(self, a):
        """
        add a_0 = 1 as input for bias w_0
        """
        return np.insert(a, 0, 1, axis=0)
    
    def check_grad(self, test_data):
        return True
    
    def sigmoid(self, z):
        """
        Sigmoid function use as activation function
        """
        return 1.0 / (1.0 + np.exp(-z))
    
    def sigmoid_grad(self, z):
        """
        Result derivative of sigmoid function
        """
        s = self.sigmoid(z)
        return s * (1 - s)