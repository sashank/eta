# Module 09: Network Traffic Profiling - Exercise Suite

This directory contains hands-on exercises for learning network traffic analysis and profiling techniques using machine learning.

## 📚 Exercises Overview

### Exercise 9.1b: Observable Features in Network Traffic
**File:** `exercise_9.1b/exercise_9.1b_observable_features.ipynb`

**Learning Objectives:**
- Extract observable features from network flows
- Understand flow-based vs packet-based analysis
- Implement basic traffic profiling

**Key Concepts:** Flow statistics, packet analysis, feature extraction, temporal patterns

**Dependencies:** Core libraries + optional Scapy for live packet capture

---

### Exercise 9.2a: TLS Fingerprinting
**File:** `exercise_9.2a/exercise_9.2a_tls_fingerprinting.ipynb`

**Learning Objectives:**
- Understand TLS/SSL fingerprinting techniques
- Implement JA3/JA4 fingerprint generation
- Classify client applications from TLS handshakes

**Key Concepts:** TLS handshake analysis, JA3/JA4 hashing, cipher suite profiling, client identification

**Dependencies:** Core libraries + scikit-learn

---

### Exercise 9.3a: Application Identification
**File:** `exercise_9.3a/exercise_9.3a_application_identification.ipynb`

**Learning Objectives:**
- Build ML classifiers for application identification
- Compare traditional ML vs deep learning approaches
- Deploy models via REST API

**Key Concepts:** Flow classification, Random Forest, LSTM/CNN (optional), model deployment, Flask API

**Dependencies:** Core libraries + scikit-learn + Flask (optional: TensorFlow)

**Additional Files:**
- `flask_api.py` - Example REST API for model deployment

---

### Exercise 9.3b: Malware Traffic Detection
**File:** `exercise_9.3b/exercise_9.3b_malware_traffic_detection.ipynb`

**Learning Objectives:**
- Detect malicious network traffic patterns
- Handle severely imbalanced datasets
- Implement ensemble detection systems

**Key Concepts:** Malware C&C detection, class imbalance (SMOTE), anomaly detection, XGBoost, ensemble methods

**Dependencies:** Core libraries + scikit-learn + XGBoost + imbalanced-learn

---

### Exercise 9.5a: Mercury Feature Extraction
**File:** `exercise_9.5a/exercise_9.5a_mercury_feature_extraction.ipynb`

**Learning Objectives:**
- Extract features using Mercury framework
- Perform encrypted traffic analysis
- Optimize feature extraction pipelines

**Key Concepts:** Mercury fingerprinting, encrypted traffic analysis, parallel processing, feature engineering

**Dependencies:** Core libraries + multiprocessing (built-in)

---

## 🚀 Getting Started

### 1. Install Dependencies

**Quick Install (Recommended):**
```bash
pip install -r requirements-minimal.txt
```

**Detailed Installation:**
See [INSTALLATION.md](INSTALLATION.md) for:
- Virtual environment setup
- Optional packages (TensorFlow, Scapy)
- Platform-specific instructions
- Troubleshooting guide

### 2. Launch Jupyter

```bash
jupyter notebook
```

Navigate to the exercise folder and open the `.ipynb` file.

### 3. Run Exercises

Each notebook includes:
- ✅ Learning objectives
- 📊 Simulated/real datasets
- 🔬 Step-by-step implementations
- 📈 Visualizations and analysis
- 🎯 Practice exercises
- 💡 Key takeaways

## 📦 File Structure

```
Exercises/
├── requirements.txt              # Detailed requirements with comments
├── requirements-minimal.txt      # Core dependencies only
├── INSTALLATION.md              # Comprehensive installation guide
├── README.md                    # This file
│
├── exercise_9.1b/
│   └── exercise_9.1b_observable_features.ipynb
│
├── exercise_9.2a/
│   └── exercise_9.2a_tls_fingerprinting.ipynb
│
├── exercise_9.3a/
│   ├── exercise_9.3a_application_identification.ipynb
│   └── flask_api.py            # Model deployment example
│
├── exercise_9.3b/
│   └── exercise_9.3b_malware_traffic_detection.ipynb
│
└── exercise_9.5a/
    └── exercise_9.5a_mercury_feature_extraction.ipynb
```

## 🎓 Learning Path

**Recommended Order:**

1. **Start:** Exercise 9.1b (Observable Features)
   - Understand basic flow features
   - Learn feature extraction fundamentals

2. **Next:** Exercise 9.2a (TLS Fingerprinting)
   - Apply fingerprinting techniques
   - Practice with protocol-specific features

3. **Then:** Exercise 9.3a (Application Identification)
   - Build classification models
   - Compare ML approaches
   - Learn deployment basics

4. **Advanced:** Exercise 9.3b (Malware Detection)
   - Handle imbalanced data
   - Build ensemble detectors
   - Focus on security-specific metrics

