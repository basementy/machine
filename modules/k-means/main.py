# Daniela Marioti e Gabriel de Oliveira

import os

from random import shuffle

from models.cluster import find_cluster
from models.mean import calculate_means

# Read the file, splitting by lines and convert feature value to float
def read_data(raw_filename):
	dirname = os.path.dirname(__file__)
	filename = os.path.join(dirname, raw_filename)

	file = open(filename, 'r')
	lines = file.read().splitlines()

	file.close()

	items = []

	for i in range(1, len(lines)):
		line = lines[i].split(',')
		item_features = []

		for j in range(len(line)-1):
			feature_value = float(line[j])

			# Add feature value to dict
			item_features.append(feature_value)

		items.append(item_features)

	shuffle(items)

	return items

def print_items(items):
	for i in range(len(items)):
		print("Item " + str(i) + ": " + str(items[i]))

def print_means(means):
	for i in range(len(means)):
		print("Mean " + str(i) + ": " + str(means[i]))

def print_clusters(clusters):
	for i in range(len(clusters)):
		print("Cluster " + str(i) + ": ")

		for j in range(len(clusters[i])):
			print("Item " + str(j) + ": " + str(clusters[i][j]))

		print()

if __name__ == "__main__":
    items = read_data("dataset.txt")
    means = calculate_means(3, items, 300)
    clusters = find_cluster(means, items)

    print("--- Items")
    print_items(items)
    print()

    print('--- Means')
    print_means(means)
    print()

    print('--- Clusters')
    print_clusters(clusters)