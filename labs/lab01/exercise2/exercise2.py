# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants,tent_capacity,tent_price):
    if participants % tent_capacity == 0:
        total_cost = tent_price * (participants / tent_capacity)
    else:
        total_cost = tent_price * math.ceil(participants / tent_capacity)
    return total_cost

total_cost1 = calculate_tent_cost(12,4,100)
print(total_cost1)

total_cost2 = calculate_tent_cost(13,4,100)
print(total_cost2)