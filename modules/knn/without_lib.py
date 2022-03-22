import os

from csv import reader
from math import sqrt

def load_file(rawFilename):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, rawFilename)

    with open(filename, 'r') as file:
        return list(reader(file))

def euclidean_distance(train, test):
    distance = 0

    for i in range(len(train) - 1):
        distance += (float(train[i]) - float(test[i])) ** 2

    return sqrt(distance)

def get_result(neighbors):
    class_votes = {}

    for neighbor in neighbors:
        response = neighbor[-1]

        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1

    sorted_votes = sorted(class_votes.items(), key=lambda x: x[1], reverse=True)

    return sorted_votes[0][0]

def calculate_knn_without_lib(train, test, k):
    distances = []

    for row in train:
        dist = euclidean_distance(row, test)
        distances.append((dist, row))

    distances.sort(key=lambda x: x[0])

    neighbors = []

    for i in range(k):
        neighbors.append(distances[i][1])

    return get_result(neighbors)