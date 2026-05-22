# SmogNet Air Quality Intelligence Dashboard

SmogNet is an AI-powered air quality intelligence system that detects pollution spikes, classifies probable pollution sources, and generates public health alerts using air quality data from Pakistani cities.

## Project Overview

Air pollution is a serious environmental and public health issue. This project focuses on analyzing air quality data, detecting abnormal PM2.5 pollution spikes, identifying possible emission sources, and communicating risk through simple public alerts.

The project works as an end-to-end pipeline:

Raw Data → Data Cleaning → Spike Detection → Source Classification → Public Alert Generation → Dashboard Visualization

## Features

- Multi-city air quality data analysis
- Data cleaning and preprocessing
- PM2.5 spike detection
- City-wise adaptive thresholding
- Source classification using pollutant signatures
- Template-based public health alert generation
- Interactive Streamlit dashboard
- Pollution risk score
- Health status indicator
- City-wise pollution ranking
- Pollutant fingerprint visualization
- Hourly pollution heatmap
- Downloadable final output

## Dataset Columns

The dataset contains air quality and weather-related columns such as:

- datetime
- main_aqi
- PM2.5
- PM10
- CO
- NO
- NO2
- SO2
- NH3
- O3
- temperature
- humidity
- wind speed
- wind direction
- city

## Methods Used

### 1. Spike Detection

For spike detection, city-wise adaptive thresholding was used.

Formula:

```text
Threshold = Mean PM2.5 + 2 × Standard Deviation
