# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
sentence_leek = "Leek is " + str(leek_price) + " euro per kilo."
print(sentence_leek)

order_leek = "leek 4"
amount_leek = int(order_leek[order_leek.find(" ")+1 :])
sum_total = leek_price * amount_leek
print(sum_total)

broccoli_price = 2.34
broccoli_order = 1.6
sum_total_broccoli = round(broccoli_price * broccoli_order,2)
print(str(broccoli_order) + "kg broccoli costs " + str(sum_total_broccoli) + "e")