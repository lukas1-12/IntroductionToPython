class fleet:
    def __init__(self, name, weight, face, velocity, c_w_value, roll_resistance, slope, a_drag_coefficient):
        self.name = name
        self.weight = weight
        self.face = face
        self.velocity = velocity
        self.c_w_value = c_w_value
        self.roll_resistance = roll_resistance
        self.slope = slope
        self.a_drag_coefficient = a_drag_coefficient

    def power_consumption(self):
        roll_force = self.weight * self.roll_resistance * 9.81
        air_force = self.c_w_value * self.face * 1.204 * ((self.velocity / 3.6) ** 2) * 0.5
        slope_force = self.weight * 9.81 * self.slope
        total_force = roll_force + air_force + slope_force

        power_consumption = total_force * (self.velocity / 3.6) / 1000
        return power_consumption
    
    def is_efficient(self):
        if self.power_consumption() > 10:
            return False
            
        elif self.power_consumption() < 10:
            return True

    def __str__(self):
        return f"Power Consumption for {self.name}: {round(self.power_consumption(), 2)} kW"
    
    

Polo = fleet('VW Polo', 1500, 1.8, 90, 0.31, 0.015, 0, 0.31)
Lambo = fleet('Lamborghini Urus', 2200, 1.3, 180, 0.2, 0.011, 0, 0.21)
Taycan = fleet('Porsche Taycan', 2300, 1.96, 250, 0.22, 0.012, 0, 0.25)
Corsa = fleet('Opel Corsa', 1200, 1.5, 100, 0.29, 0.014, -0.025, 0.28)

my_fleet_list = {Polo, Lambo, Taycan, Corsa}

for car in my_fleet_list:
    fleet.power_consumption(car)
    print(f"Power Consumption for {car.name}: {round(fleet.power_consumption(car), 2)} kW")
    fleet.is_efficient(car)
    if fleet.is_efficient(car) == False:
        print(f"{car.name} is not efficient")
    elif fleet.is_efficient(car) == True:
        print(f"{car.name} is efficient")