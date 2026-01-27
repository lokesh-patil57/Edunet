import pandas as pd

#sample renewable energy source data

renewable_resources = ["solar", "wind", "hydro", "geothermal", "biomass"]

#create a series of renewable resources
resources_series = pd.Series(renewable_resources)

print("Renewable Energy Resources Series:")
print(resources_series)

#Sample green technology procject data (for DataFrame)
data = {
    "Project": ["Solar Farm A", "Wind Turbine X", "Hydro Plant Y", "Geothermal D", "Biomass E"],
    "Capacity_MW": [150, 300, 200, 50, 100],
    "Cost(Million $)": [200, 400, 350, 100, 250],
    "Location": ["California", "Texas", "Washington", "Nevada", "Tdaho"],
    "Completion_Year": [2023, 2024, 2022, 2025, 2023]
}

projects_df = pd.DataFrame(data)
print("\nGreen Technology Projects DataFrame:")
print(projects_df)