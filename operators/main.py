# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_language = "Castilian Spanish" 
switzerland_language = "German"
print(spain_language == switzerland_language)

spain_religion = "Roman Catholic" 
switzerland_religion = "Roman Catholic"
print(spain_religion == switzerland_religion)

spain_capital_length = 6
switzerland_capital_length = 4
print(spain_capital_length != switzerland_capital_length)

spain_GDP = 1393351000000 
switzerland_GDP = 731502000000
print(switzerland_GDP > spain_GDP)

spain_pop_growth = 0.13
switzerland_pop_growth = 0.65
print(spain_pop_growth < 1.0 and switzerland_pop_growth < 1.0)

pop_count = 10000000
spain_pop = 47163418
switzerland_pop = 8508698
print(spain_pop > pop_count or switzerland_pop > pop_count)
print(not(spain_pop > pop_count and switzerland_pop > pop_count))