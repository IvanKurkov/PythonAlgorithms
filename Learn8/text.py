from collections import deque

parent = [-1, 2, 0, 0, 2, 6, 4, -1]
weight = [0, 10, 1, 1, 4, 6, 5, float("inf")]
way = [deque() for i in range(10)]


for i, n in enumerate(parent):
    if n != -1:
        way[i].appendleft(parent.index(n))
        way[i].appendleft(n)
    elif n == -1 and weight[i] != float('inf'):
        way[i].appendleft(parent.index(n))
    elif n == -1 and weight[i] == float('inf'):
        way[i].appendleft("Пути нет")
print(way)



def dikstra2(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float("inf")] * lenght
    parent = [-1] * lenght
    cost[start] = 0
    min_cost = 0
    way = []


    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:


                if cost[i] > cost[start] + vertex:
                    cost[i] = cost[start] + vertex
                    parent[i] = start



        min_cost = float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]

                start = i

        for i, n in enumerate(parent):
            if n != -1:
                way[i].append(parent.index(n))
                way[i].append(n)
            if n == -1:
                way[i].append(parent.index(n))
            # while n != -1:
            #
            #     x = parent[n]
            #     n = parent.index(x)
            #     way[i].append(parent.index(n))




    print(parent)
    print(way)
    return cost

#
# def displayShortestPath(graph, start, end,S):  # S - спимок кратчайших расстояний до всех вершин графа, возвращаемый из функции gejkstra()
#     Q = deque()
#     v = end
#     Q.append(v)  # Добавляем в очередь последнюю вершину.
#     while v is not start:  # Пока текущая вершина не является стартовой,
#         for n, x in enumerate(graph[v]):  # вычисляем для каждой из её соседей,
#             if S[v] == S[n] + graph[n][v]:  # совпадает ли сумма (кратч.расст. соседки + величина  ребра)  с кратч.расст. текущей вершины. Если да, то соседка принадлежит одному из кратч.путей.
#                 Q.appendleft(n)
#                 v = n
#
#
#
#     return Q


start = int(input("От какой вершины идем: "))
print(dikstra(g, start))

# S = dikstra(g, start)
# print(displayShortestPath(g, start, 3,S))