# from warnings import warn
import numpy as np
from sportsreference.ncaab.roster import Player

from player_ids import *

years = [id_2000, id_2001, id_2002, id_2003, id_2004, id_2005]
for year in years:
    for [player_id, is_all_star] in year:
        player = Player(player_id)

# conference, position, height, weight, offensive win shares, devensive win shares, minutes/games, fg, fga, fgp, threes, 3pa, 3pp, twos, 2pa, 2pp, ft, fta, tfp, ORB, DRB, rb, asst, steal, block, tos, fouls, points, true shooting percent, effect. field goal percent, attempt rates,
