from sys import stdin
players = stdin.readline().split()
total_games = int(stdin.readline())
for this_game in range(total_games):
    game_eval, points = True, [0,0]
    matches = stdin.readline().split()
    if len(matches) not in (3,2): game_eval = False
    else:
        # Evaluate first two sets
        for match in matches[:2]:
            match_stats = list(map(int, match.split(':')))
            if match_stats[0] > match_stats[1]: points[0] += 1
            elif match_stats[1] > match_stats[0]: points[1] += 1
            else:
                game_eval = False

            mn, mx = sorted(match_stats)
            if mx < 6: game_eval = False
            elif mx == 6:
                if (mx - mn) < 2: game_eval = False
            elif mx > 7: game_eval = False
            else:
                if mn < 5: game_eval = False

        # Evaluate third set if exists
        if len(matches) == 3:
            match = matches[2]
            match_stats = list(map(int, match.split(':')))
            if match_stats[0] > match_stats[1]: points[0] += 1
            elif match_stats[1] > match_stats[0]: points[1] += 1
            else:
                game_eval = False
            mn, mx = sorted(match_stats)
            if mx < 6:
                game_eval = False
            elif mx == 6:
                if (mx - mn) < 2:
                    game_eval = False
            else:
                if (mx - mn) != 2:
                    game_eval = False
        if (players[1] == 'federer' and points[0] > 0) \
            or (players[0] == 'federer' and points[1] > 0) \
            or  (max(points[0], points[1]) != 2): game_eval = False
    print('da') if game_eval else print('ne')