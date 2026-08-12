# Induction Motor Bearing Fault Diagnosis (CWRU Dataset)

This repository contains Python scripts for analyzing drive-end bearing faults using time-domain signal processing and Fast Fourier Transform (FFT) analysis on the CWRU dataset.

## Project Structure
* `inspect_data.py`: Loads MATLAB `.mat` files, extracts raw signal arrays, and inspects dataset structure.
* `step2_plot_time.py`: Plots and compares healthy vs. faulty time-domain waveforms to analyze vibration/current amplitude changes.
* `step 3`: Applies Fast Fourier Transform (FFT) to convert time-domain signals into the frequency domain and isolate fault characteristic frequencies.

## Requirements & Libraries
* Python 3.x
* `numpy`
* `scipy`
* `matplotlib`

## How to Run
```bash
python inspect_data.py
python step2_plot_time.py
