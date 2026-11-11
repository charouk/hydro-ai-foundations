"""Hydrological metrics — Exercise 1.6: write these yourself.

Run `pytest tests/test_metrics.py` to check your work. All tests pass = exercise done.
"""
from __future__ import annotations

import numpy as np


def nse(obs: np.ndarray, sim: np.ndarray) -> float:
    """Nash–Sutcliffe efficiency.

    NSE = 1 - sum((sim - obs)^2) / sum((obs - mean(obs))^2)

    Must ignore time steps where obs is NaN.
    """
    raise NotImplementedError("Exercise 1.6: implement NSE")


def kge(obs: np.ndarray, sim: np.ndarray) -> float:
    """Kling–Gupta efficiency (Gupta et al., 2009).

    KGE = 1 - sqrt((r - 1)^2 + (alpha - 1)^2 + (beta - 1)^2)
      r     = Pearson correlation between obs and sim
      alpha = std(sim) / std(obs)
      beta  = mean(sim) / mean(obs)

    Must ignore time steps where obs is NaN.
    """
    raise NotImplementedError("Exercise 1.6: implement KGE")


def pbias(obs: np.ndarray, sim: np.ndarray) -> float:
    """Percent bias: 100 * sum(obs - sim) / sum(obs). Positive = model underestimates."""
    raise NotImplementedError("Exercise 1.6 (bonus): implement PBIAS")
