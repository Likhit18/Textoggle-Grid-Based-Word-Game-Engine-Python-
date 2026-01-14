def map_letters_to_positions(board):
    """ Return a dict mapping each letter to its (row, col) 
    position on the board. """
    # Dictionary comprehension to create {letter: (row, col)} mapping
    return {board[r][c]: (r, c)
        for r in range(len(board))
        for c in range(len(board[0]))}

def is_adjacent(pos1, pos2):
    """ Return True if pos1 and pos2 are 
    adjacent horizontally/vertically. """
    # Manhattan distance == 1 means adjacent (no diagonal)
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1

def word_on_board(word, board):
    """ Return the path of adjacent letters 
    forming the word, or None if invalid. """
    # Edge case: empty word
    if not word:
        return None
    # Reject repeated letters in the word
    if len(set(word)) < len(word):
        return None

    letter_pos = map_letters_to_positions(board)
    path = []
    # Verify each letter is present and adjacent to previous
    for i, letter in enumerate(word):
        if letter not in letter_pos:
            return None
        
        current_pos = letter_pos[letter]
        
        # First letter just starts the path
        if i == 0:
            path.append(current_pos)
        else:
            # Subsequent letters must be adjacent to previous
            if not is_adjacent(path[-1], current_pos):
                return None
            path.append(current_pos)

    return path