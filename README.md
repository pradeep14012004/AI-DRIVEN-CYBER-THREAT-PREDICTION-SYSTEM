# AI-Driven Cyber Threat Prediction System

A deep-learning cybersecurity system for predicting and detecting network threats using the CICIDS-2017 dataset.

## Overview

The project combines a **Bi-LSTM**, **Deep Autoencoder**, and a **weighted ensemble** to learn temporal traffic patterns and detect anomalous or malicious network activity.

### Key results

- **98.6% accuracy**
- **0.981 AUC**
- CICIDS-2017 network intrusion dataset
- Hybrid sequence modelling + unsupervised anomaly detection
- Weighted ensemble for final threat prediction

## Evaluation transparency and reproducibility

The values above (98.6% accuracy and 0.981 AUC) are project-reported experimental results. They should be treated as reported results, not independently reproduced by reading this README alone.

For a reproducible research result, publish the following alongside the metrics:

- Exact train, validation, and test split strategy (including whether the split is chronological, stratified, or grouped by flow/day).
- Dataset version/source, selected CICIDS-2017 files, class mapping, and preprocessing steps.
- Feature list, handling of missing/infinite values, normalization fit scope, and any class-balancing procedure.
- Sequence-window length, Bi-LSTM and autoencoder layer sizes, loss functions, optimizer, learning rate, batch size, epochs, and random seeds.
- Weighted-ensemble formula and the method used to select its weights and decision threshold.
- Confusion matrix, per-class precision/recall/F1, macro and weighted averages, ROC-AUC definition, and evaluation script.
- Environment versions and exact commands needed to regenerate the reported tables and plots.

**Data-leakage check:** Fit preprocessing transforms and select thresholds/ensemble weights using training/validation data only. Keep the test set untouched until final evaluation. If multiple flows originate from the same capture/day, document how related records are kept from crossing splits.

Until these details and a clean rerun are committed, do not describe the headline metrics as independently verified or production performance.

## Architecture

```text
CICIDS-2017 Traffic
        |
        v
Preprocessing & Feature Engineering
        |
   +----+----------------+
   |                     |
   v                     v
Bi-LSTM              Deep Autoencoder
   |                     |
   +----------+----------+
              |
              v
       Weighted Ensemble
              |
              v
     Threat Classification
              |
              v
      Prediction / Alert
```

## Methodology

1. Clean and preprocess CICIDS-2017 traffic.
2. Perform feature engineering and normalization.
3. Train the Bi-LSTM to model temporal traffic behaviour.
4. Train the Deep Autoencoder to learn normal traffic representations and identify anomalies.
5. Combine model outputs using a weighted ensemble.
6. Evaluate using accuracy, AUC and other classification metrics.

## Dataset

**CICIDS-2017** is used as the primary network intrusion-detection dataset.

The dataset contains benign traffic and multiple attack categories, making it suitable for supervised and anomaly-based cybersecurity experiments.

> Dataset files are not included in this repository unless redistribution is permitted. Download the dataset from its official/public source and place it in the expected data directory.

## Tech Stack

- Python
- PyTorch / TensorFlow
- NumPy
- Pandas
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

## Project Structure

```text
AI-DRIVEN-CYBER-THREAT-PREDICTION-SYSTEM/
├── data/              # Local dataset files (not committed)
├── notebooks/         # Experiments and analysis
├── src/               # Preprocessing, models and evaluation
├── models/            # Saved model artifacts, when applicable
├── results/           # Metrics and plots
├── tests/             # Tests
├── requirements.txt
├── .gitignore
└── README.md
```

## Reproducibility

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Run the notebooks or project entry point provided in the repository.

## Limitations

- CICIDS-2017 is a benchmark dataset rather than live enterprise traffic.
- Reported performance should not be interpreted as production detection performance.
- Real deployment would require continuous retraining, drift monitoring and validation on organization-specific traffic.

## Research Direction

This project explores the combination of **temporal deep learning and anomaly detection** for intelligent cyber-threat prediction and can be extended toward online detection, explainability and edge deployment.

## License

See the repository license for usage terms.


## Live Demo / Deployment

A lightweight FastAPI browser demo is included in `api/` and can be deployed with the root `Dockerfile`.

```bash
docker build -t cyber-threat-demo .
docker run -p 8000:8000 cyber-threat-demo
```

Open `http://localhost:8000`. The hosted demo uses an explainable screening fallback when trained model artifacts are unavailable; it does not claim the reported 98.6% research result.