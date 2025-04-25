# This bot tries to catch an enemy bot. It will stop at the border of its
# homezone if the enemy still did not cross the border.
# As long as the enemies are far away (their position is noisy), the bot
# tries to get near to the bot in the enemy team which has the same turn.
# As soon as an enemy bot is not noisy anymore, i.e. it has come near, the
# bot goes after it and leaves the other enemy alone

import networkx


TEAM_NAME = 'Basic Defender Bots'

def init_defend_state():
    return {
            "defend_target": None,
            "defend_path": None,
        }

def move(bot, state):
    if state == {}:
        state[0] = init_defend_state()
        state[1] = init_defend_state()

    turn = bot.turn
    if (not bot.enemy[0].is_close) and (not bot.enemy[1].is_close):
        # if both enemies are far away, just aim for our turn companion
        target = bot.enemy[turn].position
    elif bot.enemy[turn].is_close:
        # if our turn companion is close, go for it
        target = bot.enemy[turn].position
    elif bot.enemy[1-turn].is_close:
        # if the other enemy is close, go for it
        target = bot.enemy[1-turn].position
    else:
        raise Exception('We should never be here!')

    # get the next position along the shortest path to our target enemy bot
    next_pos = networkx.shortest_path(bot.graph, bot.position, target)[1]
    # we save the current target in our state dictionary
    state[bot.turn]["defend_target"] = target

    # let's check that we don't go into the enemy homezone, i.e. stop at the
    # border
    if next_pos in bot.enemy[turn].homezone:
        next_pos = bot.position

    return next_pos
