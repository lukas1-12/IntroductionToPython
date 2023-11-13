my_fleet = ()

Polo = {'name': 'VW Polo', 
         'weight': 1500, 
         'face': 1.8, 
         'velocity': 90, 
         'c_w-value' : 0.31, 
         'roll-resistance' : 0.015,
         'slope' : 0,
         'a drag coefficient' : 0.31}

my_fleet += (Polo,)



Lambo = {'name': 'Lamborghini Urus', 
         'weight': 2200, 
         'face': 1.3, 
         'velocity': 180, 
         'c_w-value' : 0.2, 
         'roll-resistance' : 0.011,
         'slope' : 0,
         'a drag coefficient' : 0.21}

my_fleet += (Lambo,)

Taycan = {'name': 'Porsche Taycan', 
         'weight': 2300, 
         'face': 1.96, 
         'velocity': 250, 
         'c_w-value' : 0.22, 
         'roll-resistance' : 0.012,
         'slope' : 0,
         'a drag coefficient' : 0.25}

my_fleet += (Taycan,)

Corsa = {'name': 'Opel Corsa', 
    'weight': 1200, 
    'face': 1.5, 
    'velocity': 100, 
    'c_w-value' : 0.29, 
    'roll-resistance' : 0.014,
    'slope' : -0.025,
    'a drag coefficient' : 0.28}

my_fleet += (Corsa,)

for vehicle in my_fleet:
    RollForce = vehicle['weight'] * vehicle['roll-resistance'] * 9.81
    AirForce = vehicle['c_w-value'] * vehicle['face'] * 1.204 * (vehicle['velocity']/3.6)**2 * 0.5
    SlopeForce = vehicle['weight'] * 9.81 * vehicle['slope']
    TotalForce = RollForce + AirForce + SlopeForce

    PowerConsumption = TotalForce * (vehicle['velocity']/3.6) / 1000

    print(f"Power Consumption for {vehicle['name']}: {round(PowerConsumption, 2)} kW")
    if PowerConsumption > 10:
        print(f"{vehicle['name']} is not efficient")
    elif PowerConsumption < 10:
        print(f"{vehicle['name']} is efficient")