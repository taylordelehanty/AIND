

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    if gameState.get_legal_moves() == []: # get_legal_moves already knows which player's move it is
        return True
    else: return False

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1
    else:
        v = float("inf")
        for move in gameState.get_legal_moves():
            v = min(v, max_value(gameState.forecast_move(move)))
        return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1
    else:
        v = float("-inf")
        for move in gameState.get_legal_moves():
            v = max(v, min_value(gameState.forecast_move(move)))
        return v
