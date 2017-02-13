# TensorFlow
import tensorflow as tf


# ########### #
# Basic Setup #
# ########### #

# sensor input
input_size  = 67
# output classes (7 degrees of freedom)
num_classes = 7

# --- Basic Setup --- #



# ##### #
# Input #
# ##### #


# Data Layer
# 67 neurons

dataLayer = tf.placeholder(tf.float64, shape=[None, 67])

data_weights = tf.Variable(tf.zeros([67, 256]))
data_bias    = tf.Variable(tf.zeros([None, 256]))


# LSTM Layer
# 256 neuros

# Fully Connected Layer
# 128 neurons

# fc1 = <connection to LSTM>
fc1_weights = tf.Variable(tf.zeros([128, 128], dtype=tf.float64), dtype=tf.float64)
fc1_bias    = tf.Variable(tf.zeros([128], dtype=tf.float64), dtype=tf.float64)

# Fully Connected Layer
# 128  neurons

fc2 = tf.tanh(tf.matmul(fc1, fc1_weights) + fc1_bias)
fc2_weights = tf.Variable(tf.zeros([128, 64], dtype=tf.float64), dtype=tf.float64)
fc2_bias    = tf.Variable(tf.zeros([64], dtype=tf.float64), dtype=tf.float64)

# Filly Connected Layer
# 64 neurons

fc3 = tf.tanh(tf.matmul(fc2, fc2_weights) + fc2_bias)
fc3_weights = tf.Variable(tf.zeros([64, 7], dtype=tf.float64), dtype=tf.float64)
fc3_bias    = tf.Variable(tf.zeros([7], dtype=tf.float64), dtype=tf.float64)

# Pose Estimate
# 7 neurons

output = tf.matmul(fc3, fc3_weights) + fc3_bias
estimate = tf.placeholder(tf.float64, shape=[None, 7])
