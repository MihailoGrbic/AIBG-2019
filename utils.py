from PlayerInfo import PlayerInfo
from Map import Map


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def move_available(current_queue: list, current_map: Map, x, y):
    for e in current_queue:
        if e[0] == x and e[1] == y:
            return False
    return 0 <= x <= current_map.width and 0 <= y <= current_map.height and current_map.tiles[y][x]['item'] is None


def find_path_to(player: PlayerInfo, current_map: Map, x, y):
    # list of (x, y, cost, dir)
    queue = [(player.x, player.y, dist(x, y, player.x, player.y), None)]
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
        if move_available(queue, current_map, next_move_w[0], next_move_w[1]):
            queue.append(next_move_w)
        if move_available(queue, current_map, next_move_a[0], next_move_a[1]):
            queue.append(next_move_a)
        if move_available(queue, current_map, next_move_s[0], next_move_s[1]):
            queue.append(next_move_s)
        if move_available(queue, current_map, next_move_d[0], next_move_d[1]):
            queue.append(next_move_d)
    return path
