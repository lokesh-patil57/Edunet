# Smart Energy Consumption Analyzer
def analyze_energy_consumption(buildings_data, critical_limit=10000):
    
    total_consumption = 0.0
    building_reports = []
    
    for building in buildings_data:
        name = building['name']
        consumption = building['consumption']  # List of hourly consumption in kWh
        
        # Compute total and average for this building
        building_total = sum(consumption)
        building_avg = building_total / len(consumption) if consumption else 0
        
        # Add to overall total
        total_consumption += building_total
        
        # Check critical limit
        if total_consumption > critical_limit:
            print(f"Critical grid limit of {critical_limit} kWh exceeded! Stopping analysis.")
            break
        
        # Classify building based on average consumption
        if building_avg < 50:
            category = "Energy Efficient"
        elif building_avg < 100:
            category = "Moderate Consumption"
        else:
            category = "Energy Intensive"
        
        building_reports.append({
            'name': name,
            'total': building_total,
            'average': building_avg,
            'category': category
        })
    
    # Print sustainability report
    print("\nSustainability Report:")
    print("=" * 50)
    for report in building_reports:
        print(f"Building: {report['name']}")
        print(f"  Total Consumption: {report['total']} kWh")
        print(f"  Average Consumption: {report['average']:.2f} kWh")
        print(f"  Category: {report['category']}")
        print("-" * 30)
    
    print(f"Overall Total Consumption: {total_consumption} kWh")
    print(f"Number of Buildings Analyzed: {len(building_reports)}")

# Example usage for Smart Energy Consumption Analyzer
print("\nSmart Energy Consumption Analyzer:")
buildings_data = [
    {'name': 'Library', 'consumption': [45, 50, 40, 55, 48, 42, 38, 52, 46, 49, 44, 51, 47, 43, 50, 41, 53, 39, 48, 45, 42, 46, 44, 49]},
    {'name': 'Lecture Hall', 'consumption': [80, 85, 75, 90, 82, 78, 70, 88, 76, 83, 79, 87, 81, 77, 84, 73, 89, 74, 82, 80, 78, 81, 79, 85]},
    {'name': 'Dormitory', 'consumption': [120, 125, 115, 130, 118, 112, 105, 128, 116, 123, 119, 127, 121, 117, 124, 113, 129, 114, 122, 120, 118, 121, 119, 125]},
    {'name': 'Cafeteria', 'consumption': [60, 65, 55, 70, 62, 58, 50, 68, 56, 63, 59, 67, 61, 57, 64, 53, 69, 54, 62, 60, 58, 61, 59, 65]}
]

<<<<<<< HEAD
analyze_energy_consumption(buildings_data)


class EnergySource:
    
    def __init__(self, name, max_power):
        self.name = name
        self.__max_power = max_power
    
    @property
    def max_power(self):
        return self.__max_power
    
    def calculate_energy_availability(self):
        return self.__max_power * 0.8
    
    def get_info(self):
        return f"{self.name}: Max Power = {self.__max_power} kW, Available = {self.calculate_energy_availability():.2f} kW"

class Solar(EnergySource):
    
    def __init__(self, name, max_power, sunlight_hours):
        super().__init__(name, max_power)
        self.sunlight_hours = sunlight_hours
    
    def calculate_energy_availability(self):
        return self.max_power * (self.sunlight_hours / 24) * 0.9

class Wind(EnergySource):
    
    def __init__(self, name, max_power, wind_speed):
        super().__init__(name, max_power)
        self.wind_speed = wind_speed
    
    def calculate_energy_availability(self):
        if self.wind_speed > 10:
            return self.max_power * 0.95
        else:
            return self.max_power * 0.5

class Hydro(EnergySource):
    
    def __init__(self, name, max_power, water_flow):
        super().__init__(name, max_power)
        self.water_flow = water_flow
    
    def calculate_energy_availability(self):
        return self.max_power * min(self.water_flow / 100, 1.0)

def prioritize_energy_sources(sources, demand):
    prioritized_sources = sorted(sources, key=lambda s: s.calculate_energy_availability(), reverse=True)
    
    allocation = {}
    remaining_demand = demand
    
    print(f"\nAllocating {demand} kW of energy demand:")
    print("Priority order based on availability:")
    
    for i, source in enumerate(prioritized_sources, 1):
        availability = source.calculate_energy_availability()
        print(f"{i}. {source.name} - Available: {availability:.2f} kW")
    
    print("\nEnergy Allocation:")
    
    for source in prioritized_sources:
        if remaining_demand <= 0:
            allocation[source.name] = 0
            continue
        
        availability = source.calculate_energy_availability()
        allocated = min(availability, remaining_demand)
        allocation[source.name] = allocated
        remaining_demand -= allocated
        
        print(f"  {source.name}: {allocated:.2f} kW allocated")
    
    if remaining_demand > 0:
        print(f"\nWarning: {remaining_demand:.2f} kW demand unmet!")
    
    return allocation

if __name__ == "__main__":
    print("Renewable Energy Decision Engine")
    print("=" * 40)
    
    solar_farm = Solar("Solar Farm A", 1000, 8)
    wind_farm = Wind("Wind Farm B", 800, 12)
    hydro_plant = Hydro("Hydro Plant C", 1200, 80)
    
    sources = [solar_farm, wind_farm, hydro_plant]
    
    print("\nEnergy Sources Information:")
    for source in sources:
        print(f"  {source.get_info()}")
    
    demands = [500, 1500, 2500]
    
    for demand in demands:
        allocation = prioritize_energy_sources(sources, demand)
        total_allocated = sum(allocation.values())
        print(f"\nTotal Allocated: {total_allocated:.2f} kW")
        print("-" * 40)
=======
analyze_energy_consumption(buildings_data)
>>>>>>> cf1fd43c4e63c4b87b2403fb194dfbb06ad5c93b
