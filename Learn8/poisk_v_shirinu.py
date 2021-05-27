from collections import deque

gfr = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
def searchm(grf, start, finish):
    parent = [None for _ in range(len(grf))]
    is_visited = [False for _ in range(len(grf))]
    is_visited[start] = True
    deq = deque([start])
    while len(deq) > 0:
        curent = deq.pop()
        if curent == finish:
            break
        for i, vort in enumerate(grf[curent]):
            if vort == 1 and not is_visited[i]:
                is_visited[i] = True
                deq.appendleft(i)
                parent[i] = curent
    else:
        return f"Из вершины {start}, нельзя попасть в вершину {finish}"
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)
    return f"Путь из точки {start} в точку {finish} выглядит: {list(way)} и занимает {cost} шагов"

print(searchm(gfr, 2, 7))