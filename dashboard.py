import pandas as pd
import streamlit as st
import plotly.express as px

# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="SmogNet Intelligence Dashboard",
    page_icon="🌫️",
    layout="wide"
)

# ==============================
# Professional Custom Styling
# ==============================

st.markdown("""
<style>

/* Main app background */
.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1e293b 100%);
    color: #f8fafc;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617 0%, #111827 100%);
    border-right: 1px solid rgba(255,255,255,0.1);
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

/* Header title */
.big-title {
    font-size: 46px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 5px;
}

/* Section headings */
h1, h2, h3 {
    color: #ffffff !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.12);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.25);
}

div[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
    font-size: 15px;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 34px;
    font-weight: 800;
}

/* Health status card */
.status-card {
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #ef4444, #991b1b);
    box-shadow: 0px 8px 24px rgba(239,68,68,0.35);
    text-align: center;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.18);
}

.status-card h4 {
    color: #fee2e2 !important;
    margin-bottom: 8px;
}

.status-card h2 {
    color: #ffffff !important;
    font-size: 32px;
    font-weight: 900;
}

.status-safe {
    background: linear-gradient(135deg, #22c55e, #166534);
    box-shadow: 0px 8px 24px rgba(34,197,94,0.35);
}

.status-moderate {
    background: linear-gradient(135deg, #f59e0b, #92400e);
    box-shadow: 0px 8px 24px rgba(245,158,11,0.35);
}

.status-danger {
    background: linear-gradient(135deg, #ef4444, #991b1b);
    box-shadow: 0px 8px 24px rgba(239,68,68,0.35);
}

.status-emergency {
    background: linear-gradient(135deg, #7f1d1d, #450a0a);
    box-shadow: 0px 8px 24px rgba(127,29,29,0.45);
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 14px;
    border: none;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 700;
    color: #cbd5e1;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #38bdf8;
    border-bottom: 3px solid #38bdf8;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* Plotly chart container */
div[data-testid="stPlotlyChart"] {
    background: rgba(255,255,255,0.06);
    padding: 14px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Download button */
.stDownloadButton button {
    background: linear-gradient(135deg, #0ea5e9, #2563eb);
    color: white;
    border-radius: 12px;
    padding: 12px 22px;
    border: none;
    font-weight: 700;
}

.stDownloadButton button:hover {
    background: linear-gradient(135deg, #0284c7, #1d4ed8);
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# Load Data
# ==============================

data = pd.read_csv("cleaned_air_quality_data.csv")
final_output = pd.read_csv("final_smognet_output.csv")

data["datetime"] = pd.to_datetime(data["datetime"])
final_output["datetime"] = pd.to_datetime(final_output["datetime"])

data = data.sort_values("datetime")
final_output = final_output.sort_values("datetime")

# ==============================
# Helper Functions
# ==============================

def calculate_risk_score(row):
    pm25_score = min(row["components_pm2_5"] / 250 * 40, 40)
    pm10_score = min(row["components_pm10"] / 300 * 25, 25)
    aqi_score = min(row["main_aqi"] / 5 * 25, 25)
    no2_score = min(row["components_no2"] / 100 * 10, 10)

    total_score = pm25_score + pm10_score + aqi_score + no2_score
    return round(min(total_score, 100), 2)


def get_status(score):
    if score >= 80:
        return "Emergency", "status-emergency"
    elif score >= 60:
        return "Dangerous", "status-danger"
    elif score >= 35:
        return "Moderate Risk", "status-moderate"
    else:
        return "Relatively Safe", "status-safe"


def get_recommendation(status):
    if status == "Emergency":
        return "Avoid outdoor activities completely. Children, elderly people, and respiratory patients should stay indoors. Use masks and keep windows closed."
    elif status == "Dangerous":
        return "Limit outdoor movement. Sensitive groups should avoid going outside. Use masks when necessary."
    elif status == "Moderate Risk":
        return "Air quality is not ideal. Sensitive people should reduce outdoor activity."
    else:
        return "Air quality is comparatively better, but regular monitoring is still recommended."


# ==============================
# Header
# ==============================

st.markdown("""
<div style="padding: 35px 30px; border-radius: 24px; 
background: linear-gradient(135deg, rgba(14,165,233,0.25), rgba(37,99,235,0.18)); 
border: 1px solid rgba(255,255,255,0.15); 
box-shadow: 0px 10px 30px rgba(0,0,0,0.25);">

<div class="big-title">🌫️ SmogNet Intelligence Dashboard</div>
<div class="subtitle">
AI-powered air quality monitoring system for pollution spike detection, source classification, risk scoring, and public health alerts.
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==============================
# Sidebar
# ==============================

st.sidebar.title("🔍 Dashboard Controls")

cities = sorted(data["City"].unique())
selected_city = st.sidebar.selectbox("Select City", cities)

city_data = data[data["City"] == selected_city].copy()
city_spikes = final_output[final_output["City"] == selected_city].copy()

city_data["risk_score"] = city_data.apply(calculate_risk_score, axis=1)
latest_row = city_data.sort_values("datetime").iloc[-1]

latest_score = latest_row["risk_score"]
status, status_class = get_status(latest_score)
recommendation = get_recommendation(status)

# ==============================
# Main Status Cards
# ==============================

st.subheader("📌 Live City Pollution Status")

col1, col2, col3, col4 = st.columns([1.2, 1, 1, 1.4])

col1.metric("Selected City", selected_city)
col2.metric("Latest PM2.5", round(latest_row["components_pm2_5"], 2))
col3.metric("Risk Score", f"{latest_score}/100")

col4.markdown(
    f"""
    <div class="status-card {status_class}">
        <h4>Health Status</h4>
        <h2>{status}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.info(f"Smart Recommendation: {recommendation}")

# ==============================
# Tabs
# ==============================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "📈 Trends",
        "🏙️ City Ranking",
        "🧪 Pollutant Fingerprint",
        "🚨 Spikes & Sources",
        "📢 Public Alerts",
        "ℹ️ Methodology"
    ]
)

# ==============================
# Tab 1: Trends
# ==============================

with tab1:
    st.subheader(f"PM2.5 Trend Over Time - {selected_city}")

    fig_pm25 = px.line(
        city_data,
        x="datetime",
        y="components_pm2_5",
        title=f"PM2.5 Trend in {selected_city}",
        labels={
            "datetime": "Date and Time",
            "components_pm2_5": "PM2.5 Level"
        }
    )

    st.plotly_chart(fig_pm25, use_container_width=True)

    st.subheader("Hourly Pollution Heatmap")

    city_data["hour"] = city_data["datetime"].dt.hour
    city_data["month"] = city_data["datetime"].dt.month

    heatmap_data = city_data.pivot_table(
        index="hour",
        columns="month",
        values="components_pm2_5",
        aggfunc="mean"
    )

    fig_heatmap = px.imshow(
        heatmap_data,
        title=f"Average PM2.5 by Hour and Month - {selected_city}",
        labels=dict(x="Month", y="Hour of Day", color="PM2.5")
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)

# ==============================
# Tab 2: City Ranking
# ==============================

with tab2:
    st.subheader("Most Polluted Cities Ranking")

    ranking = data.groupby("City").agg(
        avg_pm25=("components_pm2_5", "mean"),
        avg_pm10=("components_pm10", "mean"),
        avg_aqi=("main_aqi", "mean")
    ).reset_index()

    ranking["risk_score"] = (
        ranking["avg_pm25"] / ranking["avg_pm25"].max() * 50 +
        ranking["avg_pm10"] / ranking["avg_pm10"].max() * 30 +
        ranking["avg_aqi"] / ranking["avg_aqi"].max() * 20
    ).round(2)

    ranking = ranking.sort_values("risk_score", ascending=False)

    fig_rank = px.bar(
        ranking,
        x="City",
        y="risk_score",
        title="City-wise Pollution Risk Ranking",
        labels={"risk_score": "Risk Score"}
    )

    st.plotly_chart(fig_rank, use_container_width=True)

    st.dataframe(ranking, use_container_width=True)

# ==============================
# Tab 3: Pollutant Fingerprint
# ==============================

with tab3:
    st.subheader(f"Pollutant Fingerprint - {selected_city}")

    pollutant_values = {
        "PM2.5": latest_row["components_pm2_5"],
        "PM10": latest_row["components_pm10"],
        "CO": latest_row["components_co"],
        "NO": latest_row["components_no"],
        "NO2": latest_row["components_no2"],
        "SO2": latest_row["components_so2"],
        "NH3": latest_row["components_nh3"],
        "O3": latest_row["components_o3"]
    }

    fingerprint_df = pd.DataFrame({
        "Pollutant": list(pollutant_values.keys()),
        "Value": list(pollutant_values.values())
    })

    fig_fingerprint = px.bar(
        fingerprint_df,
        x="Pollutant",
        y="Value",
        title=f"Latest Pollutant Composition in {selected_city}",
        labels={"Value": "Pollutant Level"}
    )

    st.plotly_chart(fig_fingerprint, use_container_width=True)

    highest_pollutant = fingerprint_df.sort_values("Value", ascending=False).iloc[0]

    st.warning(
        f"Dominant pollutant in latest record: {highest_pollutant['Pollutant']} "
        f"with value {round(highest_pollutant['Value'], 2)}"
    )

# ==============================
# Tab 4: Spikes and Sources
# ==============================

with tab4:
    st.subheader(f"Detected Pollution Spikes - {selected_city}")

    if len(city_spikes) > 0:
        col_a, col_b = st.columns(2)

        with col_a:
            st.metric("Total Detected Spikes", len(city_spikes))

        with col_b:
            most_common_source = city_spikes["probable_source"].value_counts().idxmax()
            st.metric("Most Common Source", most_common_source)

        source_count = city_spikes["probable_source"].value_counts().reset_index()
        source_count.columns = ["Probable Source", "Count"]

        fig_source = px.pie(
            source_count,
            names="Probable Source",
            values="Count",
            title=f"Pollution Source Distribution - {selected_city}"
        )

        st.plotly_chart(fig_source, use_container_width=True)

        st.dataframe(
            city_spikes[
                [
                    "datetime",
                    "City",
                    "components_pm2_5",
                    "components_pm10",
                    "pm25_spike_threshold",
                    "probable_source"
                ]
            ],
            use_container_width=True
        )

    else:
        st.success("No PM2.5 spikes detected for this city.")

# ==============================
# Tab 5: Public Alerts
# ==============================

with tab5:
    st.subheader(f"Generated Public Health Alerts - {selected_city}")

    if len(city_spikes) > 0:
        for index, row in city_spikes.head(10).iterrows():
            st.error(row["public_alert"])

        csv = city_spikes.to_csv(index=False)

        st.download_button(
            label="Download Alerts for Selected City",
            data=csv,
            file_name=f"{selected_city}_smognet_alerts.csv",
            mime="text/csv"
        )
    else:
        st.info("No public alerts generated for this city.")

# ==============================
# Tab 6: Methodology
# ==============================

with tab6:
    st.subheader("ℹ️ Project Methodology")

    st.markdown("""
    ### 1. Data Preparation
    We collected air quality data from multiple Pakistani cities and combined all CSV files into one dataset.
    After that, we cleaned the dataset by handling missing values, removing duplicate records, and converting the datetime column into proper date-time format.

    ### 2. Spike Detection
    We used **city-wise adaptive thresholding** for PM2.5 spike detection.

    Instead of using one fixed threshold for all cities, we calculated a separate threshold for each city.

    **Formula:**

    `Threshold = Mean PM2.5 + 2 × Standard Deviation`

    If the current PM2.5 value is greater than this threshold, it is detected as a pollution spike.

    ### 3. Source Classification
    After detecting spikes, we classified the probable pollution source using pollutant signatures.

    - High NH₃ + CO → Crop Burning
    - High NO + NO₂ → Vehicular Emissions
    - High SO₂ → Industrial Emissions
    - PM10 much greater than PM2.5 → Dust Storm
    - Mixed pollutant patterns → Mixed Sources

    ### 4. Public Alert Generation
    Finally, public health alerts were generated in simple language.
    Each alert includes the city name, probable cause, affected groups, and recommended safety actions.

    ### 5. Future Improvements
    In the future, this system can be improved by adding real-time sensor data, machine learning-based anomaly detection, SMS/mobile alerts, map visualization, and more accurate source classification using labeled pollution events.
    """)

# ==============================
# Footer
# ==============================

st.markdown("---")
st.caption("SmogNet Dashboard | Built for Air Quality Intelligence, Spike Detection, Source Classification, and Public Health Communication")