#user 1
# 5 days keep constant (+-10)
# 2 days keep constant (+-12)
# preference shifts w/season
# Spring

# 10 days of avg. temp
# 10 days of max. temp 
# 10 days of min. temp

#5 days constant for each 10-day period 
#2 days constant for each 10-day period 
# 5 days 
# 2 2 days
# = 20 +- 10 
# - 10 +- 12
#import random 

#def daily_kwh_consum(): 
#    outside_temp = rand.range(54,71)
#    set_temp = random.choice[70,75,80]
#    hours = 24
#    cooling_wattage = 1500
#    heating_wattage = 3500
#    if outside_temp = set_temp: 
#        for i in range(set_temp): 
#            i++
#    elif outside_temp > set_temp: 
#        for i in range(set_temp):
#            i--
#    elif outside_temp < set_temp: 
#        for i in range(set_temp):
#            i++
#    
#    return ((wattage * hours)/1000)

#def annual_energy_consum(daily_kwh_consum, days):
#    return daily_kwh_consum * days 

#def annual_cost(annual_energy_consum): 
#    cost_kWH = 18.7
#    return annual_energy_consum * cost_kWH

import random 

hours = 24
wattage = 2500

def wattage_adjustment():
    set_temp = 75
    outside_temp = random.randrange(54,72)
    difference = abs(outside_temp - set_temp)
    adj_wattage = difference * 1.03 * wattage
    return adj_wattage
    
def daily_kwh_consum(adj_wattage):
    if adj_wattage >= wattage: 
        daily_consumption = (adj_wattage * hours)/1000
    else: 
        daily_consumption = (wattage * hours)/1000
    return daily_consumption 

def annual_energy_consum(daily_consumption): 
    annual_consum = daily_consumption * 365
    return annual_consum

def annual_cost (annual_consum):
    centskwh = 18.7
    total_cost = centskwh * 

thermostat_wattage = wattage_adjustment()
user_kwh_consum = daily_kwh_consum(thermostat_wattage)
annual_usage = annual_energy_consum(user_kwh_consum)

print(thermostat_wattage, user_kwh_consum, annual_usage)
