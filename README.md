# hydro-ai-foundations

**Machine learning for daily streamflow on a CAMELS basin: from honest baselines to an LSTM, compared with a differentiable conceptual model.**

This repository follows a four-week progression on one CAMELS-US basin (01022500, Maine), so every model is compared on exactly the same data and test period:

1. **Data and signatures**: cleaning, runoff ratio, flow duration curve, hand-written NSE/KGE
2. **Baselines and classic ML**: persistence, climatology, linear regression, random forest, with time-based splits and a leakage demonstration
3. **PyTorch fundamentals**: autograd, a differentiable linear reservoir, an MLP training loop
4. **LSTM**: a sequence-to-one LSTM using only meteorological forcing

The conceptual benchmark comes from my companion project [hbv-torch](https://github.com/charouk/hbv-torch), a differentiable HBV model calibrated on the same basin.

## Results (test period, water years 2006–2014)

<!-- Fill in as each week is completed. -->

| Model | Uses past discharge? | NSE | KGE |
|---|---|---|---|
| Persistence | yes | | |
| Climatology | no | | |
| Linear regression (set A) | no | | |
| Random forest (set A) | no | | |
| MLP | no | | |
| LSTM | no | | |
| Differentiable HBV ([hbv-torch](https://github.com/charouk/hbv-torch)) | no | 0.80* | 0.78* |

\* hbv-torch validation period is 2009–2014; rerun it on 2006–2014 for a strict comparison.

## Notebooks

| Notebook | Content | Status |
|---|---|---|
| [01_data_exploration](notebooks/01_data_exploration.ipynb) | Loading, cleaning, hydrological signatures, metrics | ☐ |
| [02_ml_baselines](notebooks/02_ml_baselines.ipynb) | Baselines, features, time splits, random forest | ☐ |
| [03_pytorch_basics](notebooks/03_pytorch_basics.ipynb) | Tensors, autograd, linear reservoir, MLP | ☐ |
| [04_lstm](notebooks/04_lstm.ipynb) | Sequence-to-one LSTM and final comparison | ☐ |

## Run it

```bash
pip install -e .
pytest            # checks the metrics module
jupyter lab       # open the notebooks
```

Data: the CAMELS time series from NCAR ([doi:10.5065/D6MW2F4D](https://doi.org/10.5065/D6MW2F4D)). Set `CAMELS_ROOT` at the top of each notebook to the folder where you unzipped it.

## What I learned

<!-- Write 4–6 sentences in your own words at the end of Week 4. -->

## References

- Newman, A. J., et al. (2015). *HESS*, 19, 209–223. CAMELS forcing and streamflow.
- Addor, N., et al. (2017). *HESS*, 21, 5293–5313. CAMELS catchment attributes.
- Gupta, H. V., et al. (2009). *Journal of Hydrology*, 377, 80–91. KGE.
- Kratzert, F., et al. (2018). *HESS*, 22, 6005–6022. LSTM rainfall–runoff modelling.

## Author

**Ichrak Boubakri** · [GitHub](https://github.com/charouk) · MIT License
