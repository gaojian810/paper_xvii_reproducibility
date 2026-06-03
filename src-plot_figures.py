import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def fit_exponent(df, col='chi_top', g_c=1.25):
    df['delta'] = np.abs(df['g'] - g_c)
    mask = (df['delta'] > 0.01) & (df['delta'] < 0.5)
    log_delta = np.log(df.loc[mask, 'delta'])
    log_y = np.log(df.loc[mask, col])
    slope, intercept, r, p, se = stats.linregress(log_delta, log_y)
    return -slope

def make_scaling_plot(df, g_c=1.25):
    fig, ax = plt.subplots(1,2, figsize=(10,4))
    df['delta'] = np.abs(df['g'] - g_c)
    mask = (df['delta'] > 0.01) & (df['delta'] < 0.5)
    # chi_top
    ax[0].loglog(df.loc[mask, 'delta'], df.loc[mask, 'chi_top'], 'o-', label='χ_top')
    ax[0].set_xlabel(r'$|g-g_c|$')
    ax[0].set_ylabel(r'$\chi_{\mathrm{top}}$')
    ax[0].legend()
    # S_ent
    ax[1].loglog(df.loc[mask, 'delta'], df.loc[mask, 'S_ent'], 's-', color='red', label='S_ent')
    ax[1].set_xlabel(r'$|g-g_c|$')
    ax[1].set_ylabel(r'$S_{\mathrm{ent}}$')
    ax[1].legend()
    plt.tight_layout()
    plt.savefig('../results/fig_scaling.pdf')
    plt.close()

def make_derivative_plot(df, g_c=1.25):
    df_sorted = df.sort_values('g')
    dS = np.gradient(df_sorted['S_ent'], df_sorted['g'])
    chi = df_sorted['chi_top']
    plt.figure(figsize=(5,4))
    plt.plot(chi, dS, 'o')
    plt.xlabel(r'$\chi_{\mathrm{top}}$')
    plt.ylabel(r'$dS_{\mathrm{ent}}/dg$')
    plt.grid(True)
    plt.savefig('../results/fig_derivative.pdf')
    plt.close()

if __name__ == '__main__':
    df = pd.read_csv('../results/tab_numerical.csv')
    g_c = 1.25
    make_scaling_plot(df, g_c)
    make_derivative_plot(df, g_c)
    alpha = fit_exponent(df, 'chi_top', g_c)
    beta_exp = fit_exponent(df, 'S_ent', g_c)
    print(f'Fitted α = {alpha:.3f}, β = {beta_exp:.3f}')