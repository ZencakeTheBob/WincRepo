__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'Assignment: Strings'

scorer_1 = 'Ruud Gullit'
goal_0 = 32
scorer_2 = 'Marco van Basten'
goal_1 = 54
nd = "nd minute"
th = "th minute"
scored = "scored in the"
scorers = scorer_1 + " " + str(goal_0) + ", " + scorer_2 + " " + str(goal_1)
report = f"{scorer_1} {scored} {str(goal_0)}{nd}\n{scorer_2} {scored} {str(goal_1)}{th}"

player = 'Ruud Gullit'
first_name = player[:player.find(" ")]
length_name = len(player)
last_name = player[player.find(" ") +1:]
last_name_len = len(last_name)

name_short = player[0] + ". " + last_name

chant = (first_name+"! ") * int(len(first_name)-1) + (first_name + "!")
good_chant = chant[-1] != " "

print(scorers)
print(report)
print(first_name)
print(name_short)
print(chant)
print(good_chant)
print(last_name)
print(last_name_len)