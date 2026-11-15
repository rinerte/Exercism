def gamestate(board):
    flat = ''.join(board)
    x = flat.count('X')
    o = flat.count('O')
    
    
    if x-o > 1:
        raise ValueError("Wrong turn order: X went twice")
    if o>x:
        raise ValueError("Wrong turn order: O started")

    lines = [
        *board,
        *(''.join(col) for col in zip(*board)),
        flat[0::4],
        flat[2:7:2],
    ]

    o_win = 'OOO' in lines
    x_win = 'XXX' in lines
    
    if (o_win>0 and x_win>0) or (x_win>0 and x==o) or (o_win>0 and x>o):
        raise ValueError("Impossible board: game should have ended after the game was won")
        
    if o_win or x_win:
        return "win"
        
    return "ongoing" if ' ' in flat else "draw"
    
        
    
        
        
        
