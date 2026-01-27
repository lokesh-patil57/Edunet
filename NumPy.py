import numpy as np
#Energy Consumption in MWh for different renewable  sources : solar , wind , hydro

ec=[1200,3400,2900,1800,2500]
energy_comnsumption=np.array(ec)

#printing the array
print("Energy Consumption (MWh) for different Renewable Sources:", energy_comnsumption)

A = np.ones(4)
A2 = np.ones((2, 2))
print(A)
print("\n", A2)


M = np.identity(4)
print("\nIdentity Matrix (4x4):\n", M)

#calculate the total energy consumption
total_consumption = np.sum(energy_comnsumption)

print(f"Total Energy Consumption (MWh): {total_consumption} MWh")


#calculate the mean average energy consumption
mean_consumption = np.mean(energy_comnsumption)
print(f"Mean Average Energy Consumption (MWh): {mean_consumption} MWh")

#calculate standard deviation of energy consumption
std_deviation = np.std(energy_comnsumption)
print(f"Standard Deviation of Energy Consumption (MWh): {std_deviation} MWh")

#reshape the array (to 5 rows and 1 column)
energy_comnsumption2= np.array([1200,3400,2900,1800,2500,1800])
reshaped_array = energy_comnsumption2.reshape(3, 2)
print("\nReshaped Energy Consumption Array (3x2):\n", reshaped_array)

#flatten the array
flattened_array = reshaped_array.flatten()
print("\nFlattened Energy Consumption Array:\n", flattened_array)

#Resizing the array 
resized_array = np.resize(energy_comnsumption, (3, 3))
print("\nResized Energy Consumption Array (3x3):\n", resized_array)
