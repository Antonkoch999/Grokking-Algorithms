def edit_distance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    distance = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        distance[i][0] = i
    for j in range(m):
        distance[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = 0 if str1[i - 1] == str2[j - 1] else 1
            distance[i][j] = min(
                distance[i - 1][j] + 1,
                distance[i][j - 1] + 1,
                distance[i - 1][j - 1] + c,
            )
    return distance[i][j]


print(edit_distance('хлеб', 'похлеб'))
