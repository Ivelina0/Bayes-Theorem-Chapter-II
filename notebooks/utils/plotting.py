"""Shared matplotlib styling and figure-saving helper for the Bayes chapter notebooks."""

from pathlib import Path

import matplotlib.pyplot as plt

PALETTE = {
    "true": "#1A365D",       # deep blue - ground truth / exact quantities
    "approx": "#C05621",     # burnt orange - approximate / sampled quantities
    "accent": "#276749",     # forest green - secondary series
    "muted": "#A0AEC0",      # grey - particles, background traces
}


def set_style() -> None:
    plt.rcParams.update(
        {
            "figure.figsize": (7.0, 4.2),
            "figure.dpi": 110,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "font.size": 11,
            "axes.titlesize": 12,
            "axes.titleweight": "bold",
            "legend.frameon": False,
        }
    )


def save_fig(fig, name: str, notebook_dir: str) -> Path:
    """Save `fig` as PNG into `<notebook_dir>/figs/<name>.png` and return the path."""
    out_dir = Path(notebook_dir) / "figs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{name}.png"
    fig.savefig(out_path, bbox_inches="tight")
    return out_path
