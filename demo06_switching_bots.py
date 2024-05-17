# This demo shows how to combine the strategies of the basic attacker and the
# basic defender
# Initially, one bot is in attack mode, while the other uses the defending
# strategy. Once the attacking bot is killed, it restarts as a defender, while
# the previous defender changes its personality and becomes the new attacker.

from demo05_basic_defender import move as move_defender
from demo04_basic_attacker import move as move_attacker


TEAM_NAME = 'Switching Bots'

def init_state(personality):
    return {
        # specifies which personality we are: "attacker" or "defender"
        "personality": personality,

        # entries prefixed with "attack_" are used by the move_attacker function
        "attack_target": None,
        "attack_path": None,

        # entries prefixed with "defend_" are used by the move_defender function
        "defend_target": None,
        "defend_path": None,
    }

def move(bot, state):
    # Our state consists of two “substates”, one for each bot.
    # In order for the substates to work properly with the imported
    # `move_attacker` and `move_defender` funcions, we need to be sure
    # that the relevant attributes in the state are properly prefixed
    # (and each of the functions only works with “their” prefixed version).

    if state == {}:
        # here each bot has its own state dictionary (0 and 1)
        state[0] = init_state("attacker")
        state[1] = init_state("defender")

    # Only the attacker can go into the enemy zone and be killed. Therefore
    # we only need to switch roles from the perspective of the defender.
    if bot.other.was_killed:
        state[bot.turn]["personality"] = "attacker"
        state[bot.other.turn]["personality"] = "defender"

    if state[bot.turn]["personality"] == "attacker":
        next_pos = move_attacker(bot, state)
        bot.say('attacker')
    else:
        next_pos = move_defender(bot, state)
        bot.say('defender')
    return next_pos

