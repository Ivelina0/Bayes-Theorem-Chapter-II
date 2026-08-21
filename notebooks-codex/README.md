# notebooks-codex

Clean notebook workspace for the post-1950 computational Bayes section of the chapter.

This folder is intentionally independent of `notebooks-claude`.

## Structure

- `00_shared/`
  Shared helpers, plotting utilities, and common references.
- `01_metropolis_hastings/`
  Posterior sampling with a simple Metropolis-Hastings example.
- `02_particle_filtering/`
  Sequential Bayesian state estimation with a particle filter.
- `03_particle_degeneracy/`
  Genealogical/path degeneracy after repeated resampling.
- `04_variational_inference/`
  Variational approximation versus an exact or reference posterior.
- `05_gaussian_processes/`
  Prior and posterior uncertainty over functions.
- `06_bayesian_optimisation/`
  GP surrogate modelling and acquisition-based experiment selection.
- `07_hierarchical_bayes/`
  Partial pooling and hierarchical modelling.
- `08_probabilistic_programming/`
  BUGS/Stan/PyMC-style modelling workflow.
- `data/`
  Local datasets copied or prepared for offline notebook use.
- `figs/`
  Shared exported figures if needed.

## Environment

The virtual environment for this workspace lives in:

```text
notebooks-codex/.venv
```

Activate it on Windows PowerShell with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then install dependencies with:

```powershell
pip install -r requirements.txt
```

## Notebook design rule

Each notebook should follow the same order:

1. Historical problem and motivation
2. Data or simulation setup
3. Minimal mathematics
4. Code implementation
5. Diagnostics and plots
6. Interpretation
7. Original paper and textbook references
