# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type,hour):
    if vehicle_type == "Electric":
        charge = 2.0
    elif vehicle_type == "Hybrid":
        if hour <= 6 or hour >= 22:
            charge = 2.0
        else:
            charge = 5.0
    else:
        charge = 5.0
    return charge

charge1 = get_hourly_rate("Hybrid",23)
print(charge1)

charge2 = get_hourly_rate("Hybrid",13)
print(charge2)

charge3 = get_hourly_rate("Sedan",2)
print(charge3)