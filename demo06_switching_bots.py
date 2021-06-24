# This bot switches its personality when one guy dies
TEAM_NAME = 'Switching Bots'

import networkx

from pelita.utils import walls_to_graph

from demo05_basic_defender import move as move_defender
from demo04_basic_attacker import move as move_attacker

def init_state(personality):
    return {
        "personality": personality,
        "attack_target": None,
        "defend_target": None,
        "defend_path": None,
        "attack_path": None,
    }

def move(bot, state):
    # Keep two "substates" — one for each bot
    if state == {}:
        # here each bopt has its own state dictionary (0 and 1) and they share
        # the same game state information in the "graph"
        state['graph'] = walls_to_graph(bot.walls)
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

