def calculate_value(board):
    """ Calculate the total Scrabble score of a given word using standard point 
    values assigned to each letter in the official Scrabble scoring system. """

    # Create a dictionary to map each letter to its point value
    letter_values = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'N': 1,
        'R': 1, 'T': 1, 'L': 1, 'S': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 
        'P': 3,
        'F': 4, 'H': 4, 'V': 4,
        'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10,
        # Explicit blank handling 
        '_': 0}

    total_points = 0
    
    # Iterate through each row and letter on the board
    for row in board:
        for letter in row:
            # Add the letter's value (0 if blank or invalid)
            total_points += letter_values.get(letter, 0)

    return total_points