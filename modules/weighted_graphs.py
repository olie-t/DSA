class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_adjacent_vertex(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(start_city: City, final_destination: City) -> list:
    cheapest_prices_table = {}
    cheapest_previous_stopover_table = {}

    unvisited_cities = []

    visited_cities = {}

    cheapest_prices_table[start_city.name] = 0

    current_city = start_city

    while current_city:
        visited_cities[current_city.name] = True
        unvisited_cities.remove(current_city)

        for city in current_city.routes:
            if city


if __name__ == "__main__":
    london = City("London")
    birmingham = City("Birmingham")
    falmouth = City("Falmouth")
    truro = City("Truro")

    london.add_adjacent_vertex(birmingham, 120)
    london.add_adjacent_vertex(falmouth, 200)
    birmingham.add_adjacent_vertex(london, 80)
    birmingham.add_adjacent_vertex(falmouth, 90)
    falmouth.add_adjacent_vertex(london, 210)
    falmouth.add_adjacent_vertex(birmingham, 75)
    falmouth.add_adjacent_vertex(truro, 10)
    birmingham.add_adjacent_vertex(truro, 10)
    london.add_adjacent_vertex(truro, 20)
    truro.add_adjacent_vertex(falmouth, 15)
    truro.add_adjacent_vertex(birmingham, 25)
    truro.add_adjacent_vertex(london, 250)
