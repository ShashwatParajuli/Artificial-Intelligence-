import random
import math

def calculate_cost(board):
    cost = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1

    return cost


def print_board(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def simulated_annealing():
    n = 8

    for restart in range(100):
        board = [random.randint(0, n - 1) for _ in range(n)]
        current_cost = calculate_cost(board)

        T = 100
        alpha = 0.99

        while T > 0.01:
            if current_cost == 0:
                print("Solution Found!")
                print("Board:", board)
                print_board(board)
                return

            neighbor = board[:]

            col = random.randint(0, n - 1)
            row = random.randint(0, n - 1)

            while row == neighbor[col]:
                row = random.randint(0, n - 1)

            neighbor[col] = row

            new_cost = calculate_cost(neighbor)
            delta = new_cost - current_cost

            if delta < 0:
                board = neighbor
                current_cost = new_cost

            else:
                probability = math.exp(-delta / T)

                if random.random() < probability:
                    board = neighbor
                    current_cost = new_cost

            T = T * alpha

    print("Solution Not Found")


simulated_annealing()