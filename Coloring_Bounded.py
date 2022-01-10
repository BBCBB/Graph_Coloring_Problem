
f = open("C:\\Users\data\data_file","r")
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

ub=6
class node:
    def __init__(self,degree,color,neighbors,satdeg):
        self.degree=degree
        self.color=-1
        self.neighbors=neighbors
        self.satdeg=0
        

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
    nodes[i]=node(deg[i],0,ngbr[i],0)
    
#main loop
order=sorted(range(len(deg)), key=lambda k: deg[k], reverse=True)     # order based on the degree of the nodes
solution=[-1]*node_count
sat=[0]*node_count
while -1 in solution:
    if sum(solution)==-node_count:
        i=order[0]
    else:
        tp=[]
        ordsat=sorted(range(len(sat)), key=lambda k: sat[k], reverse=True)
        grbg=[]
        for j in ordsat:
            if solution[j]!=-1:
                grbg.append(j)
                if len(grbg)==node_count-solution.count(-1):
                    break
        ordsat=[k for k in ordsat if k not in grbg]
        for j in ordsat:
            tp.append(sat[j])
        if tp.count(max(tp))==1:
            ind=tp.index(max(tp))
            i=ordsat[ind]
        else:
            tp2=[]
            for l,m in enumerate(ordsat):
                if tp[l]==max(tp):
                    tp2.append(m)
                    if len(tp2)==tp2.count(max(tp2)):
                        break
            for e in order:
                if e in tp2:
                    i=e
                    break
    temp=[]
    colors=range(node_count)
    for j in nodes[i].neighbors:
        temp.append(nodes[j].color)
    colors = [k for k in colors if k not in temp]
    if min(colors)<ub:
        nodes[i].color=min(colors)
        solution[i]=min(colors)
        for n in nodes[i].neighbors:
            nodes[n].satdeg +=1    
            sat[n] += 1
    else:
        pri=0
        for n in nodes[i].neighbors:
            if nodes[n].color!=-1:
               nodes[n].color=-1
               nodes[n].satdeg -=1
               sat[n] -= 1
               solution[n]=-1
            pri=max(pri,nodes[n].satdeg)
        sat[i]=pri+1
        

chromatic_number=len(set(solution))     

output_data = str(chromatic_number) + '\n'
output_data += ' '.join(map(str, solution))
print(output_data)
