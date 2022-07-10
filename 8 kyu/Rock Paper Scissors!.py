def rps(p1, p2):
    if p1 == p2: return "Draw!"
    elif p1 == 'rock': return "Player 2 won!" if p2 == 'paper' else "Player 1 won!"
    elif p1 == 'paper': return "Player 2 won!" if p2 == 'scissors' else "Player 1 won!"
    elif p1 == 'scissors': return "Player 2 won!" if p2 == 'rock' else "Player 1 won!"
