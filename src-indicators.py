import numpy as np
from ripser import ripser
from scipy.linalg import eigh

def chi_top(point_cloud, bootstrap=30):
    n = len(point_cloud)
    Qs = []
    for _ in range(bootstrap):
        idx = np.random.choice(n, int(0.8*n), replace=False)
        sub = point_cloud[idx]
        dgms = ripser(sub, maxdim=1)['dgms']
        h1 = dgms[1]
        if len(h1) == 0:
            Qs.append(0.0)
        else:
            lifetimes = h1[:,1] - h1[:,0]
            Qs.append(np.max(lifetimes))
    return np.var(Qs)

def entanglement_entropy(H, beta=100):
    eigvals, eigvecs = eigh(H)
    prob = np.exp(-beta * eigvals)
    prob = prob / np.sum(prob)
    rho = np.zeros_like(H, dtype=float)
    for i in range(len(eigvals)):
        rho += prob[i] * np.outer(eigvecs[:,i], eigvecs[:,i])
    # reduce to empirical layer (first N0 indices)
    N0 = int(H.shape[0] / 2)  # approximate, better to pass N0 explicitly
    rho_A = rho[:N0, :N0]
    ev = np.linalg.eigvalsh(rho_A)
    ev = ev[ev > 1e-12]
    S = -np.sum(ev * np.log(ev))
    return S