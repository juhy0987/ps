# 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260
# Silver 2
# solved

def main():
    N, M, V = map(int, input().split())
    E = {k: [] for k in range(1,N+1)}
    for _ in range(M):
        v1, v2 = map(int, input().split())
        E[v1].append(v2)
        E[v2].append(v1)
    
    for k, v in E.items():
        v.sort()
    
    visited = [False] * (N+1)
    s = [V]
    dfs = []
    while s:
        cur = s.pop()
        if visited[cur]:
            continue
        visited[cur] = True
        dfs.append(str(cur))
        
        for v in reversed(E[cur]):
            if not visited[v]:
                s.append(v)
    
    visited = [False] * (N+1)
    q = [V]
    bfs = []
    while q:
        cur = q.pop(0)
        if visited[cur]:
            continue
        visited[cur] = True
        bfs.append(str(cur))
        
        for v in E[cur]:
            if not visited[v]:
                q.append(v)
    
    print(" ".join(dfs))
    print(" ".join(bfs))
        

if __name__ == "__main__":
    main()