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

analyze_energy_consumption(buildings_data)