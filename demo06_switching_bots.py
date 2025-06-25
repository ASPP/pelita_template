# This demo shows how to combine the strategies of the basic gatherer and the
# basic hunter
# Initially, one bot is in gather mode, while the other uses the hunting
# strategy. Once the gathering bot is killed, it restarts as a hunter, while
# the previous hunter changes its personality and becomes the new gatherer.

from demo05_basic_hunter import move as move_hunter
from demo04_basic_gatherer import move as move_gatherer


TEAM_NAME = 'Switching Bots'

def init_state(personality):
    return {
        # specifies which personality we are: "gatherer" or "hunter"
        "personality": personality,

        # entries prefixed with "gatherer_" are used by the move_gatherer function
        "gatherer_target": None,
        "gatherer_path": None,

        # entries prefixed with "hunter_" are used by the move_hunter function
        "hunter_target": None,
        "hunter_path": None,
    }

def move(bot, state):
    # Our state consists of two “substates”, one for each bot.
    # In order for the substates to work properly with the imported
    # `move_gatherer` and `move_hunter` funcions, we need to be sure
    # that the relevant attributes in the state are properly prefixed
    # (and each of the functions only works with “their” prefixed version).

    if state == {}:
        # here each bot has its own state dictionary (0 and 1)
        state[0] = init_state("gatherer")
        state[1] = init_state("hunter")

    # Only the gatherer can go into the enemy zone and be killed. Therefore
    # we only need to switch roles from the perspective of the hunter.
    if bot.other.was_killed:
        state[bot.turn]["personality"] = "gatherer"
        state[bot.other.turn]["personality"] = "hunter"

    if state[bot.turn]["personality"] == "gatherer":
        next_pos = move_gatherer(bot, state)
        bot.say('gatherer')
    else:
        next_pos = move_hunter(bot, state)
        bot.say('hunter')
    return next_pos

