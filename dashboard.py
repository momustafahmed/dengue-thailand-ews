import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from plotly.subplots import make_subplots

# ============================================================================
# PAGE CONFIG & STYLING
# ============================================================================

st.set_page_config(
    page_title="Dengue Early Warning System – Thailand",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advanced Notion-inspired CSS with modern enhancements
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main background with subtle texture */
    .main {
        background-color: #ffffff;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Sidebar with modern clean design */
    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e8e8e8;
        box-shadow: none;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 3rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
    
    [data-testid="stSidebar"] h3 {
        font-size: 0.75rem;
        font-weight: 700;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
        margin-top: 2rem;
    }
    
    [data-testid="stSidebar"] .stMarkdown p {
        font-size: 0.875rem;
        color: #4a4a4a;
        line-height: 1.5;
    }
    
    [data-testid="stSidebar"] hr {
        border: none;
        border-top: 1px solid #e8e8e8;
        margin: 1.5rem 0;
        opacity: 1;
    }
    
    /* Clean selectbox styling */
    [data-testid="stSidebar"] .stSelectbox > label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: #fafafa;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        font-size: 0.95rem;
        transition: all 0.2s ease;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div:hover {
        background: #f5f5f5;
        border-color: #d0d0d0;
    }
    
    /* Clean slider styling */
    [data-testid="stSidebar"] .stSlider > label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
    }
    
    [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] {
        padding-top: 0.5rem;
    }
    
    /* Clean checkbox styling */
    [data-testid="stSidebar"] .stCheckbox {
        padding: 0.5rem 0;
    }
    
    [data-testid="stSidebar"] .stCheckbox > label {
        font-size: 0.875rem;
        font-weight: 500;
        color: #2a2a2a;
    }
    
    /* Clean metric in sidebar */
    [data-testid="stSidebar"] [data-testid="stMetric"] {
        background: #fafafa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e8e8e8;
        box-shadow: none;
    }
    
    [data-testid="stSidebar"] [data-testid="stMetric"]:hover {
        background: #f5f5f5;
        transform: none;
    }
    
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a1a;
    }
    
    /* Clean button styling in sidebar */
    [data-testid="stSidebar"] .stButton > button {
        background: #1a1a1a;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.875rem;
        padding: 0.625rem 1rem;
        transition: all 0.2s ease;
        box-shadow: none;
        width: 100%;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: #2a2a2a;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    
    /* Clean caption styling */
    [data-testid="stSidebar"] .stCaption {
        font-size: 0.75rem;
        color: #8b8b8b;
        line-height: 1.4;
        margin-top: 0.25rem;
    }
    
    /* Badge styling in sidebar */
    [data-testid="stSidebar"] .badge {
        background: #1a1a1a;
        color: #ffffff;
        padding: 0.25rem 0.65rem;
        border-radius: 6px;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }
    
    /* Headers with better hierarchy */
    h1 {
        color: #0a0a0a;
        font-weight: 700;
        font-size: 2.5rem;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    
    h2 {
        color: #1a1a1a;
        font-weight: 600;
        font-size: 1.5rem;
        letter-spacing: -0.02em;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #2a2a2a;
        font-weight: 600;
        font-size: 1.125rem;
        letter-spacing: -0.01em;
        margin-bottom: 0.75rem;
    }
    
    /* Enhanced metrics with hover effect */
    [data-testid="stMetricValue"] {
        color: #0a0a0a;
        font-weight: 700;
        font-size: 2rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stMetric"] {
        background: #ffffff;
        padding: 1.25rem;
        border-radius: 8px;
        border: 1px solid #e8e8e8;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    
    [data-testid="stMetric"]:hover {
        border-color: #d0d0d0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        transform: translateY(-2px);
    }
    
    [data-testid="stMetricLabel"] {
        color: #6b6b6b;
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    [data-testid="stMetricDelta"] {
        font-weight: 600;
    }
    
    /* Modern buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
        color: #0a0a0a;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        font-weight: 500;
        font-size: 0.9rem;
        padding: 0.5rem 1.25rem;
        transition: all 0.25s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #fafafa 0%, #f0f0f0 100%);
        border-color: #c0c0c0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-1px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    
    /* Enhanced dividers */
    hr {
        border: none;
        border-top: 1px solid #e8e8e8;
        margin: 2.5rem 0;
        opacity: 0.6;
    }
    
    /* Modern cards with subtle shadow */
    .card {
        background: #ffffff;
        border: 1px solid #e8e8e8;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    
    .card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    
    /* Alert boxes */
    .alert {
        padding: 1rem 1.25rem;
        border-radius: 6px;
        margin: 1rem 0;
        border-left: 3px solid;
        font-size: 0.925rem;
        line-height: 1.6;
    }
    
    .alert-warning {
        background-color: #fffbf0;
        border-color: #ffa500;
        color: #8b6914;
    }
    
    .alert-info {
        background-color: #f0f8ff;
        border-color: #4a90e2;
        color: #2c5282;
    }
    
    .alert-success {
        background-color: #f0fdf4;
        border-color: #22c55e;
        color: #166534;
    }
    
    /* Enhanced text */
    p, .stMarkdown {
        color: #404040;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    /* Improved selectbox and inputs */
    .stSelectbox > div > div,
    .stSlider > div > div {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        transition: all 0.2s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #c0c0c0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    
    /* Tabs styling - Modern design */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 6px;
        border-bottom: none;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        color: #6b6b6b;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(26, 26, 26, 0.04);
        color: #2a2a2a;
        transform: scale(1.02);
    }
    
    .stTabs [aria-selected="true"] {
        background: #ffffff !important;
        color: #0a0a0a !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08), 
                    0 1px 2px rgba(0,0,0,0.06),
                    inset 0 -2px 0 0 #0a0a0a !important;
        transform: scale(1.02);
        font-weight: 600;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border: 1px solid #e8e8e8;
        border-radius: 6px;
        overflow: hidden;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f5f5f5;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c0c0c0;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a0a0a0;
    }
    
    /* Animated gradient background for header */
    .header-gradient {
        background: linear-gradient(135deg, #fafafa 0%, #ffffff 50%, #fafafa 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #e8e8e8;
    }
    
    /* Badge styles */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 0.25rem;
    }
    
    .badge-gray {
        background-color: #f0f0f0;
        color: #404040;
    }
    
    .badge-dark {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Loading animation */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .loading {
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    /* Stat card */
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
        border: 1px solid #e8e8e8;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        transform: translateY(-3px);
        border-color: #d0d0d0;
    }
    
    .stat-value {
        font-size: 2.25rem;
        font-weight: 700;
        color: #0a0a0a;
        margin: 0.5rem 0;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 0;
    }
    
    .stat-change {
        font-size: 0.875rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    .stat-change.positive {
        color: #22c55e;
    }
    
    .stat-change.negative {
        color: #ef4444;
    }
    
    /* Progress bar */
    .progress-bar {
        width: 100%;
        height: 8px;
        background-color: #f0f0f0;
        border-radius: 4px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #1a1a1a 0%, #404040 100%);
        border-radius: 4px;
        transition: width 1s ease;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SYNTHETIC DATA GENERATION
# ============================================================================

@st.cache_data
def generate_sample_data():
    """Generate synthetic dengue surveillance data for demonstration"""
    
    # Date range: 2022-2024 weekly data
    start_date = pd.date_range(start='2022-01-03', end='2024-11-11', freq='W-MON')
    n_weeks = len(start_date)
    
    # Provinces with realistic characteristics
    provinces_info = {
        'Bangkok': {'baseline': 80, 'amplitude': 60, 'trend': 25},
        'Chiang Mai': {'baseline': 45, 'amplitude': 35, 'trend': 15},
        'Phuket': {'baseline': 30, 'amplitude': 25, 'trend': 10},
        'Khon Kaen': {'baseline': 55, 'amplitude': 40, 'trend': 18},
        'Songkhla': {'baseline': 40, 'amplitude': 30, 'trend': 12}
    }
    
    data_list = []
    
    for province, params in provinces_info.items():
        # Seasonal pattern with noise
        weeks_of_year = np.arange(n_weeks) % 52
        seasonal = params['baseline'] + params['amplitude'] * np.sin(2 * np.pi * weeks_of_year / 52 - np.pi/2)
        
        # Add trend and realistic noise
        trend = np.linspace(0, params['trend'], n_weeks)
        noise = np.random.normal(0, params['baseline'] * 0.2, n_weeks)
        
        # Occasional outbreak spikes
        outbreak_weeks = np.random.choice(n_weeks, size=5, replace=False)
        outbreak_factor = np.ones(n_weeks)
        for week in outbreak_weeks:
            outbreak_factor[max(0, week-2):min(n_weeks, week+3)] *= np.random.uniform(1.5, 2.5)
        
        cases = np.maximum(0, (seasonal + trend + noise) * outbreak_factor).astype(int)
        
        # Weather data with realistic patterns
        temp_mean = 27 + 3 * np.sin(2 * np.pi * weeks_of_year / 52) + np.random.normal(0, 1.5, n_weeks)
        humidity = 70 + 10 * np.sin(2 * np.pi * weeks_of_year / 52 + np.pi/4) + np.random.normal(0, 5, n_weeks)
        rainfall = np.maximum(0, 50 + 80 * np.sin(2 * np.pi * weeks_of_year / 52) + np.random.normal(0, 30, n_weeks))
        
        # Control diseases
        chikungunya = np.maximum(0, (seasonal * 0.15 + np.random.normal(0, 5, n_weeks))).astype(int)
        hfmd = np.maximum(0, 30 + 20 * np.sin(2 * np.pi * weeks_of_year / 52 + np.pi/3) + np.random.normal(0, 8, n_weeks)).astype(int)
        
        for i, date in enumerate(start_date):
            data_list.append({
                'province': province,
                'epi_week': date,
                'year': date.year,
                'week_num': date.isocalendar()[1],
                'cases': cases[i],
                'temp_mean': round(temp_mean[i], 1),
                'humidity': round(humidity[i], 1),
                'rainfall': round(rainfall[i], 1),
                'chikungunya': chikungunya[i],
                'hfmd': hfmd[i]
            })
    
    return pd.DataFrame(data_list)

@st.cache_data
def generate_forecast_data(historical_df, province, weeks_ahead=4):
    """Generate sample forecast data with improved realism"""
    
    province_data = historical_df[historical_df['province'] == province].copy()
    last_date = province_data['epi_week'].max()
    last_cases = province_data[province_data['epi_week'] == last_date]['cases'].values[0]
    
    # Get recent trend
    recent_cases = province_data.tail(8)['cases'].values
    trend_slope = np.polyfit(range(len(recent_cases)), recent_cases, 1)[0]
    
    forecast_dates = pd.date_range(start=last_date + timedelta(weeks=1), periods=weeks_ahead, freq='W-MON')
    
    forecasts = []
    for i, date in enumerate(forecast_dates):
        # Combine recent value with trend
        base_pred = last_cases + trend_slope * (i + 1)
        seasonal_adjust = 1 + 0.1 * np.sin(2 * np.pi * (i + 1) / 52)
        mean_pred = base_pred * seasonal_adjust + np.random.normal(0, 3)
        mean_pred = max(0, mean_pred)
        
        # Uncertainty increases with forecast horizon
        uncertainty = 15 + i * 5
        
        forecasts.append({
            'epi_week': date,
            'predicted_mean': round(mean_pred, 1),
            'predicted_lower': round(max(0, mean_pred - uncertainty), 1),
            'predicted_upper': round(mean_pred + uncertainty, 1),
            'crps': round(8.5 + i * 1.2, 2)
        })
    
    return pd.DataFrame(forecasts)

@st.cache_data
def calculate_performance_metrics(province):
    """Calculate model performance metrics"""
    metrics = {
        'Bangkok': {'MAE': 12.4, 'RMSE': 18.7, 'R2': 0.78, 'MedAE': 9.2, 'MAPE': 15.3, 'Correlation': 0.89},
        'Chiang Mai': {'MAE': 8.9, 'RMSE': 13.2, 'R2': 0.82, 'MedAE': 6.8, 'MAPE': 12.7, 'Correlation': 0.91},
        'Phuket': {'MAE': 6.5, 'RMSE': 9.8, 'R2': 0.76, 'MedAE': 5.1, 'MAPE': 14.8, 'Correlation': 0.87},
        'Khon Kaen': {'MAE': 10.2, 'RMSE': 15.4, 'R2': 0.80, 'MedAE': 7.9, 'MAPE': 13.9, 'Correlation': 0.90},
        'Songkhla': {'MAE': 7.8, 'RMSE': 11.6, 'R2': 0.79, 'MedAE': 6.2, 'MAPE': 13.2, 'Correlation': 0.88}
    }
    return metrics.get(province, metrics['Bangkok'])

def create_risk_alert(current_cases, forecast_mean, historical_avg):
    """Generate risk alert based on case counts"""
    if current_cases > historical_avg * 1.5 or forecast_mean > historical_avg * 1.5:
        return "warning", "⚠️ Elevated Risk", "Cases above seasonal average"
    elif forecast_mean > current_cases * 1.2:
        return "info", "📈 Increasing Trend", "Forecasted rise in cases"
    else:
        return "success", "✓ Stable", "Cases within expected range"

# ============================================================================
# MAIN DASHBOARD
# ============================================================================

def main():
    
    # Load data
    df = generate_sample_data()
    
    # ========================================================================
    # SIDEBAR
    # ========================================================================
    
    with st.sidebar:
        # Header
        st.markdown("## 🦟 Dengue EWS")
        st.caption("Thailand Province-Level Forecasting")
        st.markdown("---")
        
        # Province selector
        province_icons = {
            'Bangkok': '🏙️', 'Chiang Mai': '🏔️', 'Phuket': '🏖️',
            'Khon Kaen': '🌾', 'Songkhla': '🌊'
        }
        
        st.markdown("### Location")
        province = st.selectbox(
            "Province",
            options=sorted(df['province'].unique()),
            format_func=lambda x: f"{province_icons.get(x, '📍')} {x}",
            label_visibility="collapsed"
        )
        
        # Time range
        st.markdown("### Time Range")
        years = sorted(df['year'].unique())
        year_range = st.select_slider(
            "Year Range",
            options=years,
            value=(2023, 2024),
            label_visibility="collapsed"
        )
        
        # Forecast settings
        st.markdown("### Forecast")
        
        horizon = st.slider(
            "Weeks ahead",
            min_value=2,
            max_value=8,
            value=4,
            step=1
        )
        
        show_uncertainty = st.checkbox("Prediction intervals", value=True)
        
        # Model info
        st.markdown("---")
        st.markdown("### Model")
        st.markdown('<span class="badge">XGBoost v2.3</span>', unsafe_allow_html=True)
        st.caption(f"Active for {province}")
        st.caption(f"Updated {datetime.now().strftime('%b %d, %Y')}")
        
        # Actions
        st.markdown("---")
        
        if st.button("� Refresh Data"):
            st.cache_data.clear()
            st.rerun()
        
        st.button("📥 Export CSV")
        
        # Footer
        st.markdown("---")
        st.caption("**Data Sources**")
        st.caption("MoPH DDC · TMD · GEE")
        st.caption(f"v2.3.0")
    
    # ========================================================================
    # MAIN CONTENT
    # ========================================================================
    
    # Header with gradient background
    st.markdown(f"""
    <div class="header-gradient">
        <h1>{province_icons.get(province, '📍')} {province}</h1>
        <p style="font-size: 1.1rem; margin: 0.5rem 0 0 0; color: #6b6b6b;">
            <strong>Dengue Early Warning & Forecasting System</strong>
        </p>
        <p style="margin: 0.25rem 0 0 0; color: #9b9b9b; font-size: 0.9rem;">
            Retrospective assessment and cross-validated prediction
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter data
    province_df = df[
        (df['province'] == province) & 
        (df['year'] >= year_range[0]) & 
        (df['year'] <= year_range[1])
    ].copy()
    
    # Generate forecast
    forecast_df = generate_forecast_data(df, province, weeks_ahead=horizon)
    
    # Calculate risk alert
    historical_avg = province_df['cases'].mean()
    current_cases = province_df.iloc[-1]['cases']
    forecast_mean = forecast_df.iloc[0]['predicted_mean']
    alert_type, alert_title, alert_message = create_risk_alert(current_cases, forecast_mean, historical_avg)
    
    # Show alert
    st.markdown(f"""
    <div class="alert alert-{alert_type}">
        <strong>{alert_title}</strong> — {alert_message}
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # KPI METRICS ROW with Enhanced Design
    # ========================================================================
    
    st.markdown("")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Current week cases
    current_cases = province_df.iloc[-1]['cases']
    prev_cases = province_df.iloc[-2]['cases']
    delta_cases = current_cases - prev_cases
    delta_pct = (delta_cases / prev_cases * 100) if prev_cases > 0 else 0
    
    with col1:
        st.metric(
            label="📊 Current Week",
            value=f"{current_cases:,}",
            delta=f"{delta_cases:+.0f} ({delta_pct:+.1f}%)",
            delta_color="inverse"
        )
    
    # 4-week average
    avg_4week = province_df.tail(4)['cases'].mean()
    avg_prev_4week = province_df.iloc[-8:-4]['cases'].mean()
    delta_avg = avg_4week - avg_prev_4week
    
    with col2:
        st.metric(
            label="📈 4-Week Avg",
            value=f"{avg_4week:.0f}",
            delta=f"{delta_avg:+.1f}",
            delta_color="inverse"
        )
    
    # Next week prediction
    next_week_pred = forecast_df.iloc[0]['predicted_mean']
    pred_change = next_week_pred - current_cases
    pred_change_pct = (pred_change / current_cases * 100) if current_cases > 0 else 0
    
    with col3:
        st.metric(
            label="🔮 Next Week",
            value=f"{next_week_pred:.0f}",
            delta=f"{pred_change:+.0f} ({pred_change_pct:+.1f}%)",
            delta_color="inverse"
        )
    
    # Peak this year
    peak_2024 = province_df[province_df['year'] == year_range[1]]['cases'].max()
    peak_week = province_df[province_df['year'] == year_range[1]]['cases'].idxmax()
    
    with col4:
        st.metric(
            label=f"⚡ {year_range[1]} Peak",
            value=f"{peak_2024:,}",
            delta=f"Week {province_df.loc[peak_week, 'week_num']}" if peak_week in province_df.index else None,
            delta_color="off"
        )
    
    # Year-to-date total
    ytd_total = province_df[province_df['year'] == year_range[1]]['cases'].sum()
    ytd_prev = province_df[province_df['year'] == year_range[1]-1]['cases'].sum() if year_range[1] > year_range[0] else ytd_total
    ytd_change = ((ytd_total - ytd_prev) / ytd_prev * 100) if ytd_prev > 0 else 0
    
    with col5:
        st.metric(
            label=f"📅 {year_range[1]} Total",
            value=f"{ytd_total:,}",
            delta=f"{ytd_change:+.1f}% vs {year_range[1]-1}",
            delta_color="inverse"
        )
    
    st.markdown("---")
    
    # ========================================================================
    # TABS FOR ORGANIZED CONTENT
    # ========================================================================
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Forecast & Trends",
        "🌡️ Climate Drivers", 
        "🎯 Model Performance",
        "📊 Comparative Analysis"
    ])
    
    # ========================================================================
    # TAB 1: FORECAST VISUALIZATION
    # ========================================================================
    
    with tab1:
        st.markdown("### Weekly Dengue Cases & Forecast")
        st.caption("Historical observations with model predictions and uncertainty intervals")
        
        # Prepare plot data
        historical_plot = province_df.tail(52).copy()  # Last year
        
        fig = go.Figure()
        
        # Historical cases
        fig.add_trace(go.Scatter(
            x=historical_plot['epi_week'],
            y=historical_plot['cases'],
            mode='lines+markers',
            name='Observed Cases',
            line=dict(color='#0a0a0a', width=2.5),
            marker=dict(size=6, color='#0a0a0a', symbol='circle'),
            hovertemplate='<b>Week:</b> %{x|%Y-%m-%d}<br><b>Cases:</b> %{y}<extra></extra>'
        ))
        
        # Forecast mean
        fig.add_trace(go.Scatter(
            x=forecast_df['epi_week'],
            y=forecast_df['predicted_mean'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#4a90e2', width=2.5, dash='dash'),
            marker=dict(size=6, color='#4a90e2', symbol='diamond'),
            hovertemplate='<b>Week:</b> %{x|%Y-%m-%d}<br><b>Predicted:</b> %{y:.1f}<extra></extra>'
        ))
        
        # Uncertainty band
        if show_uncertainty:
            fig.add_trace(go.Scatter(
                x=forecast_df['epi_week'].tolist() + forecast_df['epi_week'].tolist()[::-1],
                y=forecast_df['predicted_upper'].tolist() + forecast_df['predicted_lower'].tolist()[::-1],
                fill='toself',
                fillcolor='rgba(74, 144, 226, 0.15)',
                line=dict(color='rgba(74, 144, 226, 0.3)', width=1),
                name='95% Prediction Interval',
                showlegend=True,
                hoverinfo='skip'
            ))
        
        # Add threshold line
        threshold = historical_avg * 1.5
        fig.add_hline(
            y=threshold,
            line_dash="dot",
            line_color="rgba(255, 165, 0, 0.5)",
            annotation_text=f"Alert Threshold ({threshold:.0f})",
            annotation_position="right"
        )
        
        fig.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a', size=12),
            xaxis=dict(
                title='Epidemiological Week',
                title_font=dict(size=13, weight=600),
                gridcolor='#f0f0f0',
                showline=True,
                linecolor='#e0e0e0',
                linewidth=1
            ),
            yaxis=dict(
                title='Dengue Cases',
                title_font=dict(size=13, weight=600),
                gridcolor='#f0f0f0',
                showline=True,
                linecolor='#e0e0e0',
                linewidth=1
            ),
            hovermode='x unified',
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='left',
                x=0,
                bgcolor='rgba(255,255,255,0.95)',
                bordercolor='#e0e0e0',
                borderwidth=1,
                font=dict(size=11)
            ),
            margin=dict(l=70, r=30, t=80, b=70),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Time series decomposition view
        st.markdown("#### 📉 Trend Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            # Rolling average
            fig_rolling = go.Figure()
            
            recent_data = province_df.tail(52)
            rolling_4 = recent_data['cases'].rolling(window=4, center=True).mean()
            rolling_8 = recent_data['cases'].rolling(window=8, center=True).mean()
            
            fig_rolling.add_trace(go.Scatter(
                x=recent_data['epi_week'],
                y=recent_data['cases'],
                mode='lines',
                name='Weekly Cases',
                line=dict(color='#e0e0e0', width=1),
                opacity=0.5
            ))
            
            fig_rolling.add_trace(go.Scatter(
                x=recent_data['epi_week'],
                y=rolling_4,
                mode='lines',
                name='4-Week MA',
                line=dict(color='#6b6b6b', width=2)
            ))
            
            fig_rolling.add_trace(go.Scatter(
                x=recent_data['epi_week'],
                y=rolling_8,
                mode='lines',
                name='8-Week MA',
                line=dict(color='#0a0a0a', width=2.5)
            ))
            
            fig_rolling.update_layout(
                title='Moving Averages',
                title_font=dict(size=14),
                plot_bgcolor='#ffffff',
                paper_bgcolor='#ffffff',
                font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a'),
                xaxis=dict(gridcolor='#f5f5f5', title=''),
                yaxis=dict(gridcolor='#f5f5f5', title='Cases'),
                legend=dict(orientation='h', yanchor='top', y=-0.15, xanchor='left', x=0),
                margin=dict(l=50, r=20, t=40, b=60),
                height=300
            )
            
            st.plotly_chart(fig_rolling, use_container_width=True)
        
        with col2:
            # Week-over-week changes
            fig_change = go.Figure()
            
            recent_data = province_df.tail(26)
            changes = recent_data['cases'].diff()
            colors = ['#ef4444' if x < 0 else '#22c55e' for x in changes]
            
            fig_change.add_trace(go.Bar(
                x=recent_data['epi_week'],
                y=changes,
                marker=dict(color=colors, opacity=0.7),
                name='Week-over-Week Change',
                hovertemplate='<b>Change:</b> %{y:+.0f}<extra></extra>'
            ))
            
            fig_change.add_hline(y=0, line_color='#0a0a0a', line_width=1)
            
            fig_change.update_layout(
                title='Week-over-Week Changes',
                title_font=dict(size=14),
                plot_bgcolor='#ffffff',
                paper_bgcolor='#ffffff',
                font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a'),
                xaxis=dict(gridcolor='#f5f5f5', title=''),
                yaxis=dict(gridcolor='#f5f5f5', title='Change in Cases'),
                showlegend=False,
                margin=dict(l=50, r=20, t=40, b=60),
                height=300
            )
            
            st.plotly_chart(fig_change, use_container_width=True)
    
    # ========================================================================
    # TAB 2: CLIMATE CONTEXT
    # ========================================================================
    
    with tab2:
        st.markdown("### Climate Drivers & Environmental Context")
        st.caption("Meteorological variables at weekly resolution aligned with epidemiological data")
        
        # Combined climate visualization
        recent_climate = province_df.tail(52)
        
        fig_climate = make_subplots(
            rows=3, cols=1,
            subplot_titles=('Temperature (°C)', 'Relative Humidity (%)', 'Rainfall (mm)'),
            vertical_spacing=0.12,
            specs=[[{"secondary_y": False}],
                   [{"secondary_y": False}],
                   [{"secondary_y": False}]]
        )
        
        # Temperature
        fig_climate.add_trace(
            go.Scatter(
                x=recent_climate['epi_week'],
                y=recent_climate['temp_mean'],
                mode='lines',
                name='Temperature',
                line=dict(color='#ef4444', width=2),
                fill='tozeroy',
                fillcolor='rgba(239, 68, 68, 0.1)',
                hovertemplate='<b>Temp:</b> %{y:.1f}°C<extra></extra>'
            ),
            row=1, col=1
        )
        
        # Humidity
        fig_climate.add_trace(
            go.Scatter(
                x=recent_climate['epi_week'],
                y=recent_climate['humidity'],
                mode='lines',
                name='Humidity',
                line=dict(color='#3b82f6', width=2),
                fill='tozeroy',
                fillcolor='rgba(59, 130, 246, 0.1)',
                hovertemplate='<b>RH:</b> %{y:.1f}%<extra></extra>'
            ),
            row=2, col=1
        )
        
        # Rainfall
        fig_climate.add_trace(
            go.Bar(
                x=recent_climate['epi_week'],
                y=recent_climate['rainfall'],
                name='Rainfall',
                marker=dict(color='#06b6d4', opacity=0.7),
                hovertemplate='<b>Rain:</b> %{y:.1f}mm<extra></extra>'
            ),
            row=3, col=1
        )
        
        fig_climate.update_xaxes(gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0')
        fig_climate.update_yaxes(gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0')
        
        fig_climate.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a', size=11),
            showlegend=False,
            height=700,
            margin=dict(l=60, r=30, t=60, b=40)
        )
        
        st.plotly_chart(fig_climate, use_container_width=True)
        
        # Climate summary cards
        st.markdown("#### Current Climate Conditions")
        col1, col2, col3, col4 = st.columns(4)
        
        current_temp = province_df.iloc[-1]['temp_mean']
        avg_temp = province_df['temp_mean'].mean()
        
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">Temperature</p>
                <p class="stat-value">{current_temp:.1f}°C</p>
                <p class="stat-change {'positive' if current_temp > avg_temp else 'negative'}">
                    {current_temp - avg_temp:+.1f}°C vs avg
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        current_humidity = province_df.iloc[-1]['humidity']
        avg_humidity = province_df['humidity'].mean()
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">Humidity</p>
                <p class="stat-value">{current_humidity:.1f}%</p>
                <p class="stat-change {'positive' if current_humidity > avg_humidity else 'negative'}">
                    {current_humidity - avg_humidity:+.1f}% vs avg
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        current_rainfall = province_df.iloc[-1]['rainfall']
        avg_rainfall = province_df['rainfall'].mean()
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">Rainfall (Week)</p>
                <p class="stat-value">{current_rainfall:.0f}mm</p>
                <p class="stat-change {'positive' if current_rainfall > avg_rainfall else 'negative'}">
                    {current_rainfall - avg_rainfall:+.0f}mm vs avg
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        monthly_rainfall = province_df.tail(4)['rainfall'].sum()
        
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">4-Week Rainfall</p>
                <p class="stat-value">{monthly_rainfall:.0f}mm</p>
                <p class="stat-change" style="color: #6b6b6b;">
                    Cumulative
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Cross-correlation analysis
        st.markdown("#### 🔬 Climate-Dengue Correlation")
        
        # Calculate correlations at different lags
        lags = range(0, 9)
        temp_corr = [province_df['cases'].corr(province_df['temp_mean'].shift(lag)) for lag in lags]
        humid_corr = [province_df['cases'].corr(province_df['humidity'].shift(lag)) for lag in lags]
        rain_corr = [province_df['cases'].corr(province_df['rainfall'].shift(lag)) for lag in lags]
        
        fig_corr = go.Figure()
        
        fig_corr.add_trace(go.Scatter(
            x=list(lags),
            y=temp_corr,
            mode='lines+markers',
            name='Temperature',
            line=dict(color='#ef4444', width=2.5),
            marker=dict(size=8)
        ))
        
        fig_corr.add_trace(go.Scatter(
            x=list(lags),
            y=humid_corr,
            mode='lines+markers',
            name='Humidity',
            line=dict(color='#3b82f6', width=2.5),
            marker=dict(size=8)
        ))
        
        fig_corr.add_trace(go.Scatter(
            x=list(lags),
            y=rain_corr,
            mode='lines+markers',
            name='Rainfall',
            line=dict(color='#06b6d4', width=2.5),
            marker=dict(size=8)
        ))
        
        fig_corr.add_hline(y=0, line_dash="dot", line_color="#9b9b9b", line_width=1)
        
        fig_corr.update_layout(
            title='Cross-Correlation at Different Lag Periods',
            title_font=dict(size=14),
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a'),
            xaxis=dict(
                title='Lag (weeks)',
                gridcolor='#f0f0f0',
                showline=True,
                linecolor='#e0e0e0',
                dtick=1
            ),
            yaxis=dict(
                title='Correlation Coefficient',
                gridcolor='#f0f0f0',
                showline=True,
                linecolor='#e0e0e0',
                range=[-0.5, 0.8]
            ),
            legend=dict(orientation='h', yanchor='top', y=-0.15, xanchor='left', x=0),
            height=350,
            margin=dict(l=60, r=30, t=50, b=80)
        )
        
        st.plotly_chart(fig_corr, use_container_width=True)
    
    # ========================================================================
    # TAB 3: MODEL PERFORMANCE
    # ========================================================================
    
    with tab3:
        st.markdown("### Model Validation & Performance Metrics")
        st.caption("Out-of-sample validation results and feature importance analysis")
        
        # Performance metrics
        metrics = calculate_performance_metrics(province)
        
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">MAE</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['MAE']}</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Mean Abs Error</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">RMSE</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['RMSE']}</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Root MSE</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">R²</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['R2']:.2f}</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Coef of Determ</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">MedAE</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['MedAE']}</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Median AE</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col5:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">MAPE</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['MAPE']:.1f}%</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Mean APE</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col6:
            st.markdown(f"""
            <div class="stat-card">
                <p class="stat-label">Correlation</p>
                <p class="stat-value" style="font-size: 2rem;">{metrics['Correlation']:.2f}</p>
                <p style="font-size: 0.7rem; color: #6b6b6b; margin: 0;">Pearson r</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Feature importance and forecast details
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### 🔍 Feature Importance")
            st.caption("Top drivers of recent dengue transmission")
            
            # Sample feature importance
            features = pd.DataFrame({
                'Feature': ['Cases lag-1', 'Temperature (2w lag)', 'Humidity (1w lag)', 
                           'Rainfall (4w lag)', 'Week-of-year', 'Cases rolling-mean'],
                'Importance': [0.32, 0.24, 0.18, 0.12, 0.08, 0.06]
            }).sort_values('Importance', ascending=True)
            
            fig_importance = go.Figure()
            fig_importance.add_trace(go.Bar(
                y=features['Feature'],
                x=features['Importance'],
                orientation='h',
                marker=dict(
                    color='#1a1a1a',
                    line=dict(color='#0a0a0a', width=1)
                ),
                hovertemplate='<b>%{y}</b><br>Importance: %{x:.2f}<extra></extra>'
            ))
            
            fig_importance.update_layout(
                plot_bgcolor='#ffffff',
                paper_bgcolor='#ffffff',
                font=dict(family='Inter, system-ui, sans-serif', color='#1a1a1a'),
                xaxis=dict(title='Relative Importance', gridcolor='#f0f0f0', range=[0, 0.35]),
                yaxis=dict(gridcolor='#f0f0f0'),
                margin=dict(l=180, r=20, t=20, b=50),
                height=320,
                showlegend=False
            )
            
            st.plotly_chart(fig_importance, use_container_width=True)
        
        with col2:
            st.markdown("#### 📋 Forecast Details")
            
            forecast_table = forecast_df.copy()
            forecast_table['epi_week'] = forecast_table['epi_week'].dt.strftime('%Y-%m-%d')
            forecast_table = forecast_table[['epi_week', 'predicted_mean', 'predicted_lower', 'predicted_upper']]
            forecast_table.columns = ['Week', 'Mean', 'Lower', 'Upper']
            
            st.dataframe(
                forecast_table,
                use_container_width=True,
                hide_index=True,
                height=320
            )
        
        # Model info
        st.markdown("#### ⚙️ Model Configuration")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="alert alert-info">
                <strong>Algorithm</strong><br>
                XGBoost Gradient Boosting<br>
                <span class="badge badge-dark">v2.3.0</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="alert alert-info">
                <strong>Validation</strong><br>
                Blocked forward-chaining CV<br>
                80/20 temporal split
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="alert alert-info">
                <strong>Optimization</strong><br>
                Bayesian hyperparameter tuning<br>
                CRPS minimization
            </div>
            """, unsafe_allow_html=True)
    
    # ========================================================================
    # TAB 4: COMPARATIVE ANALYSIS
    # ========================================================================
    
    with tab4:
        st.markdown("### Multi-Province Comparison")
        st.caption("Comparative epidemiological trends across Thailand provinces")
        
        # Get recent data for all provinces
        recent_year = year_range[1]
        all_provinces_data = df[df['year'] == recent_year].copy()
        
        # Time series comparison
        st.markdown(f"#### 📈 Weekly Cases Comparison ({recent_year})")
        
        fig_multi = go.Figure()
        
        colors = {
            'Bangkok': '#1a1a1a',
            'Chiang Mai': '#ef4444',
            'Phuket': '#3b82f6',
            'Khon Kaen': '#22c55e',
            'Songkhla': '#f59e0b'
        }
        
        for prov in sorted(df['province'].unique()):
            prov_data = all_provinces_data[all_provinces_data['province'] == prov]
            fig_multi.add_trace(go.Scatter(
                x=prov_data['epi_week'],
                y=prov_data['cases'],
                mode='lines',
                name=f"{province_icons.get(prov, '📍')} {prov}",
                line=dict(color=colors.get(prov, '#6b6b6b'), width=2.5),
                hovertemplate='<b>' + prov + '</b><br>%{x|%Y-%m-%d}<br>Cases: %{y}<extra></extra>'
            ))
        
        fig_multi.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a'),
            xaxis=dict(title='Week', gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0'),
            yaxis=dict(title='Dengue Cases', gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0'),
            hovermode='x unified',
            legend=dict(orientation='h', yanchor='top', y=-0.15, xanchor='left', x=0),
            height=450,
            margin=dict(l=60, r=30, t=30, b=100)
        )
        
        st.plotly_chart(fig_multi, use_container_width=True)
        
        # Summary statistics
        st.markdown(f"#### 📊 Province Summary Statistics ({recent_year})")
        
        summary_data = []
        for prov in sorted(df['province'].unique()):
            prov_year_data = df[(df['province'] == prov) & (df['year'] == recent_year)]
            summary_data.append({
                'Province': f"{province_icons.get(prov, '📍')} {prov}",
                'Total Cases': f"{prov_year_data['cases'].sum():,}",
                'Weekly Average': f"{prov_year_data['cases'].mean():.1f}",
                'Peak Week': f"{prov_year_data['cases'].max():,}",
                'Std Dev': f"{prov_year_data['cases'].std():.1f}",
                'Min': f"{prov_year_data['cases'].min():,}"
            })
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        
        # Heatmap of cases by province and month
        st.markdown(f"#### 🗓️ Temporal Pattern Heatmap ({recent_year})")
        
        # Create month-province matrix
        heatmap_data = all_provinces_data.copy()
        heatmap_data['month'] = heatmap_data['epi_week'].dt.month
        pivot_data = heatmap_data.pivot_table(
            values='cases',
            index='province',
            columns='month',
            aggfunc='sum'
        ).fillna(0)
        
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig_heatmap = go.Figure(data=go.Heatmap(
            z=pivot_data.values,
            x=[month_names[i-1] for i in pivot_data.columns],
            y=[f"{province_icons.get(p, '📍')} {p}" for p in pivot_data.index],
            colorscale='Greys',
            hovertemplate='<b>%{y}</b><br>%{x}<br>Cases: %{z:.0f}<extra></extra>',
            colorbar=dict(title="Cases")
        ))
        
        fig_heatmap.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font=dict(family='Inter, system-ui, sans-serif', color='#0a0a0a'),
            xaxis=dict(title='Month', side='bottom'),
            yaxis=dict(title='Province'),
            height=350,
            margin=dict(l=150, r=100, t=30, b=50)
        )
        
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    st.markdown("---")
    st.markdown("")
    
    st.caption("""
    **Dengue Early Warning System for Thailand** | Province-level retrospective assessment and cross-validated prediction  
    Data sources: Thailand Ministry of Public Health (DDC), Thai Meteorological Department, Google Earth Engine  
    Methods: XGBoost with lagged climate & surveillance features | Cross-validation: blocked forward-chaining  
    **Note:** This is a demonstration dashboard with synthetic data for visualization purposes only.
    """)

if __name__ == "__main__":
    main()
