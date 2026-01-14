import copy
from collections import deque, Counter

SCRABBLE_POINTS = {**{c: 1 for c in "EAIONRTLSU"}, **{c: 2 for c in "DG"},
                   **{c: 3 for c in "BCMP"}, **{c: 4 for c in "FHVWY"},
                   "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10, "_": 0}


def load_words():
    with open("words_alpha.txt") as f:
        return [word.strip().upper() for word in f
                if len(word.strip()) >= 2]


def calculate_score(path, board):
    return sum(SCRABBLE_POINTS[board[r][c]] for r, c in path) * len(path)


def is_word_possible(word, board, spares):
    available = Counter()
    for row in board:
        for c in row:
            if c and c != '#':
                available[c] += 1
    for c in spares:
        available[c] += 1
    need = Counter(word)
    blanks_needed = 0
    for c in need:
        diff = need[c] - available.get(c, 0)
        if diff > 0:
            blanks_needed += diff
    return blanks_needed <= available.get('_', 0)


def find_word_path(word, board):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] or board[r][c] == '_':
                stack = deque()
                stack.append((r, c, 0, set(), []))
                while stack:
                    cr, cc, idx, visited, path = stack.pop()
                    if (cr, cc) in visited or idx >= len(word):
                        continue
                    ch = board[cr][cc]
                    if ch != word[idx] and ch != '_':
                        continue
                    new_visited = visited.copy()
                    new_visited.add((cr, cc))
                    new_path = path + [(cr, cc)]
                    if idx == len(word) - 1:
                        return new_path
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            stack.append((nr, nc, idx + 1,
                                          new_visited, new_path))
    return None


def collapse(board, col, spares):
    col_vals = [board[r][col] for r in range(len(board)) if board[r][col]]
    new_col = []
    for _ in range(len(board)):
        if col_vals:
            new_col.append(col_vals.pop())
        elif spares:
            new_col.append(spares.pop(0))
        else:
            new_col.append('#')
    for r in range(len(board)):
        board[r][col] = new_col[len(board) - r - 1]


def remove_and_refill(board, path, spares):
    for r, c in path:
        board[r][c] = None
    for c in range(len(board[0])):
        collapse(board, c, spares)
    return board, spares


def play_best_game(board, spare_letters):
    words = load_words()
    words.sort(key=lambda w: (-len(w), w))
    board = copy.deepcopy(board)
    spares = list(spare_letters)
    total = 0
    while True:
        best_word, best_score, best_path = None, -1, None
        for word in words:
            if len(word) > len(board) * len(board[0]):
                continue
            if not is_word_possible(word, board, spares):
                continue
            path = find_word_path(word, board)
            if not path:
                continue
            score = calculate_score(path, board)
            if score > best_score or (
                score == best_score and word < best_word
            ):
                best_word, best_score, best_path = word, score, path
        if not best_path:
            break
        total += best_score
        board, spares = remove_and_refill(board, best_path, spares)
    return total