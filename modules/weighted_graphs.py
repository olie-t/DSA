class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_adjacent_vertex(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(start_city: City, final_destination: City) -> list:
    cheapest_prices_table = {start_city.name: 0}
    cheapest_previous_stopover_table = {}

    unvisited_cities = [start_city.name]  # Initialize with the start city

    visited_cities = {}

    while unvisited_cities:
        # Find the city in unvisited_cities with the lowest tentative distance
        current_city_name = min(
            unvisited_cities,
            key=lambda city: cheapest_prices_table.get(city, float("inf")),
        )
        current_city = next(
            (
                c
                for c in [start_city, birmingham, falmouth, truro]
                if c.name == current_city_name
            ),
            None,
        )

        if (
            current_city is None
        ):  # Break if no current city is found (should not happen in correct usage)
            break

        visited_cities[current_city.name] = True
        unvisited_cities.remove(current_city.name)

        for city, price in current_city.routes.items():
            if city.name not in visited_cities:
                if city.name not in unvisited_cities:
                    unvisited_cities.append(city.name)
                price_through_current_city = (
                    cheapest_prices_table[current_city.name] + price
                )
                if (
                    city.name not in cheapest_prices_table
                    or price_through_current_city < cheapest_prices_table[city.name]
                ):
                    cheapest_prices_table[city.name] = price_through_current_city
                    cheapest_previous_stopover_table[city.name] = current_city.name

        # Break the loop if there are no unvisited cities left
        if not unvisited_cities:
            break

        # Prevent the loop from trying to select a new current city if unvisited_cities is empty
        current_city = (
            None
            if not unvisited_cities
            else min(
                unvisited_cities,
                key=lambda city: cheapest_prices_table.get(city, float("inf")),
            )
        )

    # Reconstruct the shortest path from the cheapest_previous_stopover_table
    shortest_path = []
    current_city_name = final_destination.name

    while current_city_name != start_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_table.get(current_city_name)
        if current_city_name is None:  # If a path doesn't exist
            return []

    shortest_path.append(start_city.name)
    shortest_path.reverse()

    return shortest_path


if __name__ == "__main__":
    london = City("London")
    birmingham = City("Birmingham")
    falmouth = City("Falmouth")
    truro = City("Truro")

    london.add_adjacent_vertex(birmingham, 120)
    london.add_adjacent_vertex(falmouth, 200)
    birmingham.add_adjacent_vertex(london, 80)
    birmingham.add_adjacent_vertex(falmouth, 15)
    falmouth.add_adjacent_vertex(london, 210)
    falmouth.add_adjacent_vertex(birmingham, 12)
    falmouth.add_adjacent_vertex(truro, 10)
    birmingham.add_adjacent_vertex(truro, 100)
    london.add_adjacent_vertex(truro, 550)
    truro.add_adjacent_vertex(falmouth, 15)
    truro.add_adjacent_vertex(birmingham, 25)
    truro.add_adjacent_vertex(london, 500)
    path = dijkstra_shortest_path(london, truro)
    print(" -> ".join(path))
