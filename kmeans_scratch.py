import numpy as np
from numpy.linalg import norm
import random
import defaultdict 

data = np.loadtxt("/home/coderpad/data/kmeans_data.csv", delimiter = ",")

# n = number of data points
# p = dimension of data 
(n, p) = data.shape

# centers: array of size k * p
# assignments: array of size n, with entries in [0 .. k-1]
# total_square_error: sum of square l2 distances between data points and assigned centers.
def kmeans(data, k):
   
    for i in range(0,3):
    
        # Initials centers 
        init_centers = np.random.rand(data, k)

        # Iterate over each element and compute distance from the center
        for i in len(range(data)):

            for j in len(range(init_centers)):

                dist = []

                dist = init_centers[j] - i

                dist.append(dist)

            assignments = []

            assignments.append(np.argmin(dist))

            # With assignments array, let's recalculate the centers as they were randomly sample previously 

        for i in len(range(data)):

            # create a dict of elements belonging to the cluster
            labels = {}

            labels[assignments[i]].append(i)

        # Compute mean of values of each key in labels
        new_centers = []

        for k, v in labels.items():

            new_centers.append(v.mean())

    return (centers, assignments, total_square_error)
    
    # Function call
    
    # print(kmeans(data, 3))    
