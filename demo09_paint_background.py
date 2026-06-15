# This bot does not move, but it paints a colored danger zone around the (estimated) enemy positions

TEAM_NAME = 'PaintingBots'

def manhattan(pos1, pos2):
    """Return the Manhattan distance between two positions."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def danger_zone(position, size=3):
    """Return a list of dangerous coordinates around position.

    Parameters
    ----------

      size : int

           the size of the danger zone measured in manhattan distance
    """
    x, y = position
    return [ (i,j) for i in range(x-size, x+size+1)
                   for j in range(y-size, y+size+1)
                   if manhattan((i, j), (x, y)) <= size ]

def move(bot, state):
    danger_size = 2
    # paint green danger zone around enemy0
    for pos in danger_zone(bot.enemy[0].position, size=danger_size):
        bot.paint_background(pos, '#FFFFA8')
    # paint yellow danger zone around enemy1
    for pos in danger_zone(bot.enemy[1].position, size=danger_size):
        bot.paint_background(pos, '#96FF96')
    # do not move at all
    return bot.position
