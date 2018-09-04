import time
# This bot takes random moves, chosen among the legal ones for its current
# position, but will not step on its teammate's toes.

TEAM_NAME = 'PoliteRandomBots'

def move(turn, game):
    bot = game.team[turn]
    teammate = game.team[1 - turn]
    x0, y0 = bot.position
    x1, y1 = teammate.position
    move_to_teammate = (x1 - x0, y1 - y0)
    possible_moves = bot.legal_moves[:]
    if move_to_teammate in possible_moves:
        bot.say('Excuse me. Sorry. Excuse me.')
        possible_moves.remove(move_to_teammate)
    return bot.random.choice(possible_moves)