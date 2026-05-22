import pandas as pd

# Read cleaned data
data = pd.read_csv("cleaned_air_quality_data.csv")

# Convert datetime
data["datetime"] = pd.to_datetime(data["datetime"])

# Calculate city-wise mean and standard deviation for PM2.5
city_stats = data.groupby("City")["components_pm2_5"].agg(["mean", "std"]).reset_index()

# Rename columns
city_stats.columns = ["City", "pm25_mean", "pm25_std"]

# Merge city stats back with original data
data = data.merge(city_stats, on="City", how="left")

# Create spike threshold
# Spike = PM2.5 greater than city average + 2 * standard deviation
data["pm25_spike_threshold"] = data["pm25_mean"] + (2 * data["pm25_std"])

# Detect spike
data["is_pm25_spike"] = data["components_pm2_5"] > data["pm25_spike_threshold"]

# Show detected spikes
spikes = data[data["is_pm25_spike"] == True]

print("Total PM2.5 spikes detected:", len(spikes))

print("\nSample detected spikes:")
print(spikes[["datetime", "City", "components_pm2_5", "pm25_spike_threshold"]].head(20))

# Save spike results
data.to_csv("spike_detection_results.csv", index=False)
spikes.to_csv("detected_pm25_spikes.csv", index=False)

print("\nSpike detection completed successfully!")
print("Files saved:")
print("1. spike_detection_results.csv")
print("2. detected_pm25_spikes.csv")