from simulation import run_simulation
import pandas as pd
import numpy as np

beta_list = [50, 100, 200]
g_vals = np.linspace(0.1, 1.8, 25)
all_results = []
for beta in beta_list:
    df = run_simulation(g_vals, beta=beta)
    df['beta'] = beta
    all_results.append(df)
combined = pd.concat(all_results)
combined.to_csv('../results/tab_beta_sensitivity.csv', index=False)