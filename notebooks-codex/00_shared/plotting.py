from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def set_plot_style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (8, 5),
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlesize": 14,
            "axes.labelsize": 11,
            "legend.frameon": False,
            "figure.dpi": 120,
        }
    )


def save_fig(fig: plt.Figure, target: str | Path, dpi: int = 180) -> None:
    path = Path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
