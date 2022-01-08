
f = open("C:\\Users\data_file","r")
input_data = ''.join(f.readlines())

lines = input_data.split('\n')

first_line = lines[0].split()
node_count = int(first_line[0])
edge_count = int(first_line[1])
edges = []
for i in range(1, edge_count + 1):
    line = lines[i]
    parts = line.split()
    edges.append((int(parts[0]), int(parts[1])))

# build a trivial solution
# every node has its own color

# solution = range(0, node_count)
class node:
    def __init__(self,degree,color,neighbors):
        self.degree=degree
        self.color=-1
        self.neighbors=neighbors
        

nodes=[0]*node_count 
deg=[0]*node_count            # these 6 lines calculate the degree of each node
ngbr=[]
for i in range(node_count):
    ngbr.append([])
for i in range(node_count):    
    for j in range(len(edges)):
        for k in range(2):
            if edges[j][k]==i:
                deg[i]=deg[i]+1
                if k==0:
                    ngbr[i].append(edges[j][1])
                else:
                    ngbr[i].append(edges[j][0])

for i in range(node_count):
    nodes[i]=node(deg[i],0,ngbr[i])
    
#main loop
order=sorted(range(len(deg)), key=lambda k: deg[k], reverse=True)
for i in order:
    temp=[]
    colors=range(node_count)
    # if nodes[i].color==-1:
    for j in nodes[i].neighbors:
        temp.append(nodes[j].color)
    colors = [k for k in colors if k not in temp]
    nodes[i].color=min(colors)
solution=[]
for l in range(len(nodes)):
    # print(nodes[l].color)
    solution.append(nodes[l].color)
chromatic_number=len(set(solution))     

output_data = str(chromatic_number) + '\n'
output_data += ' '.join(map(str, solution))
print(output_data)                              #First line shows the chromatic number of the graph and the second line the number attributed to a color which is assigned to each node