5. **Expert:** Exercise 9.5a (Mercury Features)
   - Work with encrypted traffic
   - Optimize for production
   - Handle large-scale processing

## 🔧 Technical Requirements

### Minimum Requirements
- Python 3.9, 3.10, or 3.11
- 4GB RAM
- Jupyter Notebook environment
- Core Python libraries (numpy, pandas, scikit-learn)

### Recommended Setup
- Python 3.11
- 8GB+ RAM
- Virtual environment (venv or conda)
- GPU for deep learning exercises (optional)

### Optional Enhancements
- **TensorFlow:** Enable deep learning models (Exercise 9.3a)
- **Scapy:** Live packet capture (Exercise 9.1b)
- **GPU:** Faster training for large datasets

## 📊 Datasets Used

All exercises use **simulated or built-in datasets** for easy setup:
- No external downloads required
- Realistic traffic patterns
- Properly labeled for supervised learning
- Balanced and imbalanced variants included

Advanced users can substitute real datasets:
- CICIDS2017 (network intrusion)
- CTU-13 (malware traffic)
- See course data repository for details

## 🛠️ Common Operations

### Test Installation
```python
import numpy as np
import pandas as pd
import sklearn
import xgboost
from imblearn.over_sampling import SMOTE

print("✅ All packages installed successfully!")
```

### Run Single Exercise
```bash
jupyter notebook exercise_9.2a/exercise_9.2a_tls_fingerprinting.ipynb
```

### Export Results
Each notebook generates:
- Confusion matrices
- Performance metrics
- Feature importance plots
- Classification reports

Use "File > Download as" to export results.

## 🔍 Key Concepts Covered

### Network Analysis
- Flow-based traffic analysis
- Packet-level feature extraction
- Protocol fingerprinting (TLS/SSL)
- Encrypted traffic classification

### Machine Learning
- Supervised classification
- Ensemble methods (Random Forest, XGBoost)
- Deep learning (LSTM, CNN)
- Class imbalance handling (SMOTE)
- Anomaly detection (Isolation Forest)

### Security Operations
- Application identification
- Malware C&C detection
- False positive optimization
- Model deployment strategies
- Real-time inference considerations

## ⚠️ Important Notes

### Security Best Practices
- Exercises use simulated malware traffic (safe to run)
- Never analyze live malware samples without proper isolation
- Be cautious with network packet capture (privacy concerns)

### Data Privacy
- Simulated datasets contain no real user data
- When using real datasets, follow privacy regulations
- Anonymize sensitive information before analysis

### Performance Considerations
- Some exercises are CPU-intensive (expect 5-15 min runtime)
- Use parallel processing where available (Exercise 9.5a)
- Consider Google Colab for resource-constrained systems

## 📖 Additional Resources

### Course Materials
- **Lecture Notes:** `../Lecture09.md`
- **Slides:** `../Slides09.md`
- **Theory:** `../../modules/Module_09/`

### External References
- MITRE ATT&CK: Network traffic analysis techniques
- NIST Cybersecurity Framework: Detection and response
- Zeek (Bro) IDS: Real-world traffic analysis

### Tools & Frameworks
- **Zeek:** Network security monitor
- **Suricata:** IDS/IPS engine
- **Wireshark:** Packet analysis
- **Mercury:** TLS fingerprinting library

## 🐛 Troubleshooting

### Common Issues
1. **Import errors:** Check `INSTALLATION.md` for package installation
2. **Memory errors:** Reduce dataset size or use sampling
3. **Slow execution:** Enable parallel processing or use smaller feature sets
4. **Scapy errors:** Switch to simulated data mode (no Scapy required)

### Getting Help
- Check notebook comments and markdown cells
- Review `INSTALLATION.md` for environment issues
- Consult exercise-specific troubleshooting sections
- Refer to module lecture materials

## 🎯 Learning Outcomes

By completing these exercises, you will be able to:

✅ Extract meaningful features from network traffic  
✅ Build ML-based traffic classification systems  
✅ Handle severely imbalanced security datasets  
✅ Implement TLS/SSL fingerprinting techniques  
✅ Deploy ML models for real-time traffic analysis  
✅ Evaluate models using security-relevant metrics  
✅ Understand encrypted traffic analysis challenges  
✅ Apply ensemble methods for robust detection  

## 📝 Assessment & Deliverables

Each exercise includes:
- **Guided Implementation:** Step-by-step code and explanations
- **Practice Problems:** Apply concepts to new scenarios
- **Discussion Questions:** Analyze results and trade-offs
- **Key Takeaways:** Summary of main concepts

Typical deliverables:
- Completed Jupyter notebooks
- Performance analysis reports
- Model comparison tables
- Deployment strategy recommendations

---

**Module:** 09 - Network Traffic Profiling  
**Course:** AI/ML Techniques in Cyber Security  
**Last Updated:** February 2026

For questions or issues, refer to course materials or consult with instructors.
