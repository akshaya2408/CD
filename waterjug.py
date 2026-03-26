import heapq
def heuristic(state,target):
    return abs(state[0]-target)+abs(state[1]+target)
def waterjug(cap1,cap2,target):
    start=(0,0)
    pq=[]
    heapq.heappush(pq,(0,start))
    g_cost={start:0}
    parent={}
    while pq:
        f,curr=heapq.heappop(pq)
        x,y=curr
        if x==target or y==target:
            path=[]
            while curr in parent:
                path.append(curr)
                curr=parent[curr]
            path.append(start)
            return path[::-1]
        states=[(cap1,y),(x,cap2),(0,y),(x,0),(max(0,x-(cap2-y)),min(cap2,x+y)),(min(cap1,x+y),max(0,y-(cap1-x)))]
        for s in states:
            new_g=g_cost[curr]+1
            if s not in g_cost or new_g<g_cost[s]:
                g_cost[s]=new_g
                f=new_g+heuristic(s,target)
                heapq.heappush(pq,(f,s))
                parent[s]=curr
print(waterjug(4,3,2))
