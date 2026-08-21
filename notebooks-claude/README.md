# Code companions for the Bayesian computational-revolution chapter

Each notebook below pairs one algorithm from `bayes_29_07_2026.tex` with a runnable,
worked example. They are self-contained — read/run any one of them independently.

| Notebook | Chapter section | What it shows |
|---|---|---|
| [`01_metropolis_hastings`](01_metropolis_hastings/01_metropolis_hastings_vaccine_trial.ipynb) | §*Physics Origins: The Metropolis–Hastings Framework* (`sec:mcmc-history`) | A hand-rolled Metropolis–Hastings sampler recovering the exact Beta posterior for a real vaccine-trial efficacy rate |
| [`02_particle_filter_tracking`](02_particle_filter_tracking/02_particle_filter_bearings_tracking.ipynb) | §*Bayes through time: state-space models, Kalman filtering and particle filters* | Sequential Bayesian tracking of a simulated spacecraft from noisy bearing-only measurements; where a Kalman filter breaks down and a bootstrap particle filter doesn't |
| [`03_particle_degeneracy`](03_particle_degeneracy/03_particle_degeneracy_ancestry.ipynb) | Same section, "genealogical or path degeneracy" paragraph | Tracing particle ancestry through resampling to see why reconstructing early states (smoothing) becomes hard |
| [`04_variational_inference`](04_variational_inference/04_variational_inference_banana.ipynb) | §*Variational inference: turning inference into optimisation* (`sec:bayes-computational-history`) | Mean-field Gaussian VI fit to an awkward, correlated 2D posterior, and where the approximation visibly fails |
| [`05_gaussian_processes`](05_gaussian_processes/05_gaussian_processes_co2.ipynb) | §*Random functions, Gaussian processes and kernels* (`sec:bayes-modelling`) | A GP fit to the real Mauna Loa CO2 record — the standard textbook GP example — with forward extrapolation and uncertainty bands |
| [`06_bayesian_optimisation`](06_bayesian_optimisation/06_bayesian_optimisation_hyperparam_tuning.ipynb) | §*Bayesian optimisation: using probability to decide what to try next* (`sec:bayes-ml`) | Tuning a real classifier's hyperparameter with a GP surrogate + expected improvement, benchmarked against random search — the same kind of tuning DeepMind used on AlphaGo |

## Setup

From the `notebooks/` directory:

```bash
python -m venv ../.venv          # if not already created
../.venv/Scripts/activate        # Windows; use `source ../.venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
jupyter notebook
```

**Windows + OneDrive note:** if this repo lives under a long OneDrive-synced path,
`pip install` can fail partway through with `OSError: [Errno 2] No such file or
directory` on deeply nested package files (seen with `jupyterlab` and `jedi`), because
the full destination path exceeds Windows' ~260-character limit. If that happens,
create the venv at a short path outside the repo instead, e.g.:

```powershell
python -m venv C:\venvs\bayes-theorem-ii
C:\venvs\bayes-theorem-ii\Scripts\activate
pip install -r requirements.txt
```

## Notes

- Notebooks use only real, hardcoded or library-bundled data (no network fetches at
  run time), so they run offline.
- Where a notebook cites a paper that doesn't yet have a `references.bib` entry in the
  main chapter (e.g. the particle-filter, variational-inference, Gaussian-process and
  Bayesian-optimisation papers), the full citation is written out in the notebook's
  markdown directly rather than added to `references.bib` — that's left as a follow-up
  if/when this material gets folded into the chapter's prose.
- `utils/plotting.py` holds a shared matplotlib style and a `save_fig` helper so every
  notebook's figures look consistent and land in that notebook's own `figs/` folder.
