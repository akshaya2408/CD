import heapq
def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def astar(grid,start,goal):
    rows,cols=len(grid),len(grid[0])
    open=[]
    heapq.heappush(open,(0,start))
    g_cost={start:0}
    f_cost={start:heuristic(start,goal)}
    parent={}
    while open:
        _,curr=heapq.heappop(open)
        if curr==goal:
            path=[]
            while curr in parent:
                path.append(curr)
                curr=parent[curr]
            path.append(start)
            return path[::-1]
        x,y=curr
        neigh={(x+1,y),(x,y+1),(x-1,y),(x,y-1)}
        for nx,ny in neigh:
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                temp_g=g_cost[curr]+1
                if (nx,ny) not in g_cost or temp_g < g_cost[(nx,ny)]:
                    parent[(nx,ny)]=curr
                    g_cost[(nx,ny)]=temp_g
                    f_cost[(nx,ny)]=temp_g+heuristic((nx,ny),goal)
                    heapq.heappush(open,(f_cost[(nx,ny)],(nx,ny)))
    return None
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path exists")
