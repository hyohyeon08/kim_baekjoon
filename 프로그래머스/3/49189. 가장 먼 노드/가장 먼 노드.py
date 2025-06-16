from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = {start_node : 0}
    queue = deque([start_node])
    dep = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
        
        
    return visited

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    rbfs = bfs(graph, 1)
    max_depth  = max(rbfs.values())
    answer = 0

    for node, depth in rbfs.items():
        if depth == max_depth:
            answer += 1
    return answer