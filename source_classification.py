import pandas as pd

# Read detected spikes file
spikes = pd.read_csv("detected_pm25_spikes.csv")

# Function to classify pollution source
def classify_source(row):
    pm25 = row["components_pm2_5"]
    pm10 = row["components_pm10"]
    co = row["components_co"]
    no = row["components_no"]
    no2 = row["components_no2"]
    so2 = row["components_so2"]
    nh3 = row["components_nh3"]

    # Crop burning: high ammonia and carbon monoxide
    if nh3 > spikes["components_nh3"].mean() and co > spikes["components_co"].mean():
        return "Crop Burning"

    # Vehicular emissions: high NO and NO2
    elif no > spikes["components_no"].mean() and no2 > spikes["components_no2"].mean():
        return "Vehicular Emissions"

    # Industrial emissions: high SO2
    elif so2 > spikes["components_so2"].mean():
        return "Industrial Emissions"

    # Dust storm: PM10 much higher than PM2.5
    elif pm10 > (1.5 * pm25):
        return "Dust Storm"

    # Otherwise mixed source
    else:
        return "Mixed Sources"

# Apply classification
spikes["probable_source"] = spikes.apply(classify_source, axis=1)

# Show results
print("Source classification completed!")
print("\nClassification summary:")
print(spikes["probable_source"].value_counts())

print("\nSample classified spikes:")
print(spikes[["datetime", "City", "components_pm2_5", "components_pm10", "probable_source"]].head(20))

# Save classified results
spikes.to_csv("classified_pollution_spikes.csv", index=False)

print("\nFile saved: classified_pollution_spikes.csv")