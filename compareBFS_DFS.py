

def BFS(adjacency_lst, start_node, stop_node):
    color = {u: "WHITE" for u in adjacency_lst}
    distance = {u: float("inf") for u in adjacency_lst}
    parent = {u: None for u in adjacency_lst}

    s = [start_node]
    color[start_node] = "GREY"
    distance[start_node] = 0
    comparison = 0

    while s:
        node = s.pop(0)

        for adjacent_node in adjacency_lst[node]:
            if color[adjacent_node] == "WHITE":
                color[adjacent_node] = "GREY"
                distance[adjacent_node] = distance[node] + 1
                parent[adjacent_node] = node
                
                comparison += 1
                if adjacent_node == stop_node:
                    return comparison
     
                s.append(adjacent_node)

        color[node] = "BLACK"

    return "There is no path"


def DFS(adjacency_lst,start_node, stop_node):
    color = {u:"WHITE" for u in adjacency_lst}
    time = {u:[0,0] for u in adjacency_lst}
    parent = {u:None for u in adjacency_lst}
    tracktime = 0
    comparison = 0
    
    def VisitDfs(u,stop_node):
        color[u] = "GRAY"
        nonlocal comparison
        if u == stop_node:
            return comparison

        nonlocal tracktime
        tracktime += 1
        time[u][0] = tracktime
        for v in adjacency_lst[u]:
            if color[v] == "WHITE":
                parent[v] = u
                comparison += 1
                new_path = VisitDfs(v,stop_node)
                if new_path:
                    return new_path
        color[u] = "BLACK"

        tracktime += 1
        time[u][1] = tracktime

    path = VisitDfs(start_node,stop_node)
    if path:
        return path
    return "Path not found" 


def compareDFS_BFS(adjacency_lst,start_node,stop_node):
    pathDFS = DFS(adjacency_lst,start_node,stop_node)
    pathBFS = BFS(adjacency_lst,start_node,stop_node)
    return f"Steps taken in BFS: {pathBFS}, Steps taken in DFS: {pathDFS}"

def main():
    filename = "/home/janu-chaudhary/Desktop/AI_Class/AI/graph.txt"  

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            adjacency_lst = lines[0].strip()
            start_node = lines[1].strip()
            stop_node = lines[2].strip()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except Exception as e:
        return f"Error: Could not read file - {e}"

    try:
        adjacency_lst = eval(adjacency_lst)
    except (SyntaxError, NameError) as e:
        return f"Error: Invalid adjacency list format - {e}"
    
    return compareDFS_BFS(adjacency_lst, start_node, stop_node)

if __name__ == "__main__":
    result = main()
    print(result)
