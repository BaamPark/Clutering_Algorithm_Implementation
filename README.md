# Clutering_Algorithm_Implementation

This repository contains three Python scripts: k-means clustering.py, hierarchical_clustering.py, and socket server file.py. These scripts implement different clustering algorithms and a socket server for communication.

`k_mean_clustering.ipynb`

This script implements the k-means clustering algorithm, which is a popular unsupervised learning algorithm used for clustering. The script takes input data in the form of a CSV file and a value for k, the number of clusters to be formed. The algorithm assigns each data point to the nearest centroid and then recomputes the centroid of each cluster. The process is repeated until convergence or until a specified number of iterations is reached. The output of the script is a CSV file containing the cluster assignments for each data point.

`hierarchical_clustering.ipynb`

This script implements the hierarchical clustering algorithm, which is another unsupervised learning algorithm used for clustering. The script takes input data in the form of a CSV file and a distance metric to be used. The algorithm starts by treating each data point as a separate cluster and then iteratively merges the closest pair of clusters until all the points are in a single cluster. The output of the script is a dendrogram visualizing the clustering hierarchy.

`socket server file.py`

This script implements a socket server that receives data from clients, processes it, and stores it in a CSV file. The CSV file contains measures of accelerometers and gyroscopes that are obtained from mobile device.
