def bfs(graph,root):
    visited = []
    queue = [root]
    while queue:
        X =queue.pop(0)
        visit(X)
        for i in graph[X]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

def visit(n):
    print(n)

graph = {"a":["b","c"],
         "b":[],
         "c":["d"],
         "d":[]
        }

bfs(graph,"a")