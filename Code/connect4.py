def calcPlayerPoints(board, player):
    """
    Calculate the number of points a player has scored in Connect 4.
    
    Sequences of 4+ pieces score points:
    - 4 in a row: 1 point
    - 5 in a row: 2 points
    - 6 in a row: 3 points
    - n in a row: (n - 3) points
    
    Args:
        board: List of strings representing the NxN board
        player: 'B' or 'W' representing the player
    
    Returns:
        Total points scored by the player
    
    Note:
        The board is assumed to have equal numbers of 'B' and 'W' pieces,
        simulating alternating turns in a real game.
    """
    if not board or not board[0]:
        return 0
    
    n = len(board)
    total_points = 0
    visited = set()
    
    def count_consecutive(row, col, dr, dc):
        """Count consecutive pieces starting from a position in a direction."""
        count = 0
        r, c = row, col
        
        while 0 <= r < n and 0 <= c < n and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        
        return count
    
    def get_full_sequence(row, col, dr, dc):
        """Get all cells in a sequence by extending in both directions."""
        cells = []
        
        r, c = row, col
        while 0 <= r < n and 0 <= c < n and board[r][c] == player:
            r -= dr
            c -= dc
        
        r += dr
        c += dc
        
        while 0 <= r < n and 0 <= c < n and board[r][c] == player:
            cells.append((r, c))
            r += dr
            c += dc
        
        return tuple(sorted(cells))
    
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal down-right
        (1, -1)   # diagonal down-left
    ]
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == player:
                for dr, dc in directions:
                    sequence = get_full_sequence(row, col, dr, dc)
                    
                    if len(sequence) >= 4 and sequence not in visited:
                        visited.add(sequence)
                        points = len(sequence) - 3
                        total_points += points
    
    return total_points
