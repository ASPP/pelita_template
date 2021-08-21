# This bot selects a food pellet at random, then goes and tries to get it by
# following the shortest path to it.
# It tries on the way to avoid being killed by the enemy: if the next move
# to get to the food would put it on a ghost, then it chooses a random safe
# position
TEAM_NAME = 'Basic Attacker Bots'


import networkx

from pelita.utils import walls_to_graph

def init_attack_state():
    return {
            "attack_target": None,
            "attack_path": None,
        }

def move(bot, state):
    # The state dictionary is initially empty
    if state == {}:
        # Initialize the state dictionary.
        # Each bot needs its own state dictionary to keep track of the
        # food targets.
        state[0] = init_attack_state()
        state[1] = init_attack_state()
        # Initialize a graph representation of the maze.
        # This can be shared among our bots.
        state['graph'] = walls_to_graph(bot.walls)

    # define a few variables for less typing
    enemy = bot.enemy

    target = state[bot.turn]["attack_target"]
    path = state[bot.turn]["attack_path"]

    # choose a target food pellet if we still don't have one or
    # if the old target has been already eaten
    if (target is None) or (target not in enemy[0].food):
        # position of the target food pellet
        target = bot.random.choice(enemy[0].food)
        # use networkx to get the shortest path from here to the target
        # we do not use the first position, which is always equal to bot_position
        path = networkx.shortest_path(state['graph'], bot.position, target)[1:]
        state[bot.turn]["attack_path"] = path
        state[bot.turn]["attack_target"] = target

    # get the next position along the shortest path to reach our target
    next_pos = path.pop(0)
    # if we are not in our homezone we should check if it is safe to proceed
    if next_pos not in bot.homezone:
        # get a list of safe positions
        safe_positions = []
        for pos in bot.legal_positions:
            if pos not in (enemy[0].position, enemy[1].position):
                safe_positions.append(pos)

        # we are about to step on top of an enemy
        if next_pos not in safe_positions:
            # 1. Let's forget about this target and this path
            #    We will choose a new target in the next round
            state[bot.turn]["attack_target"] = None
            state[bot.turn]["attack_path"] = None
            # watch out! We only want to overwrite these two keys:
            # in your bots you may have other relevant information in the state
            # dictionary that you don't want to delete here!

            # Choose one safe position at random (this always includes the
            # current position
            next_pos = bot.random.choice(safe_positions)

    return next_pos
