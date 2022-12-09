__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'Assignment: Strings'

goal_scorer_g = 'Ruud Gullit'
goal_0 = 32
goal_scorer_m = 'Marco van Basten'
goal_1 = 54
last_name_m = 'van Basten'
goal_string_g = goal_scorer_g + " scored in the " + str(goal_0) + "nd minute"
goal_string_m = goal_scorer_m + " scored in the " + str(goal_1) + "th minute"
scorers = goal_scorer_g + str(goal_0) + goal_scorer_m + str(goal_1)
report = goal_string_g + " and " + goal_string_m

player = 'Ruud Gullit'
first_name_g_stops_at = slice(goal_scorer_g.find(" Gullit"))
first_name = goal_scorer_g[first_name_g_stops_at]
length_name_g = len(goal_scorer_g)
last_name_len = slice(goal_scorer_g.find("Gullit"),length_name_g)
first_letter = goal_scorer_g[0]
name_short = first_letter + ". " + goal_scorer_g[last_name_len]

first_name_length = len(first_name)
chant = (" "+first_name+"!") * int(first_name_length)

length_chant = len(chant)
a = slice(length_chant)
last_character_chant = chant[a]
good_chant = last_character_chant != " "


print(last_character_chant)
print(good_chant)
print(scorers)
print(report)
print(first_letter)
print(first_name)
print(name_short)
print(chant)