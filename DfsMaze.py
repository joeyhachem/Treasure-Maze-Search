import sys
import helper

dfs_path = []
path_cost = 0
nodes_explored = 0

start = 11, 2
treasure = 19, 23


def print_dfs_path() -> None:
    for tupleValues in reversed(dfs_path):
        print("(", tupleValues[0], tupleValues[1], ")")


# Depth-First Search Implementation / Recursive solution
def dfs(row: int, col: int) -> bool:
    global path_cost
    global nodes_explored

    # ignore visited boxes
    if helper.visited[row][col] == 1:
        return False

    # if we're at the treasure location
    if row == treasure[0] and col == treasure[1]:
        return True

    helper.visited[row][col] = 1
    nodes_explored = nodes_explored + 1
    helper.draw_maze(start, treasure)

    # go up, check if there is no wall first.
    if row > 0 and helper.maze[row - 1][col] == 0 and dfs(row - 1, col):
        dfs_path.append((row - 1, col))
        path_cost += 1
        return True

    # go right, check if there is no wall first.
    if col < len(helper.maze) - 1 and helper.maze[row][col + 1] == 0 and dfs(row, col + 1):
        dfs_path.append((row, col + 1))
        path_cost += 1
        return True

    # go down, check if there is no wall first.
    if row < len(helper.maze) - 1 and helper.maze[row + 1][col] == 0 and dfs(row + 1, col):
        dfs_path.append((row + 1, col))
        path_cost += 1
        return True

    # go left, check if there is no wall first.
    if col > 0 and helper.maze[row][col - 1] == 0 and dfs(row, col - 1):
        dfs_path.append((row, col - 1))
        path_cost += 1
        return True

    return False


def main():
    global start, treasure
    gif_file_name = "dfs-maze.gif"

    # Setup start and treasure positions based on run parameters
    if sys.argv[1] is not None:
        start = int(sys.argv[1]), int(sys.argv[2])
        treasure = int(sys.argv[3]), int(sys.argv[4])

    # ******************************** DFS ********************************
    row, col = start  # root node
    if dfs(row, col):
        print("Found treasure!")
        dfs_path.append((row, col))

        print("Path Cost =", path_cost)
        print_dfs_path()

        for _i in range(len(dfs_path)):
            helper.draw_maze(start, treasure, dfs_path)
        print("Number of nodes explored before finding exit: ", nodes_explored)
    else:
        print("Couldn't find exit :(")

    helper.create_and_save_gif(gif_file_name)


if __name__ == "__main__":
    main()
