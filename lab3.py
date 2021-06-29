Soccer_players = {"Messi": 7, "Ronaldo": 9, "Virgil van Dijk": 4, "Neymar": 11}
cities = ["Oakland", "Atlanta", "New York City","Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
Soccer_teams = ["PSG", "Spurs", "Aresenal", "Man City", "Man United", "Chealse", "Liverpool", "Juventus", "Real Madrid", "FC Barcelona"]

Ronaldo_position = Soccer_players["Ronaldo"] 

Ronaldo_position = Soccer_players["Ronaldo"] + 2

print(Ronaldo_position)

list1 = cities[0:3]

list2 = Soccer_teams[0:3]

Combined_list = list1 + list2

print(Combined_list)

cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"

print(cities)

cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")

print(cities)