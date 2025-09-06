import matchmaking
import json

# Load players
with open('../data/players.json') as f:
    players = json.load(f)

# Example: Match player 1
player = players[0]
opponents = players[1:]
match = matchmaking.find_best_match(player, opponents, rigging_intensity=0.5)
print(f"Matched Opponent: {match}")
