import pandas as pd

# Read CSV files
islamabad = pd.read_csv("Islamabad_pakistan_air_quality.csv")
karachi = pd.read_csv("Karachi.CSV")
lahore = pd.read_csv("Lahore_pak.CSV")
peshawar = pd.read_csv("peshawar.CSV")
quetta = pd.read_csv("Quetta_pak_ai.CSV")

# Add city column to each dataset
islamabad["City"] = "Islamabad"
karachi["City"] = "Karachi"
lahore["City"] = "Lahore"
peshawar["City"] = "Peshawar"
quetta["City"] = "Quetta"

# Combine all datasets
combined_data = pd.concat(
    [islamabad, karachi, lahore, peshawar, quetta],
    ignore_index=True
)

# Check combined data
print("\nCombined Data:")
print(combined_data.head())

print("\nShape of combined data:")
print(combined_data.shape)

print("\nColumns:")
print(combined_data.columns)

# Save combined dataset
combined_data.to_csv("combined_air_quality_data.csv", index=False)

print("\nCombined CSV file saved successfully!")