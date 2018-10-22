import numpy as np
import random
from scipy.linalg import block_diag


B = np.random.randint(0,9, size=(150,150))
B = B/10

A = np.zeros((50,50))
A = A + 0.7
A = block_diag(A,A,A)
C = A==0
A[C] =  0.3

C = B >= A
D = B<A
A[C] = 1
A[D] = 0

row = random.sample(range(0, 150), 150)
row2 = random.sample(range(0, 150), 150)
A[[row]] = A[[row2]]
col = random.sample(range(0, 150), 150)
col2 = random.sample(range(0, 150), 150)
A[[col]] = A[[col2]]

print(A)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0).fit(A)

# kmeans algorithm

def kmeans(k):
    #generate k random centroids

    #assign points to clusters

    #recomputer the controid

    #assign points to cluster
    pass
    #do this till no points move between cluster
