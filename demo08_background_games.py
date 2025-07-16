# Run this script with
#
# python3 demo08_background_games.py
#
# - Run 100 games in the background to gather statistics
# - We'll use a team of basic hunters against a team of basic gatherers

from pelita.utils import run_background_game

from demo05_basic_hunter import move as move_hunter
from demo04_basic_gatherer import move as move_gatherer

NUM_GAMES = 100

collection = []

for idx in range(NUM_GAMES):
    print('.', end='', flush=True)

    # dictionary to store game parameters
    game = {}

    # play with the hunters and gatherers as blue and red team alternatively
    if idx%2 == 0:
        blue = move_hunter
        red = move_gatherer
        game['blue'] = 'hunter'
    else:
        blue = move_gatherer
        red = move_hunter
        game['blue'] = 'gatherer'

    # play each time on a different maze
    result = run_background_game(blue_move=blue, red_move=red)
    game['result'] = result

    # add to our collection of games
    collection.append(game)

# At the end we can pickle the results to be analyzed later:
#import pickle
#with open('results.pic', 'wb') as fh:
#    pickle.dump(collection, fh)
#
# - To open the pickle in another process:
#with open('results.pic', 'rb') as fh:
#    collection = pickle.load(fh)

# - If you want to replay a particular game, let's say the 10th game:
#replay = collection[10]

# - first check who was blue
#blue = replay['blue']
# - get the random seed for the game
#seed = replay['result']['seed']
# - let's assume that the gatherer was blue, and the seed was 1234567,
#   then you can replay on the terminal with
# pelita --seed 1234567 demo04_basic_gatherer.py demo05_basic_hunter.py

# Here we only want to print some basic stats
gatherer_wins = 0
hunter_wins = 0
draws = 0
# this is gatherer_score-defender_score
score_difference = 0

for i, game in enumerate(collection):
    blue = game['blue']
    result = game['result']
    if result['draw']:
        draws += 1
    elif blue == 'gatherer':
        gatherer_wins += result['blue_wins']
        hunter_wins += result['red_wins']
        score_difference += result['blue_score'] - result['red_score']
    elif blue == 'hunter':
        gatherer_wins += result['red_wins']
        hunter_wins += result['blue_wins']
        score_difference += result['red_score'] - result['blue_score']

print(f'Games played: {len(collection)}')
print(f'Gatherer wins: {gatherer_wins}')
print(f'Hunter wins: {hunter_wins}')
print(f'Draws: {draws}')
print(f'Average score difference: {score_difference/(i+1)}')

