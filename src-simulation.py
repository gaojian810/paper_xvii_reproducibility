import numpy as np
import pandas as pd
from model import generate_point_clouds, build_hamiltonian
from indicators import chi_top, entanglement_entropy

def run_simulation(g_list, N0=80, N1=60, dim=3, beta=100, bootstrap=30):
    X0, X1 = generate_point_clouds(N0, N1, dim)
    results = []
    for g in g_list:
        H = build_hamiltonian(X0, X1, g)
        # ground state probability on empirical layer
        eigvals, eigvecs = np.linalg.eigh(H)
        psi0 = eigvecs[:,0]
        prob0 = psi0[:N0]**2
        prob0 /= prob0.sum()
        idx = np.random.choice(N0, size=200, p=prob0, replace=True)
        cloud = X0[idx]
        chi = chi_top(cloud, bootstrap=bootstrap)
        S = entanglement_entropy(H, beta=beta)
        results.append({'g': g, 'chi_top': chi, 'S_ent': S})
    return pd.DataFrame(results)

if __name__ == '__main__':
    g_vals = np.linspace(0.1, 1.8, 25)
    df = run_simulation(g_vals)
    df.to_csv('../results/tab_numerical.csv', index=False)