maze_size = 6
obstacles = [(0, 1), (1, 1), (4, 1), (4, 2), (3, 2), (4, 3), (3, 4), (8, 4), (3, 5)]  
start = (0, 0)  
goal = (0, 5) 


def is_valid(x, y):
    return (0 <= x < maze_size) and (0 <= y < maze_size) and (x, y) not in obstacles


def dfs(current, visited, path):
    x, y = current
    if current == goal:
        path.append(current)
        return True
    visited.add(current)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for move in moves:
        if is_valid(*move) and move not in visited:
            if dfs(move, visited, path):
                path.append(current)
                return True
    return False


from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])]) 
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        x, y = current

        
        if current == goal:
            return path + [current]

        
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            if is_valid(*move) and move not in visited:
                visited.add(move)
                queue.append((move, path + [current]))

    return None 

visited = set()
path_dfs = []
if dfs(start, visited, path_dfs):
    path_dfs.reverse()
    print("Path found (DFS):")
    for position in path_dfs:
        print(position)
else:
    print("No path found (DFS)!")

path_bfs = bfs(start, goal)
if path_bfs:
    print("\nPath found (BFS):")
    for position in path_bfs:
        print(position)
else:
    print("No path found (BFS)!")
