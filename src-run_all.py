import subprocess
import os

if __name__ == '__main__':
    os.makedirs('../results', exist_ok=True)
    print("Running simulation...")
    subprocess.run(['python', 'simulation.py'])
    print("Running sensitivity analysis...")
    subprocess.run(['python', 'sensitivity_analysis.py'])
    print("Generating figures...")
    subprocess.run(['python', 'plot_figures.py'])
    print("All done. Results saved in ../results/")