from src.scoring import calculate_value
from src.word_checks import words_on_board
from src.pathfinding import word_on_board
from src.game import textoggle_move

def demo():
    board = [
        ['X', 'A', 'J', 'H'],
        ['I', 'S', 'R', 'T'],
        ['C', 'K', 'E', '_'],
        ['M', 'U', 'O', 'S']
    ]

    print("Board value:", calculate_value(board))
    print("Words possible (simple):", words_on_board(["JAM", "CAKE", "ZOO"], board))
    print("Path for 'JAM' (adjacency):", word_on_board("JAM", board))

if __name__ == "__main__":
    demo()