# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint

def graphfn(n):  # Генерация графа по принципу, как я понял условие задания

    graph = []
    for i in range(n):
        graph.append([i for i in range(randint(0,n))])
        if i in graph[i]: graph[i].remove(i)
    return graph

graph = graphfn(int(input("Введите количество вершин: ")))
print(graph)



def deep(start, graph, is_visited):  # Обход в глубину. Т.к. В условии написан просто обход,
                                    # то собсна просто обходим, без доп действий. Обход с первой вершины в списке.
    is_visited.add(start)
    for i in graph[start]:
        if i not in is_visited:
            deep(i, graph, is_visited) # Если есть не посещенные соседи вызываем рекурсию для этого соседа
is_visited = set()  # Храним посещенные вершины

m = 0 # Счетчик компонент для примера
for i, row in enumerate(graph):
    if i not in is_visited:
        deep(0,graph,is_visited)
        m += 1
print(is_visited)

# Еще вариант


visited = set()  # Храним посещенные вершины



def dfs(v):
    if v in visited:  # Если вершина уже посещена, выходим
        return
    visited.add(v)  # Посетили вершину v
    for i in graph[v]:  # Все смежные с v вершины
        if not i in visited:
            dfs(i)


start = 1
dfs(start)  # start - начальная вершина обхода, заданная в ручную
print(visited)





