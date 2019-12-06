from PlayerInfo import PlayerInfo
from Map import Map


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_path_to(player: PlayerInfo, current_map: Map, x, y):
    # list of (x, y, cost, dir)
    queue = [(player.x, player.y, dist(x, y, player.x, player.y), '0')]
    path = []
    while True:
        # find best
        best = (-1, -1, 9999)
        for e in queue:
            if e[2] < best[2]:
                best = e
        # add to path
        queue.remove(best)
        path.append(best[3])
        # add new nodes
        next_move_w = (best.x, best.y - 1, dist(best.x, best.y - 1, x, y), 'w')
        next_move_a = (best.x - 1, best.y, dist(best.x - 1, best.y, x, y), 'a')
        next_move_s = (best.x, best.y + 1, dist(best.x, best.y + 1, x, y), 's')
        next_move_d = (best.x + 1, best.y, dist(best.x - 1, best.y, x, y), 'd')
        for e in queue:
            if (e[0] != next_move_w[0] or e[1] != next_move_w[1])\
                    and (next_move_w[0] >= 0 and next_move_w[0] <= current_map.width):
                queue.append(next_move_w)
            if (e[0] != next_move_a[0] or e[1] != next_move_a[1])\
                    and (next_move_w[0] >= 0 and next_move_w[0] <= current_map.width):
                queue.append(next_move_w)
            if (e[0] != next_move_s[0] or e[1] != next_move_s[1])\
                    and (next_move_w[0] >= 0 and next_move_w[0] <= current_map.width):
                queue.append(next_move_w)
            if (e[0] != next_move_d[0] or e[1] != next_move_d[1])\
                    and (next_move_w[0] >= 0 and next_move_w[0] <= current_map.width):
                queue.append(next_move_w)
    return path
