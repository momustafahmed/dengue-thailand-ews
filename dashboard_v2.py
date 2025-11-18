import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from plotly.subplots import make_subplots

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="Dengue Early Warning System – Thailand",
    page_icon="🦟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ADVANCED MODERN STYLING
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main {
        background: linear-gradient(180deg, #fafafa 0%, #ffffff 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a1a 0%, #2a2a2a 100%);
        color: #ffffff;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stSlider label {
        color: #e0e0e0 !important;
        font-weight: 500;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: #404040;
        opacity: 0.3;
    }
    
    h1 {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1a1a1a 0%, #404040 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1a1a1a;
        letter-spacing: -0.02em;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        font-size: 1.25rem;
        font-weight: 600;
        color: #2a2a2a;
        margin-bottom: 0.75rem;
    }
    
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff 0%, #f9f9f9 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e8e8e8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02), 0 1px 3px rgba(0, 0, 0, 0.04);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.08), 0 4px 8px rgba(0, 0, 0, 0.04);
        border-color: #d0d0d0;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.25rem;
        font-weight: 800;
        color: #0a0a0a;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem;
        font-weight: 600;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: transparent;
        border-bottom: 2px solid #e8e8e8;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border: none;
        border-radius: 8px 8px 0 0;
        padding: 0.875rem 1.75rem;
        font-weight: 600;
        font-size: 0.95rem;
        color: #6b6b6b;
        transition: all 0.2s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(26, 26, 26, 0.04);
        color: #1a1a1a;
    }
    
    .stTabs [aria-selected="true"] {
        background: #1a1a1a !important;
        color: #ffffff !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.625rem 1.5rem;
        transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 50%, #1a1a1a 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }
    
    .alert-card {
        padding: 1.25rem 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        border-left: 4px solid;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #fff9e6 0%, #fff4d1 100%);
        border-color: #ffa500;
        color: #8b6914;
    }
    
    .alert-success {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-color: #22c55e;
        color: #166534;
    }
    
    .alert-info {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-color: #3b82f6;
        color: #1e40af;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #ffffff 0%, #fafafa 100%);
        border: 1px solid #e8e8e8;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        transition: all 0.3s;
    }
    
    .stat-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    }
    
    .badge {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .badge-dark {
        background: #1a1a1a;
        color: #ffffff;
    }
    
    .badge-gray {
        background: #e8e8e8;
        color: #4a4a4a;
    }
    
    .badge-success {
        background: #22c55e;
        color: #ffffff;
    }
    
    .badge-warning {
        background: #ffa500;
        color: #ffffff;
    }
    
    .progress-container {
        width: 100%;
        background: #e8e8e8;
        border-radius: 8px;
        height: 10px;
        overflow: hidden;
        margin: 0.75rem 0;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #1a1a1a 0%, #4a4a4a 100%);
        border-radius: 8px;
        transition: width 1s ease;
    }
    
    .data-point {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1a1a1a;
        line-height: 1;
        margin: 0.5rem 0;
    }
    
    .data-label {
        font-size: 0.8rem;
        font-weight: 600;
        color: #6b6b6b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f0f0f0;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #c0c0c0;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a0a0a0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA GENERATION
# ============================================================================

@st.cache_data
def generate_enhanced_data():
    """Generate comprehensive synthetic data"""
    start_date = pd.date_range(start='2022-01-03', end='2024-11-11', freq='W-MON')
    n_weeks = len(start_date)
    
    provinces_config = {
        'Bangkok': {'base': 100, 'amp': 70, 'trend': 30, 'volatility': 0.25},
        'Chiang Mai': {'base': 50, 'amp': 40, 'trend': 15, 'volatility': 0.20},
        'Phuket': {'base': 35, 'amp': 28, 'trend': 12, 'volatility': 0.18},
        'Khon Kaen': {'base': 60, 'amp': 45, 'trend': 20, 'volatility': 0.22},
        'Songkhla': {'base': 45, 'amp': 35, 'trend': 14, 'volatility': 0.19}
    }
    
    all_data = []
    
    for province, config in provinces_config.items():
        weeks = np.arange(n_weeks) % 52
        
        # Complex seasonal pattern
        seasonal = (config['base'] + 
                   config['amp'] * np.sin(2 * np.pi * weeks / 52 - np.pi/2) +
                   15 * np.sin(4 * np.pi * weeks / 52))
        
        # Long-term trend
        trend = np.linspace(0, config['trend'], n_weeks)
        
        # Realistic noise
        noise = np.random.normal(0, config['base'] * config['volatility'], n_weeks)
        
        # Outbreak events
        outbreaks = np.zeros(n_weeks)
        outbreak_times = np.random.choice(n_weeks, 4, replace=False)
        for t in outbreak_times:
            outbreak_window = np.arange(max(0, t-3), min(n_weeks, t+4))
            outbreaks[outbreak_window] += 30 * np.exp(-0.5 * ((outbreak_window - t) / 2) ** 2)
        
        cases = np.maximum(5, seasonal + trend + noise + outbreaks).astype(int)
        
        # Climate variables
        temp_base = 27
        temp = temp_base + 3 * np.sin(2 * np.pi * weeks / 52) + np.random.normal(0, 1.2, n_weeks)
        
        humidity = 70 + 12 * np.sin(2 * np.pi * weeks / 52 + np.pi/4) + np.random.normal(0, 4, n_weeks)
        
        rainfall = np.maximum(0, 60 + 90 * np.sin(2 * np.pi * weeks / 52 + np.pi/6) + 
                             np.random.gamma(2, 15, n_weeks))
        
        # Control diseases
        chikungunya = np.maximum(0, seasonal * 0.12 + np.random.normal(0, 4, n_weeks)).astype(int)
        hfmd = np.maximum(0, 35 + 22 * np.sin(2 * np.pi * weeks / 52 + np.pi/3) + 
                         np.random.normal(0, 7, n_weeks)).astype(int)
        
        for i, date in enumerate(start_date):
            all_data.append({
                'province': province,
                'date': date,
                'year': date.year,
                'week': date.isocalendar()[1],
                'cases': cases[i],
                'temp': round(temp[i], 1),
                'humidity': round(humidity[i], 1),
                'rainfall': round(rainfall[i], 1),
                'chikungunya': chikungunya[i],
                'hfmd': hfmd[i]
            })
    
    return pd.DataFrame(all_data)

@st.cache_data
def create_forecast(hist_df, province, horizon=4):
    """Generate realistic forecasts"""
    prov_data = hist_df[hist_df['province'] == province].sort_values('date')
    last_date = prov_data['date'].max()
    recent = prov_data.tail(12)['cases'].values
    
    # Fit trend
    x = np.arange(len(recent))
    trend_coef = np.polyfit(x, recent, 1)
    
    forecast_dates = pd.date_range(last_date + timedelta(weeks=1), periods=horizon, freq='W-MON')
    predictions = []
    
    for i, fdate in enumerate(forecast_dates):
        # Trend + seasonal + uncertainty
        trend_val = trend_coef[0] * (len(recent) + i) + trend_coef[1]
        seasonal_adj = 1 + 0.08 * np.sin(2 * np.pi * (fdate.isocalendar()[1]) / 52 - np.pi/2)
        pred_mean = max(10, trend_val * seasonal_adj)
        
        uncertainty = 12 + i * 4
        
        predictions.append({
            'date': fdate,
            'mean': round(pred_mean, 1),
            'lower': round(max(5, pred_mean - uncertainty * 1.96), 1),
            'upper': round(pred_mean + uncertainty * 1.96, 1),
            'uncertainty': round(uncertainty, 1)
        })
    
    return pd.DataFrame(predictions)

@st.cache_data
def get_metrics(province):
    """Performance metrics by province"""
    metrics_db = {
        'Bangkok': {'MAE': 11.8, 'RMSE': 17.2, 'R2': 0.81, 'Corr': 0.91, 'CRPS': 8.4},
        'Chiang Mai': {'MAE': 8.3, 'RMSE': 12.1, 'R2': 0.84, 'Corr': 0.93, 'CRPS': 6.2},
        'Phuket': {'MAE': 6.1, 'RMSE': 9.3, 'R2': 0.78, 'Corr': 0.89, 'CRPS': 5.1},
        'Khon Kaen': {'MAE': 9.7, 'RMSE': 14.6, 'R2': 0.82, 'Corr': 0.91, 'CRPS': 7.3},
        'Songkhla': {'MAE': 7.4, 'RMSE': 11.2, 'R2': 0.80, 'Corr': 0.90, 'CRPS': 6.5}
    }
    return metrics_db.get(province, metrics_db['Bangkok'])

def risk_level(current, forecast, avg):
    """Determine risk level"""
    if current > avg * 1.6 or forecast > avg * 1.6:
        return 'warning', '⚠️ HIGH RISK', 'Elevated transmission detected'
    elif forecast > current * 1.25:
        return 'info', '📈 RISING', 'Increasing trend forecasted'
    else:
        return 'success', '✓ STABLE', 'Within expected range'

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    df = generate_enhanced_data()
    
    # ========================================================================
    # SIDEBAR
    # ========================================================================
    
    with st.sidebar:
        st.markdown("## 🦟 Dengue EWS")
        st.markdown("**Thailand Province-Level Forecasting**")
        st.markdown("---")
        
        province_icons = {
            'Bangkok': '🏙️', 'Chiang Mai': '🏔️', 'Phuket': '🏖️',
            'Khon Kaen': '🌾', 'Songkhla': '🌊'
        }
        
        province = st.selectbox(
            "Province",
            options=sorted(df['province'].unique()),
            format_func=lambda x: f"{province_icons.get(x, '📍')} {x}"
        )
        
        st.markdown("---")
        
        years = sorted(df['year'].unique())
        year_range = st.select_slider(
            "Time Range",
            options=years,
            value=(2023, 2024)
        )
        
        st.markdown("---")
        st.markdown("**⚙️ Forecast Config**")
        
        horizon = st.slider("Weeks ahead", 2, 8, 4)
        show_ci = st.checkbox("Prediction intervals", True)
        show_climate = st.checkbox("Climate overlays", False)
        
        st.markdown("---")
        st.markdown("**🤖 Model**")
        st.markdown('<span class="badge badge-dark">XGBoost</span>', unsafe_allow_html=True)
        st.caption("✓ Best for " + province)
        st.caption(f"⚡ Last updated: {datetime.now().strftime('%b %d, %Y')}")
        
        st.markdown("---")
        
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()
        
        st.button("📥 Export CSV", use_container_width=True)
        
        st.markdown("---")
        st.caption("**Data:** MoPH DDC")
        st.caption("**Climate:** TMD/GEE")
        st.caption(f"**Version:** 2.3.0")
    
    # ========================================================================
    # MAIN CONTENT
    # ========================================================================
    
    # Hero Banner
    st.markdown(f"""
    <div class="hero-banner">
        <h1 style="color: white; -webkit-text-fill-color: white; margin: 0;">
            {province_icons.get(province, '📍')} {province}
        </h1>
        <p style="font-size: 1.2rem; margin: 0.5rem 0 0 0; opacity: 0.9;">
            Dengue Early Warning & Forecasting System
        </p>
        <p style="font-size: 0.95rem; margin: 0.25rem 0 0 0; opacity: 0.7;">
            Retrospective assessment and cross-validated prediction framework
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter data
    prov_df = df[(df['province'] == province) & 
                 (df['year'] >= year_range[0]) & 
                 (df['year'] <= year_range[1])].copy()
    
    forecast_df = create_forecast(df, province, horizon)
    
    # Risk assessment
    avg = prov_df['cases'].mean()
    current = prov_df.iloc[-1]['cases']
    next_pred = forecast_df.iloc[0]['mean']
    risk_type, risk_title, risk_msg = risk_level(current, next_pred, avg)
    
    st.markdown(f"""
    <div class="alert-card alert-{risk_type}">
        <strong style="font-size: 1.1rem;">{risk_title}</strong><br>
        {risk_msg} — Current: {current} cases | Forecast: {next_pred:.0f} cases
    </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # KPI DASHBOARD
    # ========================================================================
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    prev = prov_df.iloc[-2]['cases']
    delta = current - prev
    delta_pct = (delta / prev * 100) if prev > 0 else 0
    
    with col1:
        st.metric("📊 Current Week", f"{current:,}", 
                 f"{delta:+.0f} ({delta_pct:+.1f}%)", delta_color="inverse")
    
    with col2:
        avg_4w = prov_df.tail(4)['cases'].mean()
        st.metric("📈 4-Week Avg", f"{avg_4w:.0f}")
    
    with col3:
        change = next_pred - current
        change_pct = (change / current * 100) if current > 0 else 0
        st.metric("🔮 Next Week", f"{next_pred:.0f}", 
                 f"{change:+.0f} ({change_pct:+.1f}%)", delta_color="inverse")
    
    with col4:
        peak = prov_df[prov_df['year'] == year_range[1]]['cases'].max()
        st.metric(f"⚡ {year_range[1]} Peak", f"{peak:,}")
    
    with col5:
        total = prov_df[prov_df['year'] == year_range[1]]['cases'].sum()
        st.metric(f"📅 {year_range[1]} Total", f"{total:,}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ========================================================================
    # TABS
    # ========================================================================
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Forecast & Trends",
        "🌡️ Climate Analysis",
        "🎯 Model Performance",
        "📊 Multi-Province"
    ])
    
    # TAB 1: FORECAST
    with tab1:
        st.markdown("### Epidemiological Forecast")
        
        hist_plot = prov_df.tail(52)
        
        fig = go.Figure()
        
        # Historical
        fig.add_trace(go.Scatter(
            x=hist_plot['date'], y=hist_plot['cases'],
            mode='lines+markers',
            name='Observed',
            line=dict(color='#1a1a1a', width=2.5),
            marker=dict(size=5),
            hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Cases: %{y}<extra></extra>'
        ))
        
        # Forecast
        fig.add_trace(go.Scatter(
            x=forecast_df['date'], y=forecast_df['mean'],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#3b82f6', width=2.5, dash='dash'),
            marker=dict(size=6, symbol='diamond'),
            hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Predicted: %{y:.1f}<extra></extra>'
        ))
        
        # Confidence interval
        if show_ci:
            fig.add_trace(go.Scatter(
                x=forecast_df['date'].tolist() + forecast_df['date'].tolist()[::-1],
                y=forecast_df['upper'].tolist() + forecast_df['lower'].tolist()[::-1],
                fill='toself',
                fillcolor='rgba(59, 130, 246, 0.2)',
                line=dict(width=0),
                name='95% CI',
                hoverinfo='skip'
            ))
        
        # Alert threshold
        fig.add_hline(y=avg * 1.5, line_dash="dot", line_color="#ffa500",
                     annotation_text=f"Alert ({avg*1.5:.0f})")
        
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family='Inter', size=12),
            xaxis=dict(title='Week', gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0'),
            yaxis=dict(title='Cases', gridcolor='#f0f0f0', showline=True, linecolor='#e0e0e0'),
            hovermode='x unified',
            legend=dict(orientation='h', y=1.05, x=0),
            height=500,
            margin=dict(l=60, r=30, t=80, b=60)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Trend decomposition
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Rolling Averages")
            recent = prov_df.tail(52)
            ma4 = recent['cases'].rolling(4, center=True).mean()
            ma8 = recent['cases'].rolling(8, center=True).mean()
            
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=recent['date'], y=recent['cases'], 
                                     mode='lines', name='Weekly', 
                                     line=dict(color='#e0e0e0', width=1)))
            fig2.add_trace(go.Scatter(x=recent['date'], y=ma4, 
                                     mode='lines', name='4-Week MA',
                                     line=dict(color='#6b6b6b', width=2)))
            fig2.add_trace(go.Scatter(x=recent['date'], y=ma8, 
                                     mode='lines', name='8-Week MA',
                                     line=dict(color='#1a1a1a', width=2.5)))
            
            fig2.update_layout(
                plot_bgcolor='white', paper_bgcolor='white',
                font=dict(family='Inter'), height=300,
                xaxis=dict(gridcolor='#f5f5f5'), yaxis=dict(gridcolor='#f5f5f5'),
                legend=dict(orientation='h', y=-0.2), margin=dict(l=50, r=20, t=20, b=60)
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        with col2:
            st.markdown("#### Week-over-Week Change")
            changes = recent['cases'].diff()
            colors = ['#ef4444' if x < 0 else '#22c55e' for x in changes]
            
            fig3 = go.Figure(go.Bar(x=recent['date'], y=changes, 
                                   marker=dict(color=colors, opacity=0.7)))
            fig3.add_hline(y=0, line_color='#1a1a1a', line_width=1)
            fig3.update_layout(
                plot_bgcolor='white', paper_bgcolor='white',
                font=dict(family='Inter'), height=300,
                xaxis=dict(gridcolor='#f5f5f5'), yaxis=dict(gridcolor='#f5f5f5', title='Change'),
                showlegend=False, margin=dict(l=50, r=20, t=20, b=60)
            )
            st.plotly_chart(fig3, use_container_width=True)
    
    # TAB 2: CLIMATE
    with tab2:
        st.markdown("### Climate Drivers & Correlation Analysis")
        
        climate_data = prov_df.tail(52)
        
        fig_climate = make_subplots(
            rows=3, cols=1,
            subplot_titles=('Temperature (°C)', 'Humidity (%)', 'Rainfall (mm)'),
            vertical_spacing=0.1
        )
        
        fig_climate.add_trace(go.Scatter(
            x=climate_data['date'], y=climate_data['temp'],
            fill='tozeroy', fillcolor='rgba(239, 68, 68, 0.15)',
            line=dict(color='#ef4444', width=2), name='Temp'
        ), row=1, col=1)
        
        fig_climate.add_trace(go.Scatter(
            x=climate_data['date'], y=climate_data['humidity'],
            fill='tozeroy', fillcolor='rgba(59, 130, 246, 0.15)',
            line=dict(color='#3b82f6', width=2), name='Humidity'
        ), row=2, col=1)
        
        fig_climate.add_trace(go.Bar(
            x=climate_data['date'], y=climate_data['rainfall'],
            marker=dict(color='#06b6d4', opacity=0.7), name='Rainfall'
        ), row=3, col=1)
        
        fig_climate.update_xaxes(gridcolor='#f0f0f0')
        fig_climate.update_yaxes(gridcolor='#f0f0f0')
        fig_climate.update_layout(
            plot_bgcolor='white', paper_bgcolor='white',
            font=dict(family='Inter'), height=700,
            showlegend=False, margin=dict(l=60, r=30, t=60, b=40)
        )
        
        st.plotly_chart(fig_climate, use_container_width=True)
        
        # Current conditions
        st.markdown("#### Current Conditions")
        col1, col2, col3, col4 = st.columns(4)
        
        curr_temp = prov_df.iloc[-1]['temp']
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">Temperature</p>
                <p class="data-point">{curr_temp:.1f}°C</p>
            </div>
            """, unsafe_allow_html=True)
        
        curr_hum = prov_df.iloc[-1]['humidity']
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">Humidity</p>
                <p class="data-point">{curr_hum:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        curr_rain = prov_df.iloc[-1]['rainfall']
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">This Week Rain</p>
                <p class="data-point">{curr_rain:.0f}mm</p>
            </div>
            """, unsafe_allow_html=True)
        
        monthly_rain = prov_df.tail(4)['rainfall'].sum()
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">4-Week Rain</p>
                <p class="data-point">{monthly_rain:.0f}mm</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Cross-correlation
        st.markdown("#### Cross-Correlation Analysis")
        lags = range(0, 9)
        temp_corr = [prov_df['cases'].corr(prov_df['temp'].shift(l)) for l in lags]
        hum_corr = [prov_df['cases'].corr(prov_df['humidity'].shift(l)) for l in lags]
        rain_corr = [prov_df['cases'].corr(prov_df['rainfall'].shift(l)) for l in lags]
        
        fig_corr = go.Figure()
        fig_corr.add_trace(go.Scatter(x=list(lags), y=temp_corr, mode='lines+markers',
                                     name='Temperature', line=dict(color='#ef4444', width=2.5)))
        fig_corr.add_trace(go.Scatter(x=list(lags), y=hum_corr, mode='lines+markers',
                                     name='Humidity', line=dict(color='#3b82f6', width=2.5)))
        fig_corr.add_trace(go.Scatter(x=list(lags), y=rain_corr, mode='lines+markers',
                                     name='Rainfall', line=dict(color='#06b6d4', width=2.5)))
        
        fig_corr.add_hline(y=0, line_dash="dot", line_color="#999")
        fig_corr.update_layout(
            title='Lagged Correlation with Dengue Cases',
            plot_bgcolor='white', paper_bgcolor='white',
            font=dict(family='Inter'), height=350,
            xaxis=dict(title='Lag (weeks)', gridcolor='#f0f0f0', dtick=1),
            yaxis=dict(title='Correlation', gridcolor='#f0f0f0'),
            legend=dict(orientation='h', y=-0.2), margin=dict(l=60, r=30, t=50, b=80)
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    
    # TAB 3: MODEL PERFORMANCE
    with tab3:
        st.markdown("### Model Validation & Performance Metrics")
        
        metrics = get_metrics(province)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">MAE</p>
                <p class="data-point" style="font-size: 2rem;">{metrics['MAE']}</p>
                <p style="font-size: 0.75rem; color: #6b6b6b; margin: 0;">Mean Absolute Error</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">RMSE</p>
                <p class="data-point" style="font-size: 2rem;">{metrics['RMSE']}</p>
                <p style="font-size: 0.75rem; color: #6b6b6b; margin: 0;">Root Mean Sq Error</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">R²</p>
                <p class="data-point" style="font-size: 2rem;">{metrics['R2']:.2f}</p>
                <p style="font-size: 0.75rem; color: #6b6b6b; margin: 0;">Coefficient of Determ.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">Correlation</p>
                <p class="data-point" style="font-size: 2rem;">{metrics['Corr']:.2f}</p>
                <p style="font-size: 0.75rem; color: #6b6b6b; margin: 0;">Pearson r</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col5:
            st.markdown(f"""
            <div class="stat-card">
                <p class="data-label">CRPS</p>
                <p class="data-point" style="font-size: 2rem;">{metrics['CRPS']}</p>
                <p style="font-size: 0.75rem; color: #6b6b6b; margin: 0;">Prob. Skill Score</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Feature importance
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("#### Feature Importance")
            features = ['Cases lag-1', 'Temperature (2w)', 'Humidity (1w)', 
                       'Rainfall (4w)', 'Week-of-year', 'Rolling mean-4']
            importance = [0.34, 0.26, 0.19, 0.11, 0.06, 0.04]
            
            fig_imp = go.Figure(go.Bar(
                y=features, x=importance, orientation='h',
                marker=dict(color='#1a1a1a')
            ))
            fig_imp.update_layout(
                plot_bgcolor='white', paper_bgcolor='white',
                font=dict(family='Inter'), height=300,
                xaxis=dict(title='Relative Importance', gridcolor='#f0f0f0'),
                yaxis=dict(gridcolor='#f0f0f0'),
                margin=dict(l=150, r=20, t=20, b=50)
            )
            st.plotly_chart(fig_imp, use_container_width=True)
        
        with col2:
            st.markdown("#### Validation Strategy")
            st.markdown("""
            <div class="alert-card alert-info">
                <strong>Cross-Validation</strong><br>
                Blocked forward-chaining<br>
                <span class="badge badge-gray">80/20 split</span><br><br>
                <strong>Test Period</strong><br>
                Last 20% of time series<br><br>
                <strong>Hyperparameters</strong><br>
                Bayesian optimization
            </div>
            """, unsafe_allow_html=True)
        
        # Forecast table
        st.markdown("#### Detailed Forecast")
        forecast_table = forecast_df.copy()
        forecast_table['date'] = forecast_table['date'].dt.strftime('%Y-%m-%d')
        forecast_table.columns = ['Week Starting', 'Predicted', 'Lower 95%', 'Upper 95%', 'Uncertainty']
        st.dataframe(forecast_table, use_container_width=True, hide_index=True)
    
    # TAB 4: MULTI-PROVINCE
    with tab4:
        st.markdown("### Multi-Province Comparison")
        
        # Get recent data for all provinces
        all_recent = df[df['year'] == year_range[1]].groupby('province').agg({
            'cases': ['sum', 'mean', 'max']
        }).round(1)
        all_recent.columns = ['Total Cases', 'Weekly Average', 'Peak Week']
        all_recent = all_recent.reset_index()
        
        # Comparison chart
        fig_comp = go.Figure()
        
        for prov in df['province'].unique():
            prov_ts = df[(df['province'] == prov) & (df['year'] == year_range[1])]
            fig_comp.add_trace(go.Scatter(
                x=prov_ts['date'], y=prov_ts['cases'],
                mode='lines', name=prov,
                line=dict(width=2.5)
            ))
        
        fig_comp.update_layout(
            title=f'All Provinces - {year_range[1]} Comparison',
            plot_bgcolor='white', paper_bgcolor='white',
            font=dict(family='Inter'), height=450,
            xaxis=dict(title='Week', gridcolor='#f0f0f0'),
            yaxis=dict(title='Cases', gridcolor='#f0f0f0'),
            legend=dict(orientation='h', y=-0.15),
            margin=dict(l=60, r=30, t=50, b=80)
        )
        st.plotly_chart(fig_comp, use_container_width=True)
        
        # Summary table
        st.markdown("#### Province Summary Statistics")
        st.dataframe(all_recent, use_container_width=True, hide_index=True)
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6b6b6b; font-size: 0.85rem; padding: 2rem 0 1rem 0;">
        <strong>Dengue Early Warning System for Thailand</strong><br>
        Province-level retrospective assessment and cross-validated prediction<br>
        <em>Data: Thailand Ministry of Public Health (DDC) • Climate: TMD/Google Earth Engine</em><br>
        Methods: XGBoost with lagged meteorological & surveillance features<br>
        <span class="badge badge-gray">Demo with Synthetic Data</span>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
