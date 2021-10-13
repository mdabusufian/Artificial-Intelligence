#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


graph={
    'S':{'A':2,'B':1,},
    'A':{'C':2,'D':3},
    'B':{'D':4,'E':4},
    'C':{'G':4},
    'D':{'G':4},
    'E':{},
    'G':{}
    }

def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
 
    if start == goal:
        return "That was easy! Start = goal"
 
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
 
            
            explored.append(node)
 
    return "So sorry, but a connecting path doesn't exist"
 
bfs_shortest_path(graph, 'S', 'G')


# In[ ]:





# In[8]:


from queue import Queue

 

graph={

 

    'S':{'A':2,'B':2,},

 

    'A':{'C':2,'D':3},

 

    'B':{'D':4,'E':4},

 

    'C':{'G':4},

 

    'D':{'G':4},

 

    'E':{},

 

    'G':{}

 

    }

 

def breadthFast(startNode, destNode):
    visited = {} # to store explored nodes
    distance = {}
    parent = {} # to store path

 

    exlpored = [] 
    frontier = Queue()

 

    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        distance[node] = -1

 

    startPoint = startNode
    visited[startNode] = True
    distance[startNode] = 0
    frontier.put(startNode)   
    found = False

 

    while not frontier.empty():
        u = frontier.get()     
        exlpored.append(u)

 

        for v in graph[u].keys():
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + graph[u][v]
                frontier.put(v)
                if v== destNode:
                    found =True
                    break

 

        if found: break

 

    g = destNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

 

    path.reverse()
    print("Breadth-First Search Path Secquence:")
    print(path)
    print("Path-Cost:")
    print(distance[destNode])

 

breadthFast('S','G')


# In[ ]:





# In[ ]:




