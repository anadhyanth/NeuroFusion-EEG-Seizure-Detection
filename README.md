##NeuroFusion-EEG-Seizure-Detection
A hybrid deep learning framework for EEG seizure detection using numeric and image feature fusion. Designed from scratch using ML and DL approaches, the proposed model achieved 97.19% accuracy, outperforming existing methods through robust EEG feature extraction and classification.

<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<h1 align="center">NeuroFusion EEG Seizure Detection</h1>

<h3 align="center">
Hybrid Deep Learning using Numeric + Image Feature Fusion
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange">
  <img src="https://img.shields.io/badge/Keras-DeepLearning-red">
  <img src="https://img.shields.io/badge/Accuracy-97.19%25-brightgreen">
</p>

---

## Dataset Information

This project uses the BEED EEG Dataset for seizure and non-seizure classification.

Dataset includes:
- Multi-channel EEG recordings
- Seizure and non-seizure samples
- EEG signal segments converted into image representations

Due to GitHub storage limitations, the dataset is not included in this repository.
---

## Proposed Architecture

<p align="center">
  <img src="assets/architecture.png" width="100%">
</p>

---

## EEG Example

<p align="center">
  <img src="assets/eeg_example.png" width="100%">
</p>

---

## Experimental Results

<p align="center">
  <img src="assets/results.png" width="100%">
</p>

---

## Model Weights

This folder stores trained model weights.

Best performing model:
- best_model.h5

Achieved Accuracy:
- 97.19%

---

## Installation

```bash
git clone https://github.com/your-username/NeuroFusion-EEG-Seizure-Detection.git

cd NeuroFusion-EEG-Seizure-Detection

pip install -r requirements.txt
```

---

## Project Structure

```bash
EEG-Seizure-Detection-AI/
│
├── assets/
├── data/
├── models/
├── notebooks/
├── src/
├── app/
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── setup.py
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- MNE
- PyWavelets
- Scikit-learn
- Streamlit
- NumPy
- Pandas
- Matplotlib

---

## Key Highlights

- Designed completely from scratch
- Hybrid Numeric + Image Feature Fusion
- ML to Deep Learning Pipeline
- Achieved 97.19% Accuracy
- Outperformed Existing Methods
- EEG Signal to Image Conversion
- Robust Seizure Classification Framework

---

## Future Improvements

- Real-time EEG seizure monitoring
- Transformer-based EEG modeling
- Edge AI deployment
- Explainable AI integration
- Clinical deployment optimization

---
