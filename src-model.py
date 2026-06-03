import numpy as np
from sklearn.neighbors import kneighbors_graph
from scipy.sparse.csgraph import laplacian
from scipy.sparse import csr_matrix
from scipy.spatial.distance import cdist

def generate_point_clouds(N0=80, N1=60, dim=3, seed=42):
    np.random.seed(seed)
    X0 = np.random.randn(N0, dim)
    X1 = np.random.randn(N1, dim)
    return X0, X1

def build_hamiltonian(X0, X1, g, k=8, sigma=1.0):
    # Graph Laplacians
    A0 = kneighbors_graph(X0, k, mode='connectivity', include_self=False)
    A0 = A0.maximum(A0.T)
    L0 = laplacian(csr_matrix(A0), normed=True).toarray()
    
    A1 = kneighbors_graph(X1, k, mode='connectivity', include_self=False)
    A1 = A1.maximum(A1.T)
    L1 = laplacian(csr_matrix(A1), normed=True).toarray()
    
    # Bipartite coupling
    dist = cdist(X0, X1)
    W = np.exp(-dist**2 / (2*sigma**2))
    rows, cols, vals = [], [], []
    N0 = len(X0)
    for i in range(N0):
        for j in range(len(X1)):
            rows.append(i)
            cols.append(N0 + j)
            vals.append(W[i,j])
    A_coup = csr_matrix((vals, (rows, cols)), shape=(N0+len(X1), N0+len(X1)))
    A_coup = A_coup + A_coup.T
    L_coup = laplacian(A_coup, normed=True).toarray()
    
    # Full Hamiltonian
    H = np.zeros((N0+len(X1), N0+len(X1)))
    H[:N0, :N0] = L0
    H[N0:, N0:] = L1
    H += g * L_coup
    return H