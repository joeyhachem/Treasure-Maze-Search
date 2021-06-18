import sys
import helper
from functools import cmp_to_key

start = 13, 2
treasure = 5, 23

bfs_path = []
nodes_explored = 0

path_hash_map = {}

# Returns the cost from node passed to start node
def get_cost_from_node_to_start(j: int, i: int):
    # Print path from start to end
    current = (i, j)
    counter = 0

    while current is not None and current[0] != start[0] or current[1] != start[1]:
        current = path_hash_map.get(current)
        if current is None:
            break
        counter += 1

    return counter


# h(n)
def calculate_manhattan_distance(x_coord: int, y_coord: int):
    return abs(x_coord - treasure[1]) + abs(y_coord - (treasure[0]))


# Calculates f(n) = g(n) + h(n), where g(n) is the cost of the path from the current node to start node,
# and h(n) is the manhattan distance formula
def heuristic(first_tuple_coord: list[int], second_tuple_coord: list[int]):
    if (calculate_manhattan_distance(first_tuple_coord[1], first_tuple_coord[0]) +
        get_cost_from_node_to_start(first_tuple_coord[1], first_tuple_coord[0])) \
            < (calculate_manhattan_distance(second_tuple_coord[1], second_tuple_coord[0]) +
               get_cost_from_node_to_start(second_tuple_coord[1], second_tuple_coord[0])):
        return -1
    elif (calculate_manhattan_distance(first_tuple_coord[1], first_tuple_coord[0]) +
          get_cost_from_node_to_start(first_tuple_coord[1], first_tuple_coord[0])) \
            > (calculate_manhattan_distance(second_tuple_coord[1], second_tuple_coord[0]) +
               get_cost_from_node_to_start(second_tuple_coord[1], second_tuple_coord[0])):
        return 1
    else:
        return 0


def bfs(is_a_star_search) -> bool:
    queue = [[start[0], start[1]]]  # Need a fifo structure for bfs -> queue
    global nodes_explored, path_hash_map

    while queue:
        queue_size = len(queue)
        for index in range(queue_size):
            if is_a_star_search and len(queue) > 1:
                # Apply heuristic function here, sort the queue size based on the lowest value of the f(n) = g(n) +
                # h(n). Here, g(n) which is usually the cost from one node to the next, is the same for all
                # directions, cost of 1
                queue.sort(key=cmp_to_key(heuristic))

            tuple_coord: [int, int] = queue.pop(0)  # fifo
            nodes_explored += 1

            # if we're at the treasure location, success!
            if tuple_coord[0] == treasure[0] and tuple_coord[1] == treasure[1]:
                return True

            helper.visited[tuple_coord[0]][tuple_coord[1]] = 1
            helper.draw_maze(start, treasure)

            # go right, check if there is no wall.
            if tuple_coord[1] < len(helper.maze) - 1 and helper.maze[tuple_coord[0]][tuple_coord[1] + 1] == 0:
                if (tuple_coord[0], tuple_coord[1] + 1) not in path_hash_map:
                    queue.append([tuple_coord[0], tuple_coord[1] + 1])
                    path_hash_map[(tuple_coord[0], tuple_coord[1] + 1)] = (tuple_coord[0], tuple_coord[1])  # Keep
                    # track of parent for final path later

            # go up, check if there is no wall.
            if tuple_coord[0] > 0 and helper.maze[tuple_coord[0] - 1][tuple_coord[1]] == 0:
                if (tuple_coord[0] - 1, tuple_coord[1]) not in path_hash_map:
                    queue.append([tuple_coord[0] - 1, tuple_coord[1]])
                    path_hash_map[(tuple_coord[0] - 1, tuple_coord[1])] = (tuple_coord[0], tuple_coord[1])

            # go down, check if there is no wall.
            if tuple_coord[0] < len(helper.maze) - 1 and helper.maze[tuple_coord[0] + 1][tuple_coord[1]] == 0:
                if (tuple_coord[0] + 1, tuple_coord[1]) not in path_hash_map:
                    queue.append([tuple_coord[0] + 1, tuple_coord[1]])
                    path_hash_map[(tuple_coord[0] + 1, tuple_coord[1])] = (tuple_coord[0], tuple_coord[1])

            # go left, check if there is no wall.
            if tuple_coord[1] > 0 and helper.maze[tuple_coord[0]][tuple_coord[1] - 1] == 0:
                if (tuple_coord[0], tuple_coord[1] - 1) not in path_hash_map:
                    queue.append([tuple_coord[0], tuple_coord[1] - 1])
                    path_hash_map[(tuple_coord[0], tuple_coord[1] - 1)] = (tuple_coord[0], tuple_coord[1])

    return False


def main():
    global start, treasure
    gif_file_name = "bfs-maze.gif"
    is_a_star_search = False

    # Setup start and treasure positions based on run parameters
    if sys.argv[1] is not None:
        start = int(sys.argv[1]), int(sys.argv[2])
        treasure = int(sys.argv[3]), int(sys.argv[4])

    if len(sys.argv) > 5 and sys.argv[5] == "a":
        is_a_star_search = True
        gif_file_name = "a_star_search.gif"

    # ******************************** BFS, A* Search ********************************
    global path_hash_map

    row, col = start
    path_hash_map = {(row, col): None}  # dictionary that uses the current node being traversed as the key, and its
    # parent as the value. This is so we can print the path from end to start later on.

    if bfs(is_a_star_search):
        print("Found End!!")

        # Print path from start to end
        current = (treasure[0], treasure[1])
        path = [(treasure[0], treasure[1])]

        while current is not None and current[0] != start[0] or current[1] != start[1]:
            current = path_hash_map.get(current)
            path.insert(0, current)

            helper.draw_maze(start, treasure, path)

        print("Path cost:", len(path) - 1)
        print("Path: ", path)
        print("Number of nodes explored before finding exit: ", nodes_explored)
    else:
        print("Couldn't find treasure")

    helper.create_and_save_gif(gif_file_name)


if __name__ == "__main__":
    main()
