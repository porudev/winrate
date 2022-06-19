from http.client import NOT_EXTENDED
import math

total_match = input("Total Match: ").replace('%', '')
current_winrate = input("Current winrate: ").replace('%', '')
wanted_winrate = input("Wanted Winrate: ").replace('%', '')

total_match = float(total_match)
current_winrate = float(current_winrate)
wanted_winrate = float(wanted_winrate)

current_win = (total_match*current_winrate)/100
needed_match = ((100*current_win) - (wanted_winrate*total_match))/(wanted_winrate-100)

print(math.ceil(needed_match))

print(total_match)
print(current_winrate)
print(wanted_winrate)