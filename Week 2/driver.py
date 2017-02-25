class board:


    # class Space:
    #     def __init__(self, value, neighbors = [None, None, None, None]): #[U,D,L,R]
    #         self.value = value
    #         self.neighbors = neighbors
    #     def link(self, node, direction): #direction relative to this node
    #         d = {0:1, 1:0, 2:3, 3:2}
    #         self.neighbors[direction] = node
    #         node.neighbors[d[direction]] = self



    def __init__(self, values):
        self.values = list(values)
        # for x in values:
        #     self.nodes.append(Node(x))
        #
        #     if values.index(x) < 3: #first row
        #         if values.index(x) != 0:
        #             self.nodes[values.index(x)].link(self.nodes[values.index(x)]- 1, 2)
        #
        #     else:
        #         self.nodes[values.index(x)].link(self.nodes[values.index(x)]- 3, 0)
        #         if values.index(x) != 3 and values.index(x) != 6:
        #             self.nodes[values.index(x)].link(self.nodes[values.index(x)]- 1, 2)

    def move(self, direction): #directions = [U,D,L,R]
        if direction == 0:
            if self.values.index(0) + 3 <= 5:
                self.values[self.values.index(0)], self.values[self.values.index(0) + 3] = self.values[self.values.index(0) + 3], self.values[self.values.index(0)]
            else:
                pass
        elif direction ==
