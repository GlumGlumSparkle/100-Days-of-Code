# Default data

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# Input Data
start_again = False
while not start_again:
    country = input("Please input country you've been to:\n")
    visits = input("Please input amount of visits:\n")
    cities = input("Please input cities:\n")
    new_country = {"country":"","visits":"","cities":""}

# Function to add new country
    def add_new_country(added_country,names_cities,number_of_visits):
        new_country["country"] = added_country
        new_country["visits"] = number_of_visits
        new_country["cities"] = names_cities
        travel_log.append(new_country)
    add_new_country(added_country=country,number_of_visits=visits,names_cities=cities)

# Travel log print
    print(travel_log)

# Start again question
    start_again = input("Would you like to start again? Type yes or no:\n").lower()
    if start_again == "yes":
        start_again = False
    else:
        print("Goodbye!")



