# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, timeOfDay, cowMilkingStatus, locationOfTheCows, season, slurryTank, grassStatus):
    if weather == "rainy" and locationOfTheCows == "pasture":
        return "take cows to cowshed"
    elif weather == "sunny" and timeOfDay == "day" and cowMilkingStatus and locationOfTheCows == "pasture" and season == "spring" and grassStatus:
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
    elif locationOfTheCows == "pasture" and timeOfDay == "night":
        return "take cows to cowshed"
    elif cowMilkingStatus and locationOfTheCows == "cowshed":
        return "milk cows"
    elif locationOfTheCows == "cowshed" and slurryTank and not( weather == "sunny" or weather == "windy"):
        return "fertilize pasture"
    elif grassStatus and season == "spring" and weather == "sunny" and "pasture" not in locationOfTheCows:
        return "mow grass"
    else: 
        return "wait"

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))