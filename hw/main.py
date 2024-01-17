from wine import Wine
from beer import Beer
from market import Market

wines = [
    Wine("Billecart-Salmon, Brut Reserve", "01.01.2024"),
    Wine("Millstream Collection White", "01.01.2023"),
    Wine("Bollinger, Special Cuvee Brut", "01.01.2022"),
]

beers = [
    Beer("Winter Planet: Cherry & Vanilla - Sabotage", "16.01.2024"),
    Beer("To Infinity And Beyond - Sabotage", "01.01.2024"),
    Beer("The Raptor - Sabotage", "23.12.2023"),
    Beer("From Heaven to Hell - Sabotage", "02.05.2007"),
    Beer("Route 666 - Sabotage", "06.06.1666"),
    Beer("Tommates - Sabotage", "01.01.2024"),
]

market = Market(wines, beers)
# market = Market([], [])

print(market.has_drink_with_title("Route 666 - Sabotage")) # True
print(market.has_drink_with_title("Millstream Collection White")) # True
print(market.has_drink_with_title("test")) # False

print("-----")

sorted_drinks = market.get_drinks_sorted_by_title()
for i, drink in enumerate(sorted_drinks):
    print(f"{i + 1}. {drink.title} ({drink.production_date})") # Drink

print("-----")

drinks_by_date = market.get_drinks_by_production_date("01.12.2023", "17.01.2024")
for i, drink in enumerate(drinks_by_date):
    print(f"{i + 1}. {drink.title} ({drink.production_date})") # Drink
