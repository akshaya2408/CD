import heapq
goal=(1,2,3,4,5,6,7,8,0)
def heuristic(state):
    h=0
    for i,v in enumerate(state):
        if v!=0:
            goal_pos=goal.index(v)
            x1,y1=divmod(i,3)
            x2,y2=divmod(goal_pos,3)
            h+=abs(x1-x2)+abs(y1-y2)
    return h
def neigh(state):
    i=state.index(0)
    x,y=divmod(i,3)
    moves=[]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            ni=nx*3+ny
            new=list(state)
            new[i],new[ni]=new[ni],new[i]
            moves.append(tuple(new))
    return moves
def astar(start):
    pq=[]
    heapq.heappush(pq,(heuristic(start),0,start))
    vist=set()
    while pq:
        f,g,curr=heapq.heappop(pq)
        if curr==goal:
            return g
        vist.add(curr)
        for n in neigh(curr):
            if n not in vist:
                heapq.heappush(pq,(g+1+heuristic(n),g+1,n))
start = (1,2,3,4,0,6,7,5,8)

print("Steps:", astar(start))

