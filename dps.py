class Node:
    def __init__(self,name,children=[]):
        self.color = 'white'
        self.children = children
        self.discover_time = -1
        self.final_time = -1
        self.name = name

    def __str__(self):
        return self.name + " " + str(self.discover_time) + "/" + str(self.final_time)

#def breadth_first_search(node, time):

def depth_first_search(node, time):
    if node.color == 'white':
        node.color = 'grey'
        node.discover_time = time
        time = time + 1
        for n in node.children:
            if n.color == 'white':
                time = depth_first_search(n, time)
        node.final_time = time
        time = time + 1
        node.color = 'black'
    return time

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_g = Node('G')
nodes = [node_g, node_f, node_e, node_d, node_c, node_b, node_a]

node_g.children = [node_e,node_d]
node_e.children = [node_g,node_c]
node_d.children = [node_c,node_a]
node_c.children = []
node_b.children = [node_e,node_c]
node_a.children = [node_f,node_c,node_b]

time = 0
depth_first_search(node_g, time)
print(str(node_a))
print(str(node_b))
print(str(node_c))
print(str(node_d))
print(str(node_e))
print(str(node_f))
print(str(node_g))
