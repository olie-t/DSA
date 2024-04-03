class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_adjacent_vertex(self, city, price):
        self.routes[city] = price


def dijkstra_shortest_path(start_city: City, final_destination: City) -> list:
    # Initialize the cheapest prices table with the start city at a cost of 0.
    cheapest_prices_table = {start_city: 0}
    # Initialize a table to keep track of the cheapest path's previous city.
    cheapest_previous_stopover_table = {}
    # All cities initially unvisited; start with just the start city known.
    unvisited_cities = {start_city}
    # Keep track of visited cities to avoid revisiting.
    visited_cities = set()

    # The current city starts as the start city.
    current_city = start_city

    while current_city:
        # Mark the current city as visited.
        visited_cities.add(current_city)
        unvisited_cities.remove(current_city)

        # Update distances to each adjacent city.
        for adjacent_city, price in current_city.routes.items():
            if adjacent_city not in visited_cities:
                unvisited_cities.add(adjacent_city)
                new_price = cheapest_prices_table[current_city] + price
                if (
                    adjacent_city not in cheapest_prices_table
                    or new_price < cheapest_prices_table[adjacent_city]
                ):
                    cheapest_prices_table[adjacent_city] = new_price
                    cheapest_previous_stopover_table[adjacent_city] = current_city

        # Select the next city: the unvisited city with the lowest tentative distance.
        current_city = None
        lowest_price = float("inf")
        for city in unvisited_cities:
            if cheapest_prices_table[city] < lowest_price:
                lowest_price = cheapest_prices_table[city]
                current_city = city

        # Break the loop if no unvisited cities are left or if the final destination is reached.
        if current_city == final_destination or not current_city:
            break

    # Reconstruct and return the shortest path using the previous stopover table.
    shortest_path = []
    while final_destination:
        shortest_path.append(final_destination.name)
        final_destination = cheapest_previous_stopover_table.get(final_destination)

    return shortest_path[::-1]  # Return the reversed path, from start to destination.


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
