# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
vegetables = [broccoli, leek, potato, brussel_sprout]
price_vegetables = [2, 2, 3, 7]
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10
desired_num_veg = [num_potatoes * 3, num_leeks * 2, num_broccolis * 2, num_brussel_sprouts * 7]
discount_percentage = 30
# hierboven staan alle variabelen gedeclareerd waarin de groenten en de prijzen ervan zijn verklaart

def sum_of_one_each():
    Sum_one_each = sum(vegetables)
    return Sum_one_each

def average_price():
    total_price = sum(price_vegetables)
    count = len(price_vegetables)
    avg_price = total_price / count
    return avg_price

def sum_of_total(a):
    return sum(a)
# deze functie is goed herbruikbaar doordat er een loze variabele in wordt gebruikt


def discounted_of_sum_total():
    discounted_price = discount_percentage / 100 * sum_of_total()
    total_price = sum_of_total() - discounted_price
    total_price = round(total_price, 2)
    return total_price

sum_one_each = sum_of_one_each()#ik denk eigenlijk dat deze overbodig is
avg_price = average_price()#ik denk eigenlijk dat deze overbodig is
sum_total = sum_of_total(desired_num_veg)
"""In deze functie wordt de herbruikbare functie gebruikt
en word de lozevariabele (a) vervangen door (desired_num_veg)"""
discounted_sum_total = discounted_of_sum_total()
"""de variabelen hierboven bestaan omdat de vorige opdracht variabelen nodig had.
Maar is ook goed mogelijk dat ik dat verkeerd heb begrepen."""

print(discounted_sum_total) # dit is het enige wat geprint hoefde te worden