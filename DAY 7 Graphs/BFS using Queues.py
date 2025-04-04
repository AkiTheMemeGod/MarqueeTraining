graph = {
    0:[1,2,3],
    1:[0, 4, 5],
    2:[0, 6],
    3:[0,7],
    4:[1],
    5:[1],
    6:[2],
    7:[3]
}
start = 0
visited = set()
queue = [start]
visited.add(start)

while queue:
    node = queue.pop(0)

    print(node, end= " ")

    for i in graph[node]:
        if i not in visited:
            visited.add(i)
            queue.append(i)
























