import sys
import math

def euclidean_distance(x, y):
	sum = 0 # The sum of the squared differences of the elements

	for position in range(len(x)):
		sum += math.pow(x[position]-y[position], 2)

	# The square root of the sum
	return math.sqrt(sum)

def classify(means, item):
	# Classify item to the mean with minimum distance
	minimum_distance = sys.maxsize
	index = -1

	for mean in range(len(means)):

		# Find distance from item to mean
		distance = euclidean_distance(item, means[mean])

		if (distance < minimum_distance):
			minimum_distance = distance
			index = mean

	return index