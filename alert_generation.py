import pandas as pd

# Read classified spikes file
spikes = pd.read_csv("classified_pollution_spikes.csv")

# Function to generate public alert
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

# Generate public alerts
spikes["public_alert"] = spikes.apply(generate_alert, axis=1)

# Show full sample alerts in terminal
print("Public alerts generated successfully!")

for index, row in spikes.head(5).iterrows():
    print("\nDate:", row["datetime"])
    print("City:", row["City"])
    print("Source:", row["probable_source"])
    print("Alert:", row["public_alert"])
    print("-" * 80)

# Save alerts file
spikes.to_csv("public_alerts.csv", index=False)

print("\nFile saved successfully: public_alerts.csv")