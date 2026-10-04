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
