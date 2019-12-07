from PlayerInfo import PlayerInfo
from Map import Map
from PlayerInfo import PlayerInfo
from pprint import pprint


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def move_available(current_map: Map, other_player: PlayerInfo, x, y):
    return 0 <= x < current_map.width and 0 <= y < current_map.height and current_map.tiles[y][x]['item'] is None \
           and (other_player.x != x or other_player.y != y)


def can_move(current_map: Map, other_player: PlayerInfo, self_pos):
    for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if move_available(current_map, other_player, self_pos[0], self_pos[1]):
            return True
    return False


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze: Map, other_player: PlayerInfo, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure walkable terrain
            if not move_available(maze, other_player, node_position[0], node_position[1]) and node_position != end:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def find_path_to(player: PlayerInfo, other_info: PlayerInfo, current_map: Map, x, y):
    path = astar(current_map, other_info, (player.x, player.y), (x, y))
    if path is None:
        return [None]
    path_wasd = []
    for i in range(len(path) - 1):
        diff = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        if diff[1] == -1:
            path_wasd.append('w')
        if diff[0] == -1:
            path_wasd.append('a')
        if diff[1] == 1:
            path_wasd.append('s')
        if diff[0] == 1:
            path_wasd.append('d')
    return path_wasd


def find_resource_locations(current_map: Map, resource_type):
    coors = []

    for x in Map.items:

        if resource_type == 'wood':
            if x['itemType' == 'WOOD_SHOP']:
                coors.append((x['x'], x['y']))
        elif resource_type == 'stone':
            if x['itemType' == 'STONE_SHOP']:
                coors.append((x['x'], x['y']))
        else:
            if x['itemType' == 'METAL_SHOP']:
                coors.append((x['x'], x['y']))
    return coors


def direction(pos1: tuple, pos2: tuple) -> str:
    if pos1[1] == pos2[1] - 1:
        return 'w'
    if pos1[0] == pos2[0] - 1:
        return 'a'
    if pos1[1] == pos2[1] + 1:
        return 's'
    if pos1[0] == pos2[0] + 1:
        return 'd'


def find_path_to_nearest(current_map: Map, other_info: PlayerInfo, player: PlayerInfo, resource_type):
    min_len = 10000000
    pathoske = None
    loc_vec = find_resource_locations(current_map, resource_type)
    for loc in loc_vec:
        curr_pathoske = find_path_to(player, current_map, other_info, loc[0], loc[1])
        if len(curr_pathoske) < min_len:
            min_len = len(curr_pathoske)
            pathoske = curr_pathoske

    return pathoske


# return the position of the nearest item from pos[0], pos[1]
def find_nearest(pos: tuple, items: list):
    min_dist = -1
    min_dist_pos = None
    for item in items:
        curr_dist = dist(pos[0], pos[1], item['x'], item['y'])
        if min_dist_pos is None or curr_dist < min_dist:
            min_dist = curr_dist
            min_dist_pos = (item['x'], item['y'])

    return min_dist_pos


# ((WOOD)|(STONE)|(METAL))_SHOP
# ((SWORD)|(ARROW)|(SHIELD))_TOWER
def find_nearest_by_type(map: Map, pos: tuple, item: str):
    items = [i for i in map.items if i['itemType'] == item]
    return find_nearest(pos, items)


# a matrix of size mapSize[0],mapSize[1], having tuple of (x,y) pairs as elements
# which represent the position of the nearest item
def nearest_to_map(mapSize: tuple, items: list):
    nearest_dist = [[-1 for x in range(mapSize[1])] for y in range(mapSize[0])]
    nearest_pos = [[(-1, -1) for x in range(mapSize[1])] for y in range(mapSize[0])]

    # holds tuple of coors
    queue = []

    for item in items:
        i, j = item
        nearest_dist[i][j] = 0
        nearest_pos[i][j] = item
        if i > 0 and nearest_dist[i - 1][j] == -1:
            nearest_dist[i - 1][j] = 1
            nearest_pos[i - 1][j] = (i, j)
            queue += [(i - 1, j)]
        if j > 0 and nearest_dist[i][j - 1] == -1:
            nearest_dist[i][j - 1] = 1
            nearest_pos[i][j - 1] = (i, j)
            queue += [(i, j - 1)]
        if i < mapSize[0] - 1 and nearest_dist[i + 1][j] == -1:
            nearest_dist[i + 1][j] = 1
            nearest_pos[i + 1][j] = (i, j)
            queue += [(i + 1, j)]
        if j < mapSize[1] - 1 and nearest_dist[i][j + 1] == -1:
            nearest_dist[i][j + 1] = 1
            nearest_pos[i][j + 1] = (i, j)
            queue += [(i, j + 1)]

    curr_ind = 0
    while curr_ind != len(queue):
        i, j = queue[curr_ind]
        curr_ind += 1

        val = nearest_dist[i][j]

        if i > 0 and nearest_dist[i - 1][j] == -1:
            nearest_dist[i - 1][j] = val + 1
            nearest_pos[i - 1][j] = nearest_pos[i][j]
            queue += [(i - 1, j)]
        if j > 0 and nearest_dist[i][j - 1] == -1:
            nearest_dist[i][j - 1] = val + 1
            nearest_pos[i][j - 1] = nearest_pos[i][j]
            queue += [(i, j - 1)]
        if i < mapSize[0] - 1 and nearest_dist[i + 1][j] == -1:
            nearest_dist[i + 1][j] = val + 1
            nearest_pos[i + 1][j] = nearest_pos[i][j]
            queue += [(i + 1, j)]
        if j < mapSize[1] - 1 and nearest_dist[i][j + 1] == -1:
            nearest_dist[i][j + 1] = val + 1
            nearest_pos[i][j + 1] = nearest_pos[i][j]
            queue += [(i, j + 1)]

    return nearest_pos
