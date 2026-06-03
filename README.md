markdown
# Reproducibility package for Paper XVII: Cognitive Entanglement Entropy

This repository contains all code and instructions to reproduce the numerical experiments and figures in the paper:

> **Cognitive Entanglement Entropy and Critical Scaling in the Pyramid Knowledge Manifold**  
> Jian Gao, *Physica A* (submitted)

## Requirements

- Python 3.11 or later
- Packages listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/gaojian810/paper_xvii_reproducibility.git
   cd paper_xvii_reproducibility
Create a virtual environment (optional but recommended):

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Usage
Run the full pipeline with a single command:

bash
python src/run_all.py
This will:

Generate the two-layer point clouds.

Scan coupling parameter g from 0.1 to 1.8.

Compute χ_top and S_ent for each g.

Perform β sensitivity analysis (β = 50, 100, 200).

Produce results/fig_scaling.pdf and results/fig_derivative.pdf.

Save numerical tables as CSV files.

Output figures and tables will appear in the results/ directory.

Reproducibility with Docker
To run in an isolated container:

bash
docker build -t paper_xvii .
docker run --rm -v $(pwd)/results:/app/results paper_xvii
File descriptions
src/model.py: constructs the Hamiltonian H = L0 + L1 + g*L_coup.

src/indicators.py: functions for chi_top (persistent homology) and S_ent (density matrix).

src/simulation.py: main loop over g.

src/sensitivity_analysis.py: repeats for β = 50,100,200.

src/plot_figures.py: generates the two PDF figures.

src/run_all.py: orchestrates everything.

License
MIT (see LICENSE file).

Citation
If you use this code, please cite the paper and this Zenodo archive:

Gao, Jian (2026). Cognitive Entanglement Entropy and Critical Scaling in the Pyramid Knowledge Manifold (Version v1.0). Zenodo. https://doi.org/10.5281/zenodo.20428686

