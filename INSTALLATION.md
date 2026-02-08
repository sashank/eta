# Module 09 Network Traffic Profiling - Installation Guide

## Quick Start

### Option 1: Minimal Installation (Recommended)
Install core dependencies needed for all exercises:

```bash
pip install -r requirements-minimal.txt
```

This includes all packages needed for Exercises 9.1b, 9.2a, 9.3a (basic), 9.3b, and 9.5a.

### Option 2: Full Installation with Comments
Review the detailed requirements file with explanations:

```bash
pip install -r requirements.txt
```

## Optional Packages

### Deep Learning (Exercise 9.3a - Advanced Models)
For LSTM and CNN models in application identification:

```bash
pip install tensorflow>=2.15.0
```

**GPU Support (Optional):**
```bash
pip install tensorflow[and-cuda]
```

### Network Packet Analysis (Exercise 9.1b - Live Capture)
For real packet capture and analysis with Scapy:

**Windows:**
1. Install [Npcap](https://npcap.com/#download) (Windows packet capture library)
2. Install Scapy:
   ```bash
   pip install scapy>=2.5.0
   ```

**Linux:**
```bash
sudo apt-get install libpcap-dev
pip install scapy>=2.5.0
```

**macOS:**
```bash
brew install libpcap
pip install scapy>=2.5.0
```

**Note:** Exercises work with simulated data if Scapy is not installed.

## Python Version Requirements

- **Supported:** Python 3.9, 3.10, 3.11
- **Not Recommended:** Python 3.12+ (some dependencies may have compatibility issues)

Check your Python version:
```bash
python --version
```

## Virtual Environment Setup (Recommended)

### Using venv (Standard)
```bash
# Create virtual environment
python -m venv venv-module09

# Activate (Windows PowerShell)
.\venv-module09\Scripts\Activate.ps1

# Activate (Windows Command Prompt)
.\venv-module09\Scripts\activate.bat

# Activate (Linux/macOS)
source venv-module09/bin/activate

# Install dependencies
pip install -r requirements-minimal.txt
```

### Using conda
```bash
# Create environment
conda create -n module09 python=3.11

# Activate
conda activate module09

# Install dependencies
pip install -r requirements-minimal.txt
```

## Verification

After installation, verify key packages:

```python
# Run in Python or Jupyter
import numpy as np
import pandas as pd
import sklearn
import xgboost
import flask
from imblearn.over_sampling import SMOTE

print("✅ All core packages installed successfully!")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
```

## Troubleshooting

### Issue: "No module named 'xxx'"
**Solution:** Install the missing package:
```bash
pip install xxx
```

### Issue: XGBoost installation fails on Windows
**Solution:** Try installing from conda-forge:
```bash
conda install -c conda-forge xgboost
```

### Issue: TensorFlow installation fails
**Solution:** Install specific version:
```bash
pip install tensorflow==2.15.0
```

### Issue: Scapy not capturing packets on Windows
**Solution:**
1. Verify Npcap is installed
2. Run terminal/Jupyter as Administrator
3. Check firewall settings

### Issue: Jupyter kernel not found
**Solution:** Install and register the kernel:
```bash
python -m ipykernel install --user --name=module09
```

## Exercise-Specific Dependencies

### Exercise 9.1b (Observable Features)
- **Required:** numpy, pandas, matplotlib, seaborn
- **Optional:** scapy (for live packet analysis)
- **Alternative:** Works with simulated data without scapy

### Exercise 9.2a (TLS Fingerprinting)
- **Required:** numpy, pandas, matplotlib, seaborn, scikit-learn
- **Data:** Simulated TLS handshakes (no external dependencies)

### Exercise 9.3a (Application Identification)
- **Required:** numpy, pandas, scikit-learn, flask
- **Optional:** tensorflow (for LSTM/CNN models)
- **Note:** Random Forest works without TensorFlow

### Exercise 9.3b (Malware Traffic Detection)
- **Required:** numpy, pandas, scikit-learn, imbalanced-learn, xgboost
- **Critical:** imbalanced-learn for SMOTE (handles class imbalance)

### Exercise 9.5a (Mercury Feature Extraction)
- **Required:** numpy, pandas, matplotlib, seaborn
- **Note:** Uses multiprocessing (built-in) for parallel processing

## Performance Optimization (Optional)

For faster computation on large datasets:

```bash
pip install numba bottleneck
```

## Google Colab Alternative

If you prefer not to install packages locally, all exercises run on Google Colab:

1. Upload the notebook to Google Colab
2. Add this cell at the top:
   ```python
   !pip install imbalanced-learn xgboost flask-cors
   ```
3. Run exercises normally

**Note:** Scapy may not work on Colab (use simulated data mode).

## Dataset Notes

All exercises use simulated or built-in datasets. No external dataset downloads required for basic functionality.

For advanced exploration:
- **CICIDS2017:** Network intrusion dataset
- **CTU-13:** Malware traffic captures
- Available via course data repository (see main README)

## Support

For package-related issues:
1. Check package documentation: [PyPI](https://pypi.org/)
2. Review error messages carefully
3. Try upgrading pip: `pip install --upgrade pip`
4. Check Python version compatibility

For exercise-specific questions, refer to individual exercise README files.

---

**Last Updated:** February 2026  
**Tested On:** Windows 11, Ubuntu 22.04, macOS Sonoma  
**Python Versions:** 3.9.18, 3.10.13, 3.11.7
