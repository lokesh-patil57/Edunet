#__init__() is used to build or set up your object when you create it
class EnergySystem:
    def __init__(self, building_name, energy_consumption, emission_factor):
        # Initialize attributes
        self.building_name = building_name
        self.energy_consumption = energy_consumption # in kWh
        self.emission_factor = emission_factor # in kg CO2 per kWh

    def calculate_carbon_footprint(self):
        return self.energy_consumption * self.emission_factor

    def display_info(self):
        print(f"Building Name: {self.building_name}")
        print(f"Energy Consumption: {self.energy_consumption} kWh")
        print(f"Emission Factor: {self.emission_factor} kg CO2 per kWh")

#method to calculate energy saving(Assume saving 10% for now)
    def calculate_energy_saving(self):
        return self.energy_consumption * 0.10

# Example usage
building = EnergySystem("Building A", 5000, 0.45)
building.display_info()
footprint = building.calculate_carbon_footprint()
energysaving = building.calculate_energy_saving()
print(f"Carbon Footprint: {footprint} kg CO2")
print(f"Energy Saving: {energysaving} kWh")


#subclass for SolarEnergySystem inheriting from EnergySystem
class SolarEnergySystem(EnergySystem):
    def __init__(self, building_name, energy_consumption, emission_factor, solar_capacity):
        # Call the constructor of the parent class
        super().__init__(building_name, energy_consumption, emission_factor)
        self.solar_capacity = solar_capacity # in kW

    #method to calculate net energy consumption after solar contribution
    def calculate_net_energy_consumption(self):
        solar_contribution = self.calculate_solar_contribution()
        return self.energy_consumption - solar_contribution

    def calculate_solar_contribution(self):
        # Assume solar contribution is 20% of energy consumption for simplicity
        return self.energy_consumption * 0.20

    def display_info(self):
        super().display_info()
        print(f"Solar Capacity: {self.solar_capacity} kW")

#Example useage of subclass
solar_building = SolarEnergySystem("Solar Building ", 5000, 0.45, 1500)
solar_building.display_info()
net_consumption = solar_building.calculate_net_energy_consumption()
solar_contribution = solar_building.calculate_solar_contribution()
print(f"Solar Contribution: {solar_contribution} kWh")
print(f"Net Energy Consumption: {net_consumption} kWh")
