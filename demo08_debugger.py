# This bot shows how to enable a debugger session to explore the objects
# IMPORTANT: timeouts need to be disabled, or you will not have time to use
# the debugger at all. Run a game with:
# pelita --no-timeout demo08_debugger.py demo01_stopping.py
#

TEAM_NAME = 'Debuggable Bot'

def move(bot, state):
    # in Python >= 3.7 this can be changed to simply
    # breakpoint()
    import pdb; pdb.set_trace()
    next_move = (0,0)
    return next_move, state

if __name__ == '__main__':
    import pelita
    layout_name, layout_string = pelita.layout.get_random_layout(filter="small")
    pelita.libpelita.run_game([move, "demo01_stopping.py"], rounds=30, layout=layout_string)
