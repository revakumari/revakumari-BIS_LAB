#Ant Colony
import random

# User input
n = int(input("Enter number of customer locations: "))
locations = ["Restaurant"]

for i in range(1, n + 1):
    locations.append("C" + str(i))

print("\nEnter distance matrix:")

distances = []
for i in range(n + 1):
    row = list(map(int, input().split()))
    distances.append(row)

ants = int(input("\nEnter number of ants: "))
iterations = int(input("Enter number of iterations: "))

alpha = 1
beta = 2
evaporation = 0.5
Q = 100

# Initialize pheromone
pheromone = [[1 for j in range(n + 1)]
             for i in range(n + 1)]


# Calculate route distance
def route_distance(route):
    total = 0

    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]

    total += distances[route[-1]][route[0]]

    return total


# Select next location
def select_next(current, unvisited):
    probabilities = []

    for city in unvisited:
        p = pheromone[current][city] ** alpha
        h = (1 / distances[current][city]) ** beta
        probabilities.append(p * h)

    return random.choices(unvisited, weights=probabilities)[0]


# Ant Colony Optimization
def ACO():
    best_route = None
    best_distance = float('inf')

    for iteration in range(iterations):

        all_routes = []

        for ant in range(ants):
            route = [0]
            unvisited = list(range(1, n + 1))

            while unvisited:
                current = route[-1]
                next_city = select_next(current, unvisited)

                route.append(next_city)
                unvisited.remove(next_city)

            distance = route_distance(route)
            all_routes.append((route, distance))

            if distance < best_distance:
                best_distance = distance
                best_route = route.copy()

        # Pheromone evaporation
        for i in range(n + 1):
            for j in range(n + 1):
                pheromone[i][j] *= (1 - evaporation)

        # Pheromone update
        for route, distance in all_routes:
            deposit = Q / distance

            for i in range(len(route) - 1):
                a = route[i]
                b = route[i + 1]

                pheromone[a][b] += deposit
                pheromone[b][a] += deposit

            a = route[-1]
            b = route[0]

            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

    # Display result
    route_names = [locations[i] for i in best_route]
    route_names.append("Restaurant")

    print("\n====== OPTIMAL DELIVERY ROUTE ======")
    print("Delivery Route:", " -> ".join(route_names))
    print("Total Distance:", best_distance, "km")
    print("Customers Visited:", n)
    print("Number of Ants:", ants)
    print("Iterations:", iterations)
    print("====================================")


ACO()
