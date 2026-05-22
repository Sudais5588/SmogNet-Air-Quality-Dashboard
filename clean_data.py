import pandas as pd

# Read combined dataset
data = pd.read_csv("combined_air_quality_data.csv")

# Convert datetime column to proper date-time format
data["datetime"] = pd.to_datetime(data["datetime"], errors="coerce")

# Remove duplicate rows
data = data.drop_duplicates()

# Remove rows where datetime is missing or invalid
data = data.dropna(subset=["datetime"])

# Fill missing numeric values with column mean
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# Sort data by city and datetime
data = data.sort_values(by=["City", "datetime"])

# Save cleaned dataset
data.to_csv("cleaned_air_quality_data.csv", index=False)

print("Cleaning completed successfully!")
print("Cleaned data shape:", data.shape)

print("\nMissing values after cleaning:")
print(data.isnull().sum())