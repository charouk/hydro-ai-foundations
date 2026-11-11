"""Exercise 1.6 'Done when' checks. Run: pytest tests/test_metrics.py"""
import numpy as np
import pytest

from hydroai.metrics import kge, nse, pbias

rng = np.random.default_rng(0)
OBS = rng.gamma(2.0, 1.5, size=500)


def test_nse_perfect_is_one():
    assert nse(OBS, OBS) == pytest.approx(1.0)


def test_nse_mean_is_zero():
    assert nse(OBS, np.full_like(OBS, OBS.mean())) == pytest.approx(0.0, abs=1e-12)


def test_nse_ignores_nan():
    obs = OBS.copy()
    obs[::10] = np.nan
    sim = OBS * 1.1
    valid = ~np.isnan(obs)
    assert nse(obs, sim) == pytest.approx(nse(obs[valid], sim[valid]))


def test_kge_perfect_is_one():
    assert kge(OBS, OBS) == pytest.approx(1.0)


def test_kge_detects_bias():
    # doubling the flow keeps r = 1 but alpha = beta = 2  ->  KGE = 1 - sqrt(2)
    assert kge(OBS, 2 * OBS) == pytest.approx(1 - np.sqrt(2))


def test_pbias_sign():
    assert pbias(OBS, 0.9 * OBS) == pytest.approx(10.0)
