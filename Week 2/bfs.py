from board import board

def bfs(initial_board, goal_board):
    frontier = []
    explored = set()
    frontier.append(initial_board)

    while not frontier == []:
        state = frontier.pop()
        explored.add(state)
        leaf_nodes = [board(state.move(x)) for x in range(4)]
        state.print_board()
        print("")

        if goal_board.values == state.values:
            print("board encontrado")
            state.print_board()
            print("")
            return True

        for neighbor in leaf_nodes:
            if neighbor not in frontier and neighbor not in explored:
                frontier.insert(0,neighbor)
    print("board nao encontrado")
    return False
