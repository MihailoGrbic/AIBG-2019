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


# return the position of the nearest item from pos[0], pos[1]
def find_nearest(pos: tuple, items: list):
    min_dist = -1
    min_dist_pos = None
    for item in items:
        curr_dist = dist(*pos, *item)
        if min_dist_pos is None or curr_dist < min_dist:
            min_dist = curr_dist
            min_dist_pos = item

    return min_dist_pos


# a matrix of size mapSize[0],mapSize[1], having tuple of (x,y) pairs as elements
# which represent the position of the nearest item
def nearest_to_map(mapSize: tuple, items: list):
    nearest_dist = [[-1 for x in range(mapSize[1])] for y in range(mapSize[0])]
    nearest_pos = [[(-1, -1) for x in range(mapSize[1])] for y in range(mapSize[0])]

    # holds tuple of coors
    queue = []

    for item in items:
        i,j = item
        nearest_dist[i][j] = 0
        nearest_pos[i][j] = item
        if i > 0 and nearest_dist[i-1][j] == -1:
            nearest_dist[i-1][j] = 1
            nearest_pos[i-1][j] = (i,j)
            queue += [(i-1,j)]
        if j > 0 and nearest_dist[i][j-1] == -1:
            nearest_dist[i][j-1] = 1
            nearest_pos[i][j-1] = (i,j)
            queue += [(i,j-1)]
        if i < mapSize[0]-1 and nearest_dist[i+1][j] == -1:
            nearest_dist[i+1][j] = 1
            nearest_pos[i+1][j] = (i,j)
            queue += [(i+1,j)]
        if j < mapSize[1] - 1 and nearest_dist[i][j+1] == -1:
            nearest_dist[i][j+1] = 1
            nearest_pos[i][j+1] = (i,j)
            queue += [(i,j+1)]

    curr_ind = 0
    while curr_ind != len(queue):
        i,j = queue[curr_ind]
        curr_ind += 1

        val = nearest_dist[i][j]

        if i > 0 and nearest_dist[i - 1][j] == -1:
            nearest_dist[i - 1][j] = val+1
            nearest_pos[i-1][j] = nearest_pos[i][j]
            queue += [(i - 1, j)]
        if j > 0 and nearest_dist[i][j - 1] == -1:
            nearest_dist[i][j - 1] = val+1
            nearest_pos[i][j-1] = nearest_pos[i][j]
            queue += [(i, j - 1)]
        if i < mapSize[0] - 1 and nearest_dist[i + 1][j] == -1:
            nearest_dist[i + 1][j] = val+1
            nearest_pos[i+1][j] = nearest_pos[i][j]
            queue += [(i + 1, j)]
        if j < mapSize[1] - 1 and nearest_dist[i][j + 1] == -1:
            nearest_dist[i][j + 1] = val+1
            nearest_pos[i][j+1] = nearest_pos[i][j]
            queue += [(i, j + 1)]

    return nearest_pos
