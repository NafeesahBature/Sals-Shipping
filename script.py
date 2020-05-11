premium_ground_shipping = 125.0
def cost_of_ground_shipping(weight):
  if weight <= 2:
    return  20 + weight * 1.50 
  elif weight <= 6:
    return   20 + weight * 3.00 
  elif weight <= 10:
    return   20 + weight * 4.00 
  elif weight > 10:
    return   20 + weight * 4.75 

print(cost_of_ground_shipping(8.4))

def cost_of_drone_shipping(weight):
  if weight <= 2:
    return 0 + weight * 4.50 
  elif weight <= 6:
    return 0 + weight * 9.00 
  elif weight <= 10:
    return 0 + weight * 12.00 
  elif weight > 10:
    return 0 + weight * 14.25 
print(cost_of_drone_shipping(1.5))

def cheapest_method(weight):
  drone = cost_of_drone_shipping(weight)
  premium = premium_ground_shipping
  ground = cost_of_ground_shipping(weight)
  if drone < premium and drone < ground:
    return "Drone is the cheapest!.. $" + str(drone)
  elif ground < premium and ground < drone:
    return "premium is the cheapest!.. $" + str(ground)
  else:
    return "premium it is.... $" + str(premium)
print(cheapest_method(round(41.8)))

