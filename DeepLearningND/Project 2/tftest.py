# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:33:20 2017

@author: tim.latham
"""

import tensorflow as tf

# Create TensorFlow object called tensor
hello_constant = tf.constant('Hello World!')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)
    
x = tf.placeholder(tf.string)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
    print(output)
    
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)
    
with tf.Session() as sess:
    x = tf.add(5,2)
    output = sess.run(x)
    print(output)
    x = tf.nn.softmax([2.0, 1.0, 0.2])
    output = sess.run(x)
    print(output)


#tf.Variable()
x = tf.Variable(5)
'''The tf.Variable class creates a tensor with an initial value that can be 
modified, much like a normal Python variable. This tensor stores its state 
in the session, so you must initialize the state of the tensor manually. 
You'll use the tf.global_variables_initializer() function to initialize the 
state of all the Variable tensors.'''

#Initialization
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    
'''The tf.global_variables_initializer() call returns an operation that will 
initialize all TensorFlow variables from the graph. You call the operation 
using a session to initialize all the variables as shown above. Using the 
tf.Variable class allows us to change the weights and bias, but an initial 
value needs to be chosen.

Initializing the weights with random numbers from a normal distribution is 
good practice. Randomizing the weights helps the model from becoming stuck 
in the same place every time you train it. You'll learn more about this in 
the next lesson, when you study gradient descent.

Similarly, choosing weights from a normal distribution prevents any one 
weight from overwhelming other weights. You'll use the tf.truncated_normal()
function to generate random numbers from a normal distribution.'''
 
n_features = 120
n_labels = 5
weights = tf.Variable(tf.truncated_normal((n_features, n_labels)))

n_labels = 5
bias = tf.Variable(tf.zeros(n_labels))
