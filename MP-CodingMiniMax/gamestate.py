from copy import deepcopy

x_dim, y_dim = 3, 2

class GameState:

    def __init__(self):
        self.board = [[0] * y_dim for _ in range(x_dim)] # array of some size
        self.board[-1][-1] = 1 # mark bottom right corner
        self.player_turn = 0 # boolean: 0 = 1st player, 1 = 2nd player
        self.players_location = [None, None] # array of 2 tuples
    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        # look at legal moves, determine if it's ok
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")

        # copy board, mark new move on board, update player location
        board_copy = deepcopy(self)
        board_copy.board[move[0]][move[1]] = 1
        board_copy.players_location[self.player_turn] = move
        board_copy.player_turn = not board_copy.player_turn
        return board_copy
    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        # must remain inside board
        # cannot be where a player has moved before
        # cannot move through obstacles
            
        # remember: see player location with self.players_location[self.player_turn]
        start_pos = self.players_location[self.player_turn] # (x, y)
        
        if start_pos == None:
            flat_board = [(x, y) for x in range(x_dim) for y in range(y_dim) if self.board[x][y] != 1]
            return flat_board

        # each_step = (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)
        deltas = [-1, 0, 1]
        steps = [(x, y) for x in deltas for y in deltas if not (x == 0 and y == 0)]
        legal_moves = []
        
        for step_x, step_y in steps:
            pos_x, pos_y = start_pos
            while (0 <= pos_x + step_x < x_dim) and (0 <= pos_y + step_y < y_dim) and self.board[pos_x + step_x][pos_y + step_y] != 1:
                pos_x, pos_y = pos_x + step_x, pos_y + step_y
                legal_moves.append((pos_x, pos_y))
        return legal_moves
