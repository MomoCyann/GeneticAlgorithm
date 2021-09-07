#拓扑排序
graph = {
    1:[2,3,4,5],
    2:[6],
    3:[7],
    4:[8],
    5:[9],
    6:[10],
    7:[11],
    8:[11],
    9:[11],
    10:[12],
    11:[12],
    12:[],
}

def touuuupu(graph):
    count = 0
    deg = dict((i,0) for i in graph)
    #初始化节点数量
    for i in graph:
        for j in graph[i]:
            deg[j] += 1
    tmp = [i for i in graph if deg[i] == 0]
    res = []

    while tmp:
        i = tmp.pop()
        res.append(i)
        for j in graph[i]:
            deg[j] -= 1
            if deg[j] == 0:
                tmp.append(j)
    count += 1

    return res
result = []
result = touuuupu(graph)
print(result)