from .utils import classify

def find_cluster(means, items):
	clusters = [[] for i in range(len(means))] # Init clusters

	for item in items:

		# Classify item into a cluster
		index = classify(means, item)

		# Add item to cluster
		clusters[index].append(item)

	return clusters