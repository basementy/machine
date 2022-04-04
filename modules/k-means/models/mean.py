import sys

from random import uniform

from .utils import classify

def find_col_min_max(items):
    number = len(items[0])

    min = [sys.maxsize for i in range(number)]
    max = [-sys.maxsize -1 for i in range(number)]

    for item in items:
      for f in range(len(item)):
        if (item[f] < min[f]):
          min[f] = item[f]

        if (item[f] > max[f]):
          max[f] = item[f]

    return min, max

def initialize_means(items, k, column_min, column_max):
	# Initialize means to random numbers between the min and max of each column/feature
	features_length = len(items[0]) # number of features

	means = [[0 for i in range(features_length)] for j in range(k)]

	for mean in means:
		for position in range(len(mean)):
			# Set value to a random float
			# (adding +-1 to avoid a wide placement of a mean)
			mean[position] = uniform(column_min[position] + 1, column_max[position] - 1)

	return means

def update_mean(n, means, item):
	for i in range(len(means)):
		mean = means[i]
		mean = (mean * (n-1) + item[i]) / float(n)
		means[i] = round(mean, 3)

	return means

def calculate_means(k, items, maxIterations=100000):
	# Find the min and max for columns
	column_min, column_max = find_col_min_max(items)

	# Initialize means at random points
	means = initialize_means(items, k, column_min, column_max)

	# Initialize clusters, the array to hold
	# the number of items in a class
	cluster_sizes = [0 for i in range(len(means))]

	# An array to hold the cluster an item is in
	belongs_to = [0 for i in range(len(items))]

	# Calculate means
	for e in range(maxIterations):

		# If no change of cluster occurs, halt
		no_change = True

		for i in range(len(items)):
			item = items[i]

			# Classify item into a cluster and update the
			# corresponding means.
			index = classify(means, item)

			cluster_sizes[index] += 1
			cluster_size = cluster_sizes[index]

			means[index] = update_mean(cluster_size, means[index], item)

			# Item changed cluster
			if(index != belongs_to[i]):
				no_change = False

			belongs_to[i] = index

		# Nothing changed, return
		if (no_change):
			break

	return means