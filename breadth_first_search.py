"""Check code in https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python."""


def get_len_and_prepare_maze(maze):
    new_maze = []
    maze_lst = maze.split('\n')
    len_maze = len(maze_lst)
    for el in maze_lst:
        new_maze.append(list(el.strip()))
    return len_maze, new_maze


def path_finder(maze):
    len_maze, prepare_maze = get_len_and_prepare_maze(maze)
    start = (0, 0)
    finish = (len_maze - 1, len_maze - 1)
    path = bfs(prepare_maze, start, finish)
    if path is not None:
        return True
    return False


def bfs(maze, start, finish):
    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]  # Required due to a quirk with tuples in Python
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == finish:
            return path
        elif front not in visited:
            for adjacent_space in get_adjacent_spaces(maze, front, visited):
                new_path = list(path)
                new_path.append(adjacent_space)
                queue.append(new_path)
            visited.add(front)
    return None


def get_adjacent_spaces(maze, space, visited):
    up = (space[0] - 1, space[1]) if space[0] - 1 >= 0 else None
    down = (space[0] + 1, space[1])
    left = (space[0], space[1] - 1) if space[1] - 1 >= 0 else None
    right = (space[0], space[1] + 1)
    spaces = [up, down, left, right]

    final = list()
    for i in spaces:
        if i is None:
            continue
        try:
            if maze[i[0]][i[1]] != 'W' and i not in visited:
                final.append(i)
        except IndexError:
            continue
    return final


def path_finder_from_codewars(maze):
    matrix = list(map(list, maze.splitlines()))
    stack, length = [[0, 0]], len(matrix)
    while stack:
        x, y = stack.pop()
        if matrix[x][y] == '.':
            matrix[x][y] = 'x'
            for x, y in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):
                if 0 <= x < length and 0 <= y < length:
                    stack.append((x, y))
    return matrix[length - 1][length - 1] == 'x'
