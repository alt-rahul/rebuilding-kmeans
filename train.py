import numpy as np

def KMeans(x, y, clusters):
    sample_x = x
    sample_y = y
    sample_list = []
    for i in range(len(clusters)):
        