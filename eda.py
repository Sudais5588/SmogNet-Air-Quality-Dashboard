import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
data = pd.read_csv("cleaned_air_quality_data.csv")

# Convert datetime again
data["datetime"] = pd.to_datetime(data["datetime"])

# 1. Average PM2.5 by city
avg_pm25 = data.groupby("City")["components_pm2_5"].mean()

plt.figure(figsize=(8, 5))
avg_pm25.plot(kind="bar")
plt.title("Average PM2.5 by City")
plt.xlabel("City")
plt.ylabel("Average PM2.5")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Average PM10 by city
avg_pm10 = data.groupby("City")["components_pm10"].mean()

plt.figure(figsize=(8, 5))
avg_pm10.plot(kind="bar")
plt.title("Average PM10 by City")
plt.xlabel("City")
plt.ylabel("Average PM10")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. AQI count
aqi_count = data["main_aqi"].value_counts().sort_index()

plt.figure(figsize=(7, 5))
aqi_count.plot(kind="bar")
plt.title("AQI Category Count")
plt.xlabel("AQI Category")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# 4. PM2.5 trend over time for each city
for city in data["City"].unique():
    city_data = data[data["City"] == city]

    plt.figure(figsize=(10, 5))
    plt.plot(city_data["datetime"], city_data["components_pm2_5"])
    plt.title(f"PM2.5 Trend Over Time - {city}")
    plt.xlabel("Date")
    plt.ylabel("PM2.5")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()