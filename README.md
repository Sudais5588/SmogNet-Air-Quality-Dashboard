# SmogNet Air Quality Intelligence Dashboard

Live Dashboard: https://hamdan-smognet.streamlit.app/

SmogNet is an air quality intelligence system that detects pollution spikes, classifies probable pollution sources, and generates public health alerts using air quality data from Pakistani cities.

## Project Overview

Air pollution is a serious environmental and public health issue, especially in urban areas. Many cities experience high levels of pollutants such as PM2.5, PM10, CO, NO2, SO2, NH3, and O3. These pollutants can affect public health, especially children, elderly people, and patients with respiratory diseases.

This project focuses on analyzing air quality data, detecting abnormal PM2.5 pollution spikes, identifying possible emission sources, and communicating risk through simple public alerts.

The project works as an end-to-end pipeline:

```text
Raw Data → Data Cleaning → Spike Detection → Source Classification → Public Alert Generation → Dashboard Visualization
```

## Objectives

The main objectives of this project are:

- To combine air quality data from multiple Pakistani cities
- To clean and prepare the dataset for analysis
- To analyze pollution patterns city-wise
- To detect abnormal PM2.5 pollution spikes
- To classify the probable source of pollution
- To generate public health alerts in simple language
- To display results in an interactive dashboard

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
- Smart health recommendation
- City-wise pollution ranking
- Pollutant fingerprint visualization
- Hourly pollution heatmap
- Detected pollution spike table
- Source classification summary
- Downloadable final CSV output

## Dataset Overview

The dataset contains air quality and weather-related data from different Pakistani cities. Each row represents air quality conditions at a specific date and time for a specific city.

The dataset includes pollutant concentration values and weather-related features.

## Dataset Columns

Important columns used in this project include:

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
- surface pressure
- wind speed
- wind direction
- shortwave radiation
- city

## Pollutant Components

The major pollutant components used in this project are:

| Component | Meaning |
|---|---|
| PM2.5 | Particulate Matter 2.5 |
| PM10 | Particulate Matter 10 |
| CO | Carbon Monoxide |
| NO | Nitric Oxide |
| NO2 | Nitrogen Dioxide |
| SO2 | Sulfur Dioxide |
| NH3 | Ammonia |
| O3 | Ozone |

## Project Workflow

### 1. Data Reading

The project starts by reading multiple CSV files containing air quality data from different cities.

### 2. Data Combining

All city-wise CSV files are combined into one dataset. A city column is added so that each record can be linked to its city.

### 3. Data Cleaning

The combined dataset is cleaned before analysis.

Cleaning steps include:

- Converting datetime into proper date-time format
- Removing duplicate records
- Handling missing values
- Sorting data by city and time
- Saving the cleaned dataset

### 4. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand pollution patterns.

EDA includes:

- Average PM2.5 by city
- Average PM10 by city
- AQI category distribution
- PM2.5 trend over time
- City-wise pollution comparison

### 5. Spike Detection

PM2.5 spike detection was performed using a city-wise adaptive thresholding method.

### 6. Source Classification

Detected spikes were classified into probable pollution sources using pollutant patterns.

### 7. Public Alert Generation

For each detected pollution spike, a public health alert was generated in simple language.

### 8. Dashboard Visualization

The final results were displayed using an interactive Streamlit dashboard.

## Methods Used

### 1. Data Cleaning and Preprocessing

The raw CSV files from different cities were first combined into a single dataset. After combining the data, basic cleaning steps were applied.

Cleaning steps included:

- Combining multiple CSV files
- Adding a city column
- Converting datetime into proper date-time format
- Removing duplicate records
- Handling missing values
- Sorting data by city and time

This step was important because clean data is required before performing analysis, spike detection, and dashboard visualization.

## 2. Spike Detection Method

For pollution spike detection, city-wise adaptive thresholding was used.

Instead of using one fixed value for all cities, a separate threshold was calculated for each city. This is useful because pollution levels are different in every city.

Formula:

```text
Threshold = Mean PM2.5 + 2 × Standard Deviation
```

If the PM2.5 value is greater than the calculated city-specific threshold, it is detected as a pollution spike.

This method makes the system more context-aware because a PM2.5 value that is normal for one city may be abnormal for another city.

## 3. Source Classification Method

After detecting pollution spikes, rule-based pollutant fingerprint classification was used to classify the probable pollution source.

Rules used:

| Pollutant Pattern | Probable Source |
|---|---|
| High NH3 + CO | Crop Burning |
| High NO + NO2 | Vehicular Emissions |
| High SO2 | Industrial Emissions |
| PM10 much greater than PM2.5 | Dust Storm |
| Mixed pollutant patterns | Mixed Sources |

This approach was used because the dataset did not contain labeled source categories. Therefore, pollutant relationships were used to estimate the possible cause of pollution spikes.

## 4. NLP Method

Template-based Natural Language Generation was used to create public health alerts.

This method converts technical results into simple public messages.

Each alert includes:

- City name
- PM2.5 level
- Probable pollution source
- Affected population groups
- Recommended safety actions

Example alert:

```text
Air pollution has increased in Islamabad, with PM2.5 reaching 310.7.
The probable cause of this pollution spike is Crop Burning.
Children, elderly people, and respiratory patients should avoid outdoor activities.
People are advised to wear masks, keep windows closed, and limit unnecessary travel.
```

## Dashboard Features

The Streamlit dashboard presents the results in an interactive and easy-to-understand format.

Dashboard includes:

- City selection filter
- PM2.5 trend over time
- Pollution risk score
- Health status indicator
- Smart recommendation
- City-wise pollution ranking
- Pollutant fingerprint chart
- Hourly pollution heatmap
- Detected pollution spikes
- Source classification summary
- Generated public health alerts
- Download final CSV output button
- Methodology section

## Risk Score

The dashboard includes a pollution risk score. The risk score is calculated using important air quality factors such as:

- PM2.5
- PM10
- AQI category
- NO2

The score helps users quickly understand how risky the air quality condition is for the selected city.

## Health Status

Based on the risk score, the dashboard shows a health status such as:

- Relatively Safe
- Moderate Risk
- Dangerous
- Emergency

This makes the dashboard easier to understand for non-technical users.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- GitHub
- Streamlit Cloud

## Project Files

Important files in this project:

```text
dashboard.py
final_pipeline.py
read_data.py
clean_data.py
eda.py
spike_detection.py
source_classification.py
alert_generation.py
cleaned_air_quality_data.csv
final_smognet_output.csv
requirements.txt
README.md
```

## How to Run Locally

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

## Final Output

The final output contains:

- Detected PM2.5 pollution spikes
- City-wise spike threshold
- Probable pollution source
- Generated public health alert
- Downloadable CSV output

## Limitations

- Source classification is rule-based and not trained on labeled pollution source data.
- The dashboard uses historical dataset values, not live sensor data.
- Spike detection is currently focused mainly on PM2.5.
- Public alerts are generated using templates, not a large language model.
- More accurate results would require verified ground-truth pollution source labels.

## Future Improvements

- Add real-time sensor data
- Use machine learning-based anomaly detection
- Add map-based city visualization
- Add SMS/mobile alert system
- Improve source classification using labeled pollution events
- Add more pollutant-specific health recommendations
- Add forecasting for future pollution levels
- Deploy with a cleaner custom domain in the future

## Author

Muhammad Sudais  
CS Student | Web Development | AI & Data Science | Python Developer

## Project Status

Completed and deployed.
