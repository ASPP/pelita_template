TEAM_NAME = 'Basic Eating Bots'

import networkx

from pelita.utils import walls_to_graph


def move(bot, state):
#    if state == {} or state["target"] is None:
#        state["target"] = bot.random.choice(bot.enemy[0].food)
    target =  bot.random.choice(bot.enemy[0].food)
    graph = walls_to_graph(bot.walls)

    #path = networkx.shortest_path(graph, bot.position, state["target"])[1:]
    path = networkx.shortest_path(graph, bot.position, target)[1:]
#    if len(path) == 1:
#        state["target"] = None

    next_pos = path[0]
    return next_pos
