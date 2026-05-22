import pandas as pd

# ==============================
# Step 1: Read cleaned dataset
# ==============================
data = pd.read_csv("cleaned_air_quality_data.csv")
data["datetime"] = pd.to_datetime(data["datetime"])

print("Dataset loaded successfully!")


# ==============================
# Step 2: PM2.5 Spike Detection
# ==============================

# Calculate city-wise mean and standard deviation
city_stats = data.groupby("City")["components_pm2_5"].agg(["mean", "std"]).reset_index()
city_stats.columns = ["City", "pm25_mean", "pm25_std"]

# Merge statistics with main data
data = data.merge(city_stats, on="City", how="left")

# Create threshold
data["pm25_spike_threshold"] = data["pm25_mean"] + (2 * data["pm25_std"])

# Detect spike
data["is_pm25_spike"] = data["components_pm2_5"] > data["pm25_spike_threshold"]

# Filter spike rows
spikes = data[data["is_pm25_spike"] == True].copy()

print("Spike detection completed!")
print("Total PM2.5 spikes detected:", len(spikes))


# ==============================
# Step 3: Source Classification
# ==============================

def classify_source(row):
    pm25 = row["components_pm2_5"]
    pm10 = row["components_pm10"]
    co = row["components_co"]
    no = row["components_no"]
    no2 = row["components_no2"]
    so2 = row["components_so2"]
    nh3 = row["components_nh3"]

    if nh3 > spikes["components_nh3"].mean() and co > spikes["components_co"].mean():
        return "Crop Burning"

    elif no > spikes["components_no"].mean() and no2 > spikes["components_no2"].mean():
        return "Vehicular Emissions"

    elif so2 > spikes["components_so2"].mean():
        return "Industrial Emissions"

    elif pm10 > (1.5 * pm25):
        return "Dust Storm"

    else:
        return "Mixed Sources"


spikes["probable_source"] = spikes.apply(classify_source, axis=1)

print("Source classification completed!")
print("\nClassification Summary:")
print(spikes["probable_source"].value_counts())


# ==============================
# Step 4: Public Alert Generation
# ==============================

def generate_alert(row):
    city = row["City"]
    source = row["probable_source"]
    pm25 = round(row["components_pm2_5"], 2)

    alert = (
        f"Air pollution has increased in {city}, with PM2.5 reaching {pm25}. "
        f"The probable cause of this pollution spike is {source}. "
        f"Children, elderly people, and respiratory patients should avoid outdoor activities. "
        f"People are advised to wear masks, keep windows closed, and limit unnecessary travel."
    )

    return alert


spikes["public_alert"] = spikes.apply(generate_alert, axis=1)

print("\nPublic alert generation completed!")


# ==============================
# Step 5: Save Final Output
# ==============================

spikes.to_csv("final_smognet_output.csv", index=False)

print("\nFinal output file saved successfully: final_smognet_output.csv")


# ==============================
# Step 6: Show Sample Results
# ==============================

print("\nSample Final Alerts:")

for index, row in spikes.head(5).iterrows():
    print("\nDate:", row["datetime"])
    print("City:", row["City"])
    print("PM2.5:", row["components_pm2_5"])
    print("Source:", row["probable_source"])
    print("Alert:", row["public_alert"])
    print("-" * 80)