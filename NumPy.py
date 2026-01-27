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