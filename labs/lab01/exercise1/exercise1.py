# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km,budget):
    fuel = budget / 2
    distance = fuel * 10
    if distance >= (one_way_km * 2):
        return True
    else:
        return False

round_trip1 = is_budget_sufficient(100,40)
print(round_trip1)

round_trip2 = is_budget_sufficient(100,39)
print(round_trip2)