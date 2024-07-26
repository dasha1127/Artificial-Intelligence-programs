import numpy as np

def nearest_neighbor(dist_matrix):
    n = len(dist_matrix)
    unvisited = set(range(n))
    tour = [0]
    total_distance = 0
    current_city = 0

    while len(unvisited) > 1:
        unvisited.remove(current_city)
        nearest_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(nearest_city)
        total_distance += dist_matrix[current_city][nearest_city]
        current_city = nearest_city

    total_distance += dist_matrix[current_city][tour[0]]
    tour.append(tour[0])
    
    return tour, total_distance

def main():
    dist_matrix = np.array([
        [0, 2, 9, 10, 7],
        [1, 0, 6, 4, 3],
        [15, 7, 0, 8, 9],
        [6, 3, 12, 0, 5],
        [10, 8, 6, 9, 0]
    ])
    tour, distance = nearest_neighbor(dist_matrix)
    print(f"Tour: {' -> '.join(map(str, tour))}")
    print(f"Total distance: {distance}")

if __name__ == "__main__":
    main()
