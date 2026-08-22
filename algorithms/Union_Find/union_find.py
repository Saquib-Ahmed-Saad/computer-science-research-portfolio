class UnionFind:

    def __init__(self, nodes):
        self.parent = {}

        # Initially, every node is its own parent.
        for node in nodes:
            self.parent[node] = node

    def find(self, node):

        # Follow parents until we reach the root.
        while self.parent[node] != node:
            node = self.parent[node]

        return node

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        # Join the two sets if they are different.
        if root1 != root2:
            self.parent[root2] = root1

nodes = ["A", "B", "C", "D"]

uf = UnionFind(nodes)

uf.union("A", "B")
uf.union("C", "D")

print(uf.find("A"))
print(uf.find("B"))

uf.union("B", "C")

print(uf.find("D"))
