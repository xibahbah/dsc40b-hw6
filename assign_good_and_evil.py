def assign_good_and_evil(graph):
  

    color = {}   

    for start in graph.nodes:
        if start not in color:

            color[start] = 'good'
            queue = [start]   

            while queue:
                u = queue.pop(0)   

                for v in graph.neighbors(u):
                    if v not in color:
                        color[v] = 'evil' if color[u] == 'good' else 'good'
                        queue.append(v)
                    else:
                        if color[v] == color[u]:   # conflict
                            return None

    return color
