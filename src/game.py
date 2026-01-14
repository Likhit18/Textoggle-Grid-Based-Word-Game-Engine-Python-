import copy

def remove_letters(board, positions):
    """ Mark positions as None to remove letters. Modifies board in-place. """
    for row, col in positions:
        board[row][col] = None

def collapse_column(board, col, spare_letters, spare_index):
    """ Collapse column downward, fill with spares or '#'. Modifies board. """
    
    # Collect non-None letters from bottom to top
    remaining = [board[row][col] for row in range(len(board) - 1, -1, -1)
        if board[row][col] is not None]
    
    # Refill column from bottom up
    for row in range(len(board) - 1, -1, -1):
        if remaining:
            # Replace with existing letter from column
            board[row][col] = remaining.pop(0)
        elif spare_index[0] < len(spare_letters):
            # Use next available spare letter
            board[row][col] = spare_letters[spare_index[0]]
            spare_index[0] += 1
        else:
            # Mark as empty when no spares remain
            board[row][col] = '#'

def textoggle_move(board, word_sequence, spare_letters):
    """ Process Textoggle move: remove word, collapse columns, refill spares.
    Returns new board without modifying original. """
    # Create deep copy to avoid modifying original board
    new_board = copy.deepcopy(board)
    # Remove letters used in the word
    remove_letters(new_board, word_sequence)
    # Track position in spare letters list
    spare_index = [0]
    
    # Process each column left-to-right
    for col in range(len(new_board[0])):
        collapse_column(new_board, col, spare_letters, spare_index)
    
    return new_board