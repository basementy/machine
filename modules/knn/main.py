# Daniela Marioti, Gabriel Back e Gabriel de Oliveira, Gabriel Back

import os

from csv import reader

from with_lib import calculate_knn_with_lib
from without_lib import calculate_knn_without_lib

def load_file(rawFilename):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, rawFilename)

    with open(filename, 'r') as file:
        return list(reader(file))

if __name__ == "__main__":
    local_dataset = load_file('dataset.csv')
    local_dataset_target = local_dataset[42]

    n_neighbors = 3

    result_with_lib = calculate_knn_with_lib(n_neighbors)
    result_without_lib = calculate_knn_without_lib(local_dataset, local_dataset_target, n_neighbors)

    print("Result with library (iris dataset w/ points check): ", result_with_lib)
    print("Result without library (local dataset w/ only one target): ", result_without_lib)