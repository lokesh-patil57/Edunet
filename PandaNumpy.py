import pandas as pd
import numpy as np

#sample data with missing values

data={
    "Energy source": ["solar", "wind", "hydro", "geothermal", "biomass", "tidal"],
    "Energy comsumption (MWh)": [1200, np.nan, 2900, np.nan,2500,3200],
    "cost(Million $)": [200,400, np.nan, 150,250,np.nan]
}

#Create a DataFrame
energy_df = pd.DataFrame(data)
print("Initial Energy DataFrame with Missing Values:")
print(energy_df)

#remove row with any missing values
cleaned_df = energy_df.dropna(axis=0)

print("\nCleaned Energy DataFrame (Rows with Missing Values Removed):")
print(cleaned_df)


#Fill missing values with mean

ec_mean = energy_df["Energy comsumption (MWh)"].mean()
cost_mean = energy_df["cost(Million $)"].mean() 
print(f"\nMean Energy Consumption (MWh): {ec_mean}")
print(f"Mean Cost (Million $): {cost_mean}")    


#Impute missing values in energy Consumption(MWh) with mean

energy_df["Energy comsumption (MWh)"].fillna(ec_mean, inplace=True)

#Impute missing values in cost(Million $) with mean
energy_df["cost(Million $)"].fillna(cost_mean, inplace=True)

print("\nEnergy DataFrame after Imputing Missing Values with Mean:")
energy_df.head()
print(energy_df)