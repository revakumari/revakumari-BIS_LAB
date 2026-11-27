#Parallel Cellular

import random
import math

# Fitness function
def fitness(x, y, rooms, radius):
    covered = 0
    for rx, ry in rooms:
        distance = math.sqrt((x-rx)**2 + (y-ry)**2)
        if distance <= radius:
            covered += 1
    return covered

# User input
width = int(input("Enter building width: "))
height = int(input("Enter building height: "))

n = int(input("Enter number of rooms: "))
rooms = []

for i in range(n):
    x = int(input(f"Enter x coordinate of room {i+1}: "))
    y = int(input(f"Enter y coordinate of room {i+1}: "))
    rooms.append((x, y))

radius = float(input("Enter router coverage radius: "))
cells = int(input("Enter number of cells: "))
iterations = int(input("Enter number of iterations: "))

# Initialize cells randomly
population = [
    [random.uniform(0, width), random.uniform(0, height)]
    for _ in range(cells)
]

best_position = None
best_fitness = -1

# Parallel Cellular Algorithm
for step in range(iterations):

    new_population = []

    for i in range(cells):

        # Find neighboring cells
        neighbors = [
            population[i],
            population[(i-1) % cells],
            population[(i+1) % cells]
        ]

        # Select the best neighboring position
        best_neighbor = max(
            neighbors,
            key=lambda p: fitness(p[0], p[1], rooms, radius)
        )

        # Random mutation for exploration
        x = best_neighbor[0] + random.uniform(-2, 2)
        y = best_neighbor[1] + random.uniform(-2, 2)

        # Keep position within building
        x = max(0, min(width, x))
        y = max(0, min(height, y))

        new_population.append([x, y])

    # Update all cells simultaneously
    population = new_population

    # Find best solution
    for cell in population:
        score = fitness(cell[0], cell[1], rooms, radius)

        if score > best_fitness:
            best_fitness = score
            best_position = cell.copy()

# Display result
print("\nOptimal Router Placement:")
print("X Coordinate:", round(best_position[0], 2))
print("Y Coordinate:", round(best_position[1], 2))
print("Rooms Covered:", best_fitness, "/", n)
print("Coverage Percentage:", round(best_fitness/n*100, 2), "%")
