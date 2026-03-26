import heapq
def astar_graph(graph,heuristic,start,goal):
    pq=[]
    heapq.heappush(pq,(0,start))
    g_cost={start:0}
    parent={}
    while pq:
        f,curr=heapq.heappop(pq)
        if curr==goal:
            path=[]
            while curr in parent:
                path.append(curr)
                curr=parent[curr]
            path.append(start)
            return path[::-1]
        for neigh,cost in graph[curr]:
            new_g=g_cost[curr]+cost
            if neigh not in g_cost or new_g<g_cost[neigh]:
                g_cost[neigh]=new_g
                f=new_g+heuristic[neigh]
                heapq.heappush(pq,(f,neigh))
                parent[neigh]=curr
graph={
'A':[('B',1),('C',3)],
'B':[('D',1)],
'C':[('D',1)],
'D':[]
}

heuristic={
'A':3,
'B':2,
'C':1,
'D':0
}

print(astar_graph(graph,heuristic,'A','D'))