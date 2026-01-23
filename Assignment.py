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

print("\nSustainability Assessment:")
print("\nCities with Sustainable Carbon Footprint:")
for data in climate_data:
    if data["carbon_footprint"] < 400:
        assessment = "Sustainable"
    else:
        assessment = "Not Sustainable"
    print(f"{data['city']}: {assessment}")
for data in climate_data:
    if data["carbon_footprint"] < 400:
        print(data["city"])


# print("\nAdd new city data:")
# new_city = {"city": "City F", "temperature": 20, "carbon_footprint": 300}
# climate_data.append(new_city)
# print(f"Updated Climate Data: {climate_data}")

print("\ncity with highest Carbon Footprint Value:")
highest_carbon_city = max(climate_data, key=lambda x: x["carbon_footprint"])
print(f"{highest_carbon_city['city']} with {highest_carbon_city['carbon_footprint']} kg CO2")
print("\ncity with lowest Carbon Footprint Value:")
lowest_carbon_city = min(climate_data, key=lambda x: x["carbon_footprint"])
print(f"{lowest_carbon_city['city']} with {lowest_carbon_city['carbon_footprint']} kg CO2")



print("\nFunction to calculate total carbon footprint:")
def total_carbon_footprint(data):
    return sum(city["carbon_footprint"] for city in data)
total_footprint = total_carbon_footprint(climate_data)
print(f"Total Carbon Footprint of all cities: {total_footprint} kg CO2")

print("\nFunction to Calculate Average Carbon Footprint:")
def average_carbon_footprint(data):
    if not data:
        return 0
    total = sum(city["carbon_footprint"] for city in data)
    return total / len(data)
average_footprint = average_carbon_footprint(climate_data)
print(f"Average Carbon Footprint of all cities: {average_footprint:.2f} kg CO2")



def calculate_carbone_footprint(energy_consumption, total_waste, emmision_factors):
    carbon_footprint = (energy_consumption * emmision_factors.get("energy", 0) +
                        total_waste * emmision_factors.get("waste", 0))
    return carbon_footprint

print("Sustainability threshold, fro example,  400 tons CO2 per month :")
sustainability_threshold = 400
def is_sustainable(carbon_footprint, threshold):
    return carbon_footprint < threshold
emmision_factors = {"energy": 0.5, "waste": 0.3}  # Example factors
energy_consumption = 600  # Example energy consumption in kWh
print("\nCalculating carbon footprint for given energy consumption and waste:")
total_waste = 150  # Example waste in kg
