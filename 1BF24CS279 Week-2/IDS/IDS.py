def print_board(board):
    """Prints the 3x3 puzzle board."""
    for i in range(0, 9, 3):
        print(board[i : i + 3])
    print()


def get_neighbors(state):
    """Generates valid neighboring states by moving the blank tile (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    # Possible movements: (row_change, col_change, direction_name)
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

    for dr, dc, _ in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            # Swap blank with the adjacent tile
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = (
                new_state[new_idx],
                new_state[zero_idx],
            )
            neighbors.append(tuple(new_state))

    return neighbors


def dls(state, goal, limit, path, visited):
    """Depth-Limited Search helper function for IDS."""
    if state == goal:
        return path

    if limit <= 0:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            path.append(neighbor)
            result = dls(neighbor, goal, limit - 1, path, visited)
            if result is not None:
                return result
            path.pop()  # Backtrack

    visited.remove(state)
    return None


def ids(start_state, goal_state, max_depth=20):
    """Iterative Deepening Search algorithm."""
    start_tuple = tuple(start_state)
    goal_tuple = tuple(goal_state)

    for depth in range(max_depth + 1):
        visited = set()
        path = [start_tuple]
        result = dls(start_tuple, goal_tuple, depth, path, visited)
        if result is not None:
            return result, depth

    return None, None


# Example usage:
if __name__ == "__main__":
    # 0 represents the empty/blank tile
    initial_board = [1, 2, 3, 5, 0, 6, 4, 7, 8]
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    print("Initial Board:")
    print_board(initial_board)

    print("Running Iterative Deepening Search (IDS)...")
    solution_path, found_depth = ids(initial_board, goal_board, max_depth=15)

    if solution_path:
        print(f"Solution found at depth {found_depth}!\n")
        print("Steps:")
        for step, board_state in enumerate(solution_path):
            print(f"Step {step}:")
            print_board(board_state)
    else:
        print("No solution found within the depth limit.")