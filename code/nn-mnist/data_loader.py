
"""
data_loader
~~~~~~~~~~~~
Load the MNIST dataset.
Use ``load()`` method to load dataset.
Check the ``load()`` method for detail.
"""

import os
import urllib2
import gzip
import cPickle
import numpy as np

DATA_PATH = '../.tmp'
DATA_FILENAME = 'mnist.pkl.gz'
DATA_FILE = DATA_PATH + '/' + DATA_FILENAME

def load():
  '''
  Load MNIST dataset.
  This will return tuple of (training_data, validation_data, test_data)
  ``training_data`` is a list of 50,000 training data. Each sample is a tuple ``(x, y)``.
  ``x`` is a 784-dim np.ndarray contains the input image, and ``y`` is a 10-dim np.ndarray for one-hot label vector.
  ``validataion_test`` and ``test_data`` are lists of 10,000 validataion and test data.
  The structure is similar to ``training_data``, except ``y`` is a number corresponding to ``x`` input image.
  '''
  # download data if not exist
  if not os.path.exists(DATA_FILE):
    download()
  
  # load data
  with gzip.open(DATA_FILE, 'rd') as file:
    tr_dt, v_dt, t_dt = cPickle.load(file)
  
  # training data
  inputs = [x.reshape((784, 1)) for x in tr_dt[0]]
  labels = [label_2_vec(y) for y in tr_dt[1]]
  training_data = zip(inputs, labels)
  
  # validation data
  inputs = [x.reshape((784, 1)) for x in v_dt[0]]
  validation_data = zip(inputs, v_dt[1])
  
  # test data
  inputs = [x.reshape((784, 1)) for x in t_dt[0]]
  test_data = zip(inputs, t_dt[1])
  
  return (training_data, validation_data, test_data)

def download():
  '''
  Download MNIST dataset
  '''
  # create data dir if not exist
  if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)
  
  # download
  url = 'https://github.com/mnielsen/neural-networks-and-deep-learning/raw/master/data/mnist.pkl.gz'
  input = urllib2.urlopen(url)
  with open(DATA_FILE, 'wb') as output:
    while True:
      data = input.read(4096)
      if data:
        output.write(data)
      else:
        break
    print('Downloaded MNIST dataset: '+ DATA_FILE)

def label_2_vec(label):
  '''
  One-hot label vector
  '''
  v = np.zeros((10, 1))
  v[label] = 1.0
  return v