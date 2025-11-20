# Dengue Early Warning System - Thailand

A modern, interactive dashboard for province-level dengue surveillance and forecasting in Thailand. Built with Streamlit and featuring cross-validated prediction models.

![Dashboard Preview](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎯 Overview

This system provides **retrospective assessment and cross-validated prediction** of dengue transmission in Thailand using:
- **Climate data** (temperature, humidity, rainfall)
- **Routine surveillance** data from Thailand Ministry of Public Health
- **Machine learning** (XGBoost) for forecasting

## ✨ Features

### 📊 Interactive Dashboard
- **Province-level forecasting** for 5 major provinces
- **4-week ahead predictions** with uncertainty intervals
- **Real-time risk assessment** and alerts
- **Climate-dengue correlation** analysis

### 🎨 Modern Design
- **Minimal, Notion-inspired UI** with clean typography
- **Responsive visualizations** using Plotly
- **Interactive controls** for dynamic analysis
- **Professional charts** and metrics

### 📈 Analysis Capabilities
- **Forecast & Trends**: Weekly predictions with confidence intervals
- **Climate Drivers**: Meteorological analysis and cross-correlations
- **Model Performance**: Validation metrics (MAE, RMSE, R², CRPS)
- **Comparative Analysis**: Multi-province comparisons and heatmaps

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/momustafahmed/dengue-thailand-ews.git
cd dengue-thailand-ews
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install streamlit pandas numpy plotly
```

### Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## 📁 Project Structure

```
dengue-thailand-ews/
├── dashboard.py          # Main Streamlit application
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── .gitignore          # Git ignore file
```

## 🛠️ Technology Stack

- **Framework**: Streamlit 1.28+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **ML Model**: XGBoost (for forecasting)
- **Language**: Python 3.9+

## 📊 Data Sources

- **Surveillance**: Thailand Ministry of Public Health - Department of Disease Control (MoPH DDC)
- **Climate**: Thai Meteorological Department (TMD) / Google Earth Engine (GEE)
- **ICD-10 Codes**: A90 (Dengue fever), A91 (Dengue hemorrhagic fever)

## 🎯 Key Metrics

### Model Performance
- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Square Error
- **R²**: Coefficient of Determination
- **CRPS**: Continuous Ranked Probability Score

### Features
- Cases lag (1-8 weeks)
- Temperature (mean, min, max, DTR)
- Relative humidity
- Rainfall (1, 2, 4-week cumulative)
- Seasonal harmonics
- Rolling statistics

## 🔬 Methodology

### Validation Strategy
- **Cross-validation**: Blocked forward-chaining
- **Test split**: 80/20 temporal split
- **Hyperparameter tuning**: Bayesian optimization
- **Objective**: CRPS minimization

### Forecasting
- **Model**: XGBoost Gradient Boosting
- **Horizon**: 2-8 weeks ahead
- **Uncertainty**: 95% prediction intervals
- **Update frequency**: Weekly

## 🌟 Features in Detail

### Province Coverage
- Bangkok
- Chiang Mai
- Phuket
- Khon Kaen
- Songkhla

### Risk Assessment
- High Risk: Cases >1.5x seasonal average
- Rising: Increasing trend detected
- Stable: Within expected range

### Syndromic Context (Control Diseases)
- HFMD and Chikungunya synthetic signals for situational awareness
- Weekly metrics alongside dengue forecasts
- Comparative overlay chart for recent 52 weeks

## 📝 Note

This is a **demonstration dashboard** using synthetic data for visualization purposes. For operational deployment, integrate with real-time surveillance and climate data sources.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

## 🙏 Acknowledgments

- Thailand Ministry of Public Health
- Thai Meteorological Department
- World Health Organization (WHO) dengue guidelines

---

**Built with ❤️ using Streamlit** | **Version 2.3.0**
