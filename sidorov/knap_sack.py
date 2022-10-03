def simple_knap_sack(max_weight, list_weights):
    """Стоимость пропорц. весу (simple). max_weigh - макс. вместимость рюкзака, list_weights - веса доступных вещей."""
    n = len(list_weights)
    D = [[0 for _ in range(n + 1)] for _ in range(max_weight + 1)]
    for i in range(n):
        for new_w in range(1, max_weight + 1):
            D[new_w][i + 1] = D[new_w][i]
            if list_weights[i] <= new_w:
                D[new_w][i + 1] = max(
                    D[new_w][i + 1],
                    D[new_w - list_weights[i]][i] + list_weights[i]
                )
    return D[max_weight][n]


print(simple_knap_sack(10, [1, 4, 8]))
