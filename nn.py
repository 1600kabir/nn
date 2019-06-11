from numpy import exp, random, linspace
from matplotlib import pyplot as plt
from math import sqrt

data = [[3, 1.5, 1],
		[2, 1, 0],
		[4, 1.5, 1],
		[3, 1, 0],
		[3.5, .5, 1],
		[2, .5, 0],
		[5.5, 1, 1],
		[1, 1, 0]]
guess = [4.5, 1.5]



def sigmoid(x):
	return 1/(1 + exp(-x))

def sigmoid_p(x):
	return sigmoid(x) * (1-sigmoid(x))

X = linspace(-5, 5, 100)
Y = sigmoid(X)
Y2 = sigmoid_p(X)


def scatter_initdata():
	for i in range(len(data)):
		point = data[i]
		color = "r"
		if point[2] == 0:
			color = "b"
		plt.scatter(point[0], point[1], c=color)
	plt.show()

def train():
	
	w1 = random.randn()
	w2 = random.randn()
	b = random.randn()

	train_loops = 1000000
	learning_rate = 0.1
	cost = []
	for i in range(0, train_loops):
		ri = random.randint(len(data))
		point = data[ri]

		z = point[0] * w1 + point[1] * w2 * b

		pred = sigmoid(z)
		target = point[2]
		
		cost = [(pred - target)]
		#add costs to list
		if i % 100 == 0:
			c = 0
			for j in range(len(data)):
				p = data[j]
				p_pred = sigmoid(w1 * p[0] + w2 * p[1] + b)
				c += .5 ** (p_pred - p[2])
			cost.append(c)
		
		dcost_pred = 2 * (pred - target)
		dpred_dz = sigmoid_p(z)
		dz_dw1 = point[0]
		dz_dw2 = point[1]
		dz_db = 1
		#partial deriv
		dcost_dw1 = dcost_pred * dpred_dz * dz_dw1
		dcost_dw2 = dcost_pred * dpred_dz * dz_dw2
		dcost_db = dcost_pred * dpred_dz * dz_db

		w1 = w1 - learning_rate * dcost_dw1
		w2 = w2 - learning_rate * dcost_dw2
		b = b - learning_rate * dcost_db

		return cost, w1, w2, b

cost, w1, w2, b = train()


def predict():
	z = w1 * guess[0] + w2 * guess[1] + b
	pred = sigmoid(z)
	if pred < .5:
		print("green flower, close to 0")
	else:
		print("orange flower, close to 1")

predict()
