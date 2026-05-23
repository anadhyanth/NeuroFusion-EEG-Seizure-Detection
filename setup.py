from setuptools import setup, find_packages

setup(
    name="NeuroFusion-EEG-Seizure-Detection",
    version="1.0.0",
    author="Manu",
    description="Hybrid Deep Learning Framework for EEG Seizure Detection using Numeric and Image Feature Fusion",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "tensorflow",
        "keras",
        "opencv-python",
        "mne",
        "PyWavelets",
        "streamlit"
    ],
)