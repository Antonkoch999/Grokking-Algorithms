
def get_map(string_map):
    result = [[]]
    start, end = [], []
    i, j = 0, 0
    for ch in string_map:
        if ch == '\n':
            i += 1
            j = 0
            result.append([])
            continue
        if ch == 'S':
            start = [i, j]
        if ch == 'E':
            end = [i, j]
        result[i].append(ch)
        j += 1
    return result, start, end


def get_neighbours(list_map, pos, path=[]):
    neighbours = []
    i, j = pos[0], pos[1]
    if j - 1 >= 0 and list_map[i][j - 1] != '0' and [i, j - 1] not in path:
        neighbours.append([i, j - 1])
    if j + 1 < len(list_map[i]) and list_map[i][j + 1] != '0' and [i, j + 1] not in path:
        neighbours.append([i, j + 1])
    if i - 1 >= 0 and list_map[i - 1][j] != '0' and [i - 1, j] not in path:
        neighbours.append([i - 1, j])
    if i + 1 < len(list_map) and list_map[i + 1][j] != '0' and [i + 1, j] not in path:
        neighbours.append([i + 1, j])
    if neighbours:
        path.append(pos)
    return neighbours, path


def search(list_map, start, end, current=None, path=[]):
    if not current: current = start
    neighbours, path = get_neighbours(list_map, current, path)
    for x, y in neighbours:
        if [x, y] != [end[0], end[1]]:
            search(list_map, start, end, [x, y], path[:])
        else:
            print('\nResult:', path)
            return path


string_map = 'S**0E\n' \
             '***0*\n' \
             '*00**\n' \
             '****0'
print(string_map)
list_map, start, end = get_map(string_map)
search(list_map, start, end)
