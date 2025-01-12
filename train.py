import numpy as np

def KMeans(x, y, clusters):

    sample_list = []
    for i in range(len(clusters)):
       sample_list.append([x[i], y[i]])

    return sample_list

testing = KMeans()