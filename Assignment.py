climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450},
]


print("Cities with temperature above 26 degrees Celsius:")
for data in climate_data:
    if data["temperature"] > 26:
        print(data["city"])


print("\nAverage of Temperatures:")
total_temp = sum(data["temperature"] for data in climate_data)
average_temp = total_temp / len(climate_data)
print(f"Average Temperature: {average_temp:.2f} °C")

print("\n Average Carbon Footprint:")
total_carbon = sum(data["carbon_footprint"] for data in climate_data)
average_carbon = total_carbon / len(climate_data)
print(f"Average Carbon Footprint: {average_carbon:.2f} kg CO2")