from collections import Counter

def count_letters_on_board(board):
    """ Count the frequency of each letter on the board, given a 2D list of 
    letters or blanks, and return a Counter mapping each letter to its 
    occurrence frequency. """
    # Flatten 2D board into 1D list for counting
    letters = [letter for row in board for letter in row]
    return Counter(letters)

def can_word_be_formed(word, board_counter):
    """ Check if the target word can be formed using available letters and 
    blanks on the board, based on the provided letter frequency counter. """
    word_counter = Counter(letter for letter in word)
    blanks = board_counter.get('_', 0)
    # Check each letter requirement against board inventory
    for letter, required in word_counter.items():
        available = board_counter.get(letter, 0)
        shortage = required - available
        
        # Use blanks to cover any shortage
        if shortage > 0:
            blanks -= shortage
            # Not enough blanks to compensate
            if blanks < 0:
                return False
                
    return True

def words_on_board(words, board):
    """ Filter the list of words to include only those that can be formed using 
    the letters and blanks available on the board. """
    board_counter = count_letters_on_board(board)
    
    # Filter words to only those formable from board resources
    return [word for word in words if can_word_be_formed(word, board_counter)]