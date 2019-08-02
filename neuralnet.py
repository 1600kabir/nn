from numpy import exp, random, linspace, dot, zeroes, shape, T
from matplotlib import pyplot as plt
from math import sqrt

class NeuralNetwork:
	def __init__(self, x, y, epochs):
		self.input = x
		self.weights1 = random.randn()
		self.weights2 = random.randn()
		self.y = y 
		self.output = zeros(y.shape)
	def sigmoid(x):
		return 1/(1 + exp(-x))
	def deriv_sigmoid(x):
		return sigmoid(x) * (1-sigmoid(x))
	def feedforward(self):
		self.layer1 = sigmoid(dot(self.X, self.weights1))
		self.layer2 = sigmoid(dot(self.X, self.weights2))
		self.output = sigmoid(dot(self.layer1, weights2))
	def backpropagation(self):
		d_weights2 = dot(self.layer1.T, (2*(self.y - self.output) * deriv_sigmoid(self.output)))
		d_weights1 = dot(self.X.T, dot(2*(self.y - self.output) * deriv_sigmoid(self.output), self.weights2.T) * deriv_sigmoid(self.layer1))
		self.weights1 += d_weights1
		self.weights2 += d_weights2
	def grad_des(self):

	def predict():
		prediction = w1 * guess[0] + w2 * guess[1] + b
		return prediction

