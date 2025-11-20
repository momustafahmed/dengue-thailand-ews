# Dengue Early Warning System - Thailand

> ⚠️ **Prototype Notice**: This dashboard is a design + analytics prototype powered entirely by _simulated data_. It demonstrates the user experience, analytical flows, and visual language for a future operational system, but it is **not connected to live surveillance feeds** yet.

A modern, interactive dashboard concept for province-level dengue surveillance and forecasting in Thailand. Built with Streamlit and featuring cross-validated prediction models on synthetic datasets so stakeholders can test-drive the experience safely.

![Dashboard Preview](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎯 Overview

This prototype showcases how a system could provide **retrospective assessment and cross-validated prediction** of dengue transmission in Thailand using simulated signals meant to resemble:
- **Climate data** (temperature, humidity, rainfall)
- **Routine surveillance** data from Thailand Ministry of Public Health
- **Machine learning** (XGBoost) for forecasting

## ✨ Features

### 📊 Interactive Dashboard
- **Province-level forecasting** for 5 major provinces (synthetic baseline)
- **4-week ahead predictions** with uncertainty intervals
- **Prototype risk assessment** messages for scenario planning
- **Climate-dengue correlation** analysis using mock climate inputs

### 🎨 Modern Design
- **Minimal, Notion-inspired UI** with clean typography
- **Responsive visualizations** using Plotly
- **Interactive controls** for dynamic analysis
- **Professional charts** and metrics

### 📈 Analysis Capabilities
- **Forecast & Trends**: Weekly predictions with confidence intervals
- **Climate Drivers**: Meteorological analysis and cross-correlations
- **Model Performance**: Validation metrics (MAE, RMSE, R², CRPS) on hold-out synthetic folds
- **Comparative Analysis**: Multi-province comparisons and heatmaps derived from simulated outbreaks

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

All values in this prototype are **generated programmatically** to reflect realistic seasonality, outbreak spikes, and climate covariates. Agencies listed below are the intended upstream providers once the system is wired to real feeds:

- **Surveillance**: Thailand Ministry of Public Health - Department of Disease Control (MoPH DDC) *(placeholder)*
- **Climate**: Thai Meteorological Department (TMD) / Google Earth Engine (GEE) *(placeholder)*
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

This is a **prototype / demonstration dashboard** that only uses synthetic data for visualization purposes. For operational deployment, integrate with real-time surveillance and climate data sources and validate against official case counts.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

## 🙏 Acknowledgments

This prototype leans on the outstanding public-domain work of the regional health and climate community. The following organizations provided reference methodologies, open documentation, or design inspiration, even though this build uses synthetic data only:

- **Thailand Ministry of Public Health (DDC)** – national surveillance guidelines and outbreak reports
- **Thai Meteorological Department / GISTDA** – climate-monitoring references that shaped the driver cards
- **World Health Organization (WHO)** – dengue control frameworks and early-warning best practices

---

**Built with ❤️ using Streamlit** | **Prototype v2.3.0 (synthetic data only)**
